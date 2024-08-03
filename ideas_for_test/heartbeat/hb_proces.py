from pathlib import Path
import re
from datetime import datetime


# Функция для конвертации времени в объект datetime
def time_to_datetime(time_str):
    return datetime.strptime(time_str, '%H:%M:%S')


# Функция для анализа интервалов времени
def analyze_intervals(timestamps, output_file):
    with open(output_file, mode="a") as log:
        for i in range(1, len(timestamps)):
            prev_time = timestamps[i - 1]
            curr_time = timestamps[i]

            # Вычисление интервала
            interval = curr_time - prev_time
            interval_seconds = interval.total_seconds()

            # Запись предупреждений и ошибок
            if 30 < interval_seconds < 32:
                log.write(
                    f"WARNING: Heartbeat interval of {interval_seconds} seconds detected between {prev_time.time()} and {curr_time.time()}.\n")
            elif interval_seconds >= 32:
                log.write(
                    f"ERROR: Heartbeat interval of {interval_seconds} seconds detected between {prev_time.time()} and {curr_time.time()}.\n")


# Основная функция
def process_log_file(input_file, output_file):
    timestamps = []

    with open(input_file, mode="r") as f:
        lines = f.readlines()

    for line in lines:
        match = re.search(r'Timestamp (\d{2}:\d{2}:\d{2})', line)
        if match:
            timestamp = match.group(1)
            timestamps.append(time_to_datetime(timestamp))

    # Сортировка временных меток
    timestamps.sort()

    # Анализ интервалов
    analyze_intervals(timestamps, output_file)


if __name__ == "__main__":
    input_filename = Path(__file__).parent / "hblog"
    output_filename = Path(__file__).parent / "hb.log"
    process_log_file(input_filename, output_filename)
