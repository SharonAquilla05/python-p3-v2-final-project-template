import sqlite3
from .database import Database

class User:
    def __init__(self, name):
        self.name = name

    def save(self):
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO users (name) VALUES (?)", (self.name,))
            db.commit()

    @staticmethod
    def delete(user_id):
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            db.commit()

    @staticmethod
    def get_all():
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()

    @staticmethod
    def find_by_id(user_id):
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            return cursor.fetchone()

