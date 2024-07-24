import sqlite3

class DB_users:
    
    def __init__(self, filename: str) -> None:
            self.conn_to_db(filename)
        
    def conn_to_db(self, filename: str = ':memory:'):
            self.connection = sqlite3.connect(filename)
            self.cursor = self.connection.cursor()
        
        
    def create_table(self, table_name: str):
            create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            );"""
            self.cursor.execute(create_table_sql)
            self.connection.commit()
        

    def add_new_entry(self, table_name: str, data: dict):
            columns = ', '.join(data.keys())
            placeholders = ', '.join('?' for _ in data)
            insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(insert_sql, tuple(data.values()))
            self.connection.commit()

    def selection_of_all_records(self, table_name: str):
            select_sql = f"SELECT * FROM {table_name}"
            self.cursor.execute(select_sql)
            records = self.cursor.fetchall()
            return records


if __name__ == '__main__':
    db = DB_users("example.db")
    db.create_table('users')
    db.add_new_entry('users', {'name': 'Tanya', 'age': 26})
    db.add_new_entry('users', {'name': 'Vika', 'age': 18})
    records = db.selection_of_all_records('users')
    print('All records:', records)
    