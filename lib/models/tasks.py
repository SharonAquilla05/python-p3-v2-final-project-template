import sqlite3
from .database import Database

class Task:
    @staticmethod
    def create(title, user_id, category_id):
        with Database().connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (title, user_id, category_id) VALUES (?, ?, ?)",
                           (title, user_id, category_id))
            conn.commit()

    @staticmethod
    def delete(task_id):
        with Database().connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()

    @staticmethod
    def get_all():
        with Database().connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            return cursor.fetchall()

    @staticmethod
    def find_by_id(task_id):
        with Database().connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            return cursor.fetchone()



