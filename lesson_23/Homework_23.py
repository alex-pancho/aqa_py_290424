import sqlite3
from typing import List, Tuple, Any, Dict
import csv
import unittest
import os


def create_database(db_name: str):
    return sqlite3.connect(db_name)


def create_table(connection, table_name, fields: Dict):
    fields_str = ', '.join([f'{name} {dtype}' for name, dtype in fields.items()])
    connection.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({fields_str});')
    connection.commit()


def insert_record(connection, table_name, record: Dict):
    fields = ', '.join(record.keys())
    placeholders = ', '.join(['?' for _ in record])
    values = tuple(record.values())
    connection.execute(f'INSERT INTO {table_name} ({fields}) VALUES ({placeholders});', values)
    connection.commit()


def select_all_records(connection, table_name):
    cursor = connection.execute(f'SELECT * FROM {table_name};')
    return cursor.fetchall()





def import_csv_to_table(connection, csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        table_name = csv_file.split('.')[0]
        fields = reader.fieldnames
        field_types = {field: 'TEXT' for field in fields}  # за замовчуванням всі поля мають тип TEXT

        create_table(connection, table_name, field_types)

        for row in reader:
            insert_record(connection, table_name, row)


def delete_record(connection, table_name, condition):
    connection.execute(f'DELETE FROM {table_name} WHERE {condition};')
    connection.commit()




class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db_name = 'test.db'
        self.connection = create_database(self.db_name)

    def tearDown(self):
        self.connection.close()
        os.remove(self.db_name)

    def test_create_table(self):
        create_table(self.connection, 'test_table', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT'})
        tables = self.connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_table';").fetchall()
        self.assertEqual(len(tables), 1)

    def test_insert_and_select_record(self):
        create_table(self.connection, 'test_table', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT'})
        insert_record(self.connection, 'test_table', {'id': 1, 'name': 'John Doe'})
        records = select_all_records(self.connection, 'test_table')
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0], (1, 'John Doe'))

    def test_import_csv_to_table(self):
        with open('test.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'name'])
            writer.writerow([1, 'John Doe'])
            writer.writerow([2, 'Jane Doe'])

        import_csv_to_table(self.connection, 'test.csv')
        records = select_all_records(self.connection, 'test')
        self.assertEqual(len(records), 2)

        os.remove('test.csv')

    def test_delete_record(self):
        create_table(self.connection, 'test_table', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT'})
        insert_record(self.connection, 'test_table', {'id': 1, 'name': 'John Doe'})
        delete_record(self.connection, 'test_table', 'id=1')
        records = select_all_records(self.connection, 'test_table')
        self.assertEqual(len(records), 0)

if __name__ == '__main__':
    unittest.main()