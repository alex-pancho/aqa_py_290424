from pathlib import Path
from datetime import datetime

def convert_to_datetime(time_str):
    """
    Converts a time string in the format HH:MM:SS to a datetime object.
    """
    return datetime.strptime(time_str, '%H:%M:%S')

def log_heartbeat_issues(timestamps, log_file):
    """
    Analyzes the time intervals between consecutive timestamps
    and logs warnings and errors to a file.
    """
    with open(log_file, mode="a") as log:
        for idx in range(1, len(timestamps)):
            previous_time = timestamps[idx - 1]
            current_time = timestamps[idx]

            interval_seconds = (current_time - previous_time).total_seconds()

            if 30 < interval_seconds < 32:
                log.write(
                    f"WARNING: Interval of {interval_seconds} seconds between {previous_time.time()} and {current_time.time()}.\n")
            elif interval_seconds >= 32:
                log.write(
                    f"ERROR: Interval of {interval_seconds} seconds between {previous_time.time()} and {current_time.time()}.\n")

def analyze_log_file(log_file_path, output_log_path):
    """
    Reads the input log file, analyzes the timestamps, and logs the results.
    """
    timestamps = []

    with open(log_file_path, mode="r") as file:
        lines = file.readlines()

    for line in lines:
        if 'Timestamp' in line:
            parts = line.split('Timestamp ')
            if len(parts) > 1:
                timestamp_str = parts[1].split()[0].strip()
                try:
                    timestamps.append(convert_to_datetime(timestamp_str))
                except ValueError as e:
                    print(f"Failed to convert: {timestamp_str} - {e}")

    timestamps.sort()

    log_heartbeat_issues(timestamps, output_log_path)

if __name__ == "__main__":
    input_log_file = Path(__file__).parent / "hblog"
    output_log_file = Path(__file__).parent / "hb.log"
    analyze_log_file(input_log_file, output_log_file)
