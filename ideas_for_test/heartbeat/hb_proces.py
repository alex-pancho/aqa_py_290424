from pathlib import Path
import logging

logging.basicConfig(filename="hblog", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

filename = Path(__file__).parent / "hblog"
print(filename)

with open(filename, mode="r") as f:
    lines = f.readlines()

previous_timestamp = None

for line in lines:
    timestamp_str = line.strip()
    try:
        timestamp = int(timestamp_str)
    except ValueError:
        logging.error(f"Invalid timestamp in log: {timestamp_str}")
        continue

    if previous_timestamp is not None:
        heartbeat = timestamp - previous_timestamp

        if 30 < heartbeat < 32:
            logging.warning(f"Heartbeat delay: {heartbeat} seconds")
        elif heartbeat >= 32:
            logging.error(f"Heartbeat delay: {heartbeat} seconds")

    previous_timestamp = timestamp

