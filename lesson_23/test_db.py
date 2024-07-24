import os
import sqlite3
import pytest
from db import DB_users

@pytest.fixture
def db():
    db = DB_users(':memory:')
    db.create_table('users')
    yield db
    db.connection.close()

def test_database_creation():
    db_filename = 'example.db'
    db = DB_users(db_filename)
    db.create_table('users')
    assert os.path.exists(db_filename), f"Error: Database file {db_filename} does not exist."

def test_create_table(db):
    db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    assert db.cursor.fetchone() is not None

def test_add_new_entry(db):
    db.add_new_entry('users', {'name': 'Yarosh', 'age': 33})
    db.cursor.execute("SELECT * FROM users WHERE name='Yarosh'")
    record = db.cursor.fetchone()
    assert record is not None
    assert record[1] == 'Yarosh'
    assert record[2] == 33

def test_selection_of_all_records(db):
    db.add_new_entry('users', {'name': 'Tanya', 'age': 26})
    db.add_new_entry('users', {'name': 'Vika', 'age': 18})
    records = db.selection_of_all_records('users')
    assert len(records) == 2
    assert records[0][1] == 'Tanya'
    assert records[0][2] == 26
    assert records[1][1] == 'Vika'
    assert records[1][2] == 18
