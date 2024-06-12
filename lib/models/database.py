import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('tasks.db')
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """)
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """)
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                user_id INTEGER,
                category_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
            """)

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

database = Database()