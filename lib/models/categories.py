import sqlite3
from .database import Database

class Category:
    @staticmethod
    def create(name):
        with Database().connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
            conn.commit()

    @staticmethod
    def delete(category_id):
        with Database().connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
            conn.commit()

    @staticmethod
    def get_all():
        with Database().connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM categories")
            return cursor.fetchall()

    @staticmethod
    def find_by_id(category_id):
        with Database().connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM categories WHERE id = ?", (category_id,))
            return cursor.fetchone()