import sqlite3

class DB_users():

    def __init__(self, filename:str) -> None:
        self.conn_to_db(filename)

    def conn_to_db(self, filename: str = ':memory:'):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def create_table(self, name:str, field_dict:dict):
        fields = [f"{field} {type_}" for field, type_ in field_dict.items()]
        fields = ", ".join(fields)
        sql = f'''
                CREATE TABLE IF NOT EXISTS {name} (
                id INTEGER PRIMARY KEY,
                {fields}
                )
               '''
        self.cursor.execute(sql)
        self.connection.commit()

    def add_record(self, table_name: str, data: dict):
        fields = ", ".join(data.keys())
        values = ", ".join(['?'] * len(data))
        sql = f"INSERT INTO {table_name} ({fields}) VALUES ({values})"
        self.cursor.execute(sql, tuple(data.values()))
        self.connection.commit()

    def select_all_records(self, table_name: str):
        sql = f"SELECT * FROM {table_name}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
