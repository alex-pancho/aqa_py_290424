import pytest
import sqlite3
from db_func import create_database, create_table, insert_record, select_all_records, delete_all_records


def test_create_database():
    db_name = "test.db"
    create_database(db_name)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    assert len(tables) == 0  # Після створення бази даних таблиць ще немає

    conn.close()


def test_create_table():
    db_name = "test.db"
    table_name = "test_table"
    columns = [("id", "INTEGER PRIMARY KEY"), ("name", "TEXT"), ("age", "INTEGER")]

    create_table(db_name, table_name, columns)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    table_exists = cursor.fetchone()

    assert table_exists is not None

    conn.close()


def test_insert_record():
    db_name = "test.db"
    table_name = "test_table"
    data = {"name": "Alice", "age": 30}

    insert_record(db_name, table_name, data)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()

    assert len(records) == 1
    assert records[0][1] == "Alice"
    assert records[0][2] == 30

    conn.close()


def test_select_all_records():
    db_name = "test.db"
    table_name = "test_table"

    records = select_all_records(db_name, table_name)

    assert len(records) > 0  # Повинні бути записи в таблиці


def test_delete_all_records():
    db_name = "test.db"
    table_name = "test_table"

    delete_all_records(db_name, table_name)
    records = select_all_records(db_name, table_name)

    assert len(records) == 0  # Після видалення 0 записів у таблиці


if __name__ == '__main__':
    pytest.main()
