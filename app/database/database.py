import sqlite3


class Database:
    def __init__(self, db_name: str | None = None):
        self.db_name = f"{db_name}.db" if db_name is not None else "tasks.db"
        [self.cursor, self.conn] = self.start_connection()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS tasks(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                description TEXT NOT NULL,
                                status BOOLEAN NOT NULL DEFAULT false
                            )"""
        )
        self.conn.commit()  # commit the changes

    def start_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.row_factory = sqlite3.Row
        return [self.cursor, self.conn]

    def close_connection(self):
        self.conn.close()
        print("Conexão encerrada!")
        return None

    def execute_query(self, query: str):
        [cursor, conn] = self.start_connection()
        cursor.execute(query)
        conn.commit()  # commit the changes
        return self.close_and_return()

    def close_and_return(self):
        rows = self.cursor.fetchall()
        self.close_connection()
        return rows

    def get_all_data(self, query: str):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows
