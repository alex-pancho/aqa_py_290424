import unittest
from homework import DB_users

class TestDBUsers(unittest.TestCase):

    def setUp(self):
        self.db = DB_users(':memory:')
        self.table_name = "test_table"
        self.fields = {
            "name": "TEXT NOT NULL",
            "age": "INTEGER",
            "email": "TEXT"
        }
        self.db.create_table(self.table_name, self.fields)

    def tearDown(self):
        self.db.connection.close()

    def test_create_table(self):
        self.db.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table_name}'")
        table_exists = self.db.cursor.fetchone()
        self.assertIsNotNone(table_exists)

    def test_add_record(self):
        data = {"name": "Jane Doe", "age": 28, "email": "jane.doe@example.com"}
        self.db.add_record(self.table_name, data)
        self.db.cursor.execute(f"SELECT * FROM {self.table_name} WHERE name = 'Jane Doe'")
        record = self.db.cursor.fetchone()
        self.assertIsNotNone(record)
        self.assertEqual(record[1], "Jane Doe")
        self.assertEqual(record[2], 28)
        self.assertEqual(record[3], "jane.doe@example.com")

    def test_select_all_records(self):
        data1 = {"name": "Jane Doe", "age": 28, "email": "jane.doe@example.com"}
        data2 = {"name": "John Smith", "age": 35, "email": "john.smith@example.com"}
        self.db.add_record(self.table_name, data1)
        self.db.add_record(self.table_name, data2)
        records = self.db.select_all_records(self.table_name)
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0][1], "Jane Doe")
        self.assertEqual(records[1][1], "John Smith")

if __name__ == '__main__':
    unittest.main()
