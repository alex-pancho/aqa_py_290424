import unittest
import os
import sqlite3
import csv
from homework_23 import SQLiteDB

class TestSQLiteDB(unittest.TestCase):

    def setUp(self):
        # Створення тестової бази даних
        self.db_name = 'test_example.db'
        self.db = SQLiteDB(self.db_name)
        self.table_name = 'test_table'
        self.columns = {
            'id': 'INTEGER PRIMARY KEY',
            'name': 'TEXT NOT NULL',
            'age': 'INTEGER',
            'email': 'TEXT UNIQUE'
        }
        self.db.create_table(self.table_name, self.columns)

    def tearDown(self):
        # Закриття з'єднання та видалення тестової бази даних
        self.db.close()
        if os.path.exists(self.db_name):
            try:
                os.remove(self.db_name)
            except PermissionError as e:
                print(f"Error removing file: {e}")

    def test_create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({self.table_name})")
            columns = cursor.fetchall()
            self.assertEqual(len(columns), 4)
            self.assertEqual(columns[0][1], 'id')
            self.assertEqual(columns[1][1], 'name')
            self.assertEqual(columns[2][1], 'age')
            self.assertEqual(columns[3][1], 'email')

    def test_insert_and_fetch(self):
        # Очистка таблиці перед вставкою нових записів
        self.db.delete_record(self.table_name, '1=1')  # Видалення всіх записів у таблиці
        self.db.insert_record(self.table_name, {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'})
        records = self.db.fetch_all_records(self.table_name)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]['name'], 'Alice')
        self.assertEqual(records[0]['age'], 30)
        self.assertEqual(records[0]['email'], 'alice@example.com')

    def test_delete_record(self):
        self.db.insert_record(self.table_name, {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'})
        self.db.delete_record(self.table_name, 'name = "Alice"')
        records = self.db.fetch_all_records(self.table_name)
        self.assertEqual(len(records), 0)

    def test_import_from_csv(self):
        with open('test.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'age', 'email'])
            writer.writerow(['Charlie', 35, 'charlie@example.com'])
            writer.writerow(['David', 40, 'david@example.com'])

        self.db.import_from_csv('test.csv')
        records = self.db.fetch_all_records('test')
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]['name'], 'Charlie')
        self.assertEqual(records[1]['name'], 'David')

        os.remove('test.csv')

    def test_export_to_csv(self):
        self.db.insert_record(self.table_name, {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'})
        self.db.insert_record(self.table_name, {'name': 'Bob', 'age': 25, 'email': 'bob@example.com'})

        self.db.export_to_csv(self.table_name, 'output.csv')
        with open('output.csv', 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]['name'], 'Alice')
            self.assertEqual(rows[1]['name'], 'Bob')

        os.remove('output.csv')

if __name__ == '__main__':
    unittest.main()
