import sqlite3
from services.settings.database_base import DB_NAME, TABLES


class DB:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(
            DB_NAME,
            check_same_thread = False,
        )
        self.cursor = self.connection.cursor()
        self.create_tables()
    
    def execute(self, query : str, is_commit : bool = False) -> object:
        try:
            self.cursor.execute(query)
            if is_commit:
                self.connection.commit()
                return 0
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return 1
    
    def create_tables(self) -> object:
        for table_name in TABLES:
            query : str = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
            for field in TABLES[table_name]:
                query = query + f"{field} {TABLES[table_name][field]}\n"
            query += "\n)"
            self.execute(query = query, is_commit = True)

db : DB = DB()