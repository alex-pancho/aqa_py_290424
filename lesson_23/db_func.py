import sqlite3
from typing import List, Tuple, Dict


def create_database(db_name: str):
    conn = sqlite3.connect(db_name)
    conn.close()


def create_table(db_name: str, table_name: str, columns: List[Tuple[str, str]]):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Формуємо SQL запит для створення таблиці
    columns_def = ", ".join([f"{name} {data_type}" for name, data_type in columns])
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"

    cursor.execute(create_table_sql)
    conn.commit()
    conn.close()


def insert_record(db_name: str, table_name: str, data: Dict[str, any]):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Формуємо SQL запит для вставки запису
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?" for _ in data.values()])
    insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    cursor.execute(insert_sql, tuple(data.values()))
    conn.commit()
    conn.close()


def select_all_records(db_name: str, table_name: str) -> List[Tuple]:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    select_sql = f"SELECT * FROM {table_name}"
    cursor.execute(select_sql)
    records = cursor.fetchall()

    conn.close()
    return records


def delete_all_records(db_name: str, table_name: str):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    delete_sql = f"DELETE FROM {table_name}"
    cursor.execute(delete_sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # Создаем базу данных
    create_database("example.db")

    # Создаем таблицу
    create_table("example.db", "users", [("id", "INTEGER PRIMARY KEY"), ("name", "TEXT"), ("age", "INTEGER")])

    # Вставляем записи в таблицу
    insert_record("example.db", "users", {"name": "Alice", "age": 30})
    insert_record("example.db", "users", {"name": "Bob", "age": 25})

    # Получаем все записи из таблицы
    records = select_all_records("example.db", "users")
    print(records)  # [(1, 'Alice', 30), (2, 'Bob', 25)]

    # Удаляем все записи из таблицы
    delete_all_records("example.db", "users")

    # Проверяем, что таблица пустая
    records = select_all_records("example.db", "users")
    print(records)  # []

