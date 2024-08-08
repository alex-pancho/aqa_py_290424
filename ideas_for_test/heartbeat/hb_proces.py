from pathlib import Path
from datetime import datetime


def parse_timestamp(timestamp):
    return datetime.strptime(timestamp, "%H:%M:%S")

filename = Path(__file__).parent / "hblog"
output_log = Path(__file__).parent / "hb.log"

with open(filename, mode="r") as f:
    lines = f.readlines()

previous_timestamp = None

with open(output_log, mode="w") as log_file:
    for line in lines:

        start_idx = line.find("Timestamp") + len("Timestamp ")
        end_idx = line.find(" ", start_idx)
        if end_idx == -1:
            end_idx = len(line)
        timestamp_str = line[start_idx:end_idx]
        current_timestamp = parse_timestamp(timestamp_str)

        log_file.write(f"Parsed timestamp: {timestamp_str}\n")

        if previous_timestamp is not None:

            diff_seconds = (current_timestamp - previous_timestamp).total_seconds()

            if 30 < diff_seconds < 32:
                log_file.write(f"WARNING: Heartbeat interval is {diff_seconds} seconds at {timestamp_str}\n")
            elif diff_seconds >= 32:
                log_file.write(f"ERROR: Heartbeat interval is {diff_seconds} seconds at {timestamp_str}\n")

            log_file.write(f"Interval: {diff_seconds} seconds\n")

        previous_timestamp = current_timestamp


