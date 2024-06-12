import sqlite3
from .database import Database

class Task:
    def __init__(self, title, user_id, category_id):
        self.title = title
        self.user_id = user_id
        self.category_id = category_id

    def save(self):
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO tasks (title, user_id, category_id) VALUES (?, ?, ?)",
                           (self.title, self.user_id, self.category_id))
            db.commit()

    @staticmethod
    def delete(task_id):
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            db.commit()

    @staticmethod
    def get_all():
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM tasks")
            return cursor.fetchall()

    @staticmethod
    def find_by_id(task_id):
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            return cursor.fetchone()

    @staticmethod
    def find_by_user(user_id):
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
            return cursor.fetchall()
