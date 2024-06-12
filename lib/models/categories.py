import sqlite3
from .database import Database

class Category:
    def __init__(self, name):
        self.name = name

    def save(self):
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO categories (name) VALUES (?)", (self.name,))
            db.commit()

    @staticmethod
    def delete(category_id):
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
            db.commit()

    @staticmethod
    def get_all():
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM categories")
            return cursor.fetchall()

    @staticmethod
    def find_by_id(category_id):
        with Database() as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM categories WHERE id = ?", (category_id,))
            return cursor.fetchone()
