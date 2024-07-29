import sqlite3
from typing import Dict, Any, List
import csv

class SQLiteDB:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute('pragma foreign_keys = on')

    def close(self):
        if self.conn:
            self.conn.close()

    def create_table(self, table_name: str, columns: Dict[str, str]):
        cursor = self.conn.cursor()
        cols = ', '.join([f"{name} {dtype}" for name, dtype in columns.items()])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols})")
        self.conn.commit()

    def insert_record(self, table_name: str, record: Dict[str, Any]):
        cursor = self.conn.cursor()
        cols = ', '.join(record.keys())
        placeholders = ', '.join(['?' for _ in record])
        cursor.execute(f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})", tuple(record.values()))
        self.conn.commit()

    def fetch_all_records(self, table_name: str) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def delete_record(self, table_name: str, condition: str):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.conn.commit()

    def import_from_csv(self, csv_file: str):
        table_name = csv_file.split('.')[0]
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            columns = {field: 'TEXT' for field in reader.fieldnames}
            self.create_table(table_name, columns)
            for row in reader:
                self.insert_record(table_name, row)

    def export_to_csv(self, table_name: str, csv_file: str):
        records = self.fetch_all_records(table_name)
        if records:
            with open(csv_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=records[0].keys())
                writer.writeheader()
                writer.writerows(records)

