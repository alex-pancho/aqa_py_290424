import logging
from pathlib import Path
import datetime


# Setup logging
log_filename = Path(__file__).parent / "hb.log"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

# Read log file
def read_log_file():
    log_filename = Path(__file__).parent / "hblog"
    with open(log_filename, mode="r") as f:
        lines = f.readlines()
    return lines

# Parse timestamps from log file content
def parse_timestamps(lines):
    timestamps = set()
    for line in lines:
        if 'Timestamp' in line:
            parts = line.split(' ')
            for part in parts:
                if part.startswith('Timestamp'):
                    timestamp_str = part.split('Timestamp')[1].strip()
                    timestamp = datetime.datetime.strptime(timestamp_str, '%H:%M:%S')
                    timestamps.add(timestamp)
    return sorted(timestamps)

# Compare timestamps and log warnings/errors
def compare_timestamps(timestamps):
    for i in range(1, len(timestamps)):
        time_diff = (timestamps[i] - timestamps[i-1]).total_seconds()
        if 30 < time_diff < 32:
            logging.warning(f"Heartbeat delay: {time_diff} seconds")
        elif time_diff >= 32:
            logging.error(f"Heartbeat delay: {time_diff} seconds")

# Main function to execute the monitoring process
def monitor_heartbeat():
    lines = read_log_file()
    timestamps = parse_timestamps(lines)
    compare_timestamps(timestamps)

if __name__ == "__main__":
    monitor_heartbeat()