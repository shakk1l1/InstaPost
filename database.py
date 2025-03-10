# database.py
import sqlite3
from sqlite3 import Connection
from queue import Queue

class Database:
    def __init__(self, db_name='images.db', pool_size=5):
        self.db_name = db_name
        self.pool = Queue(maxsize=pool_size)
        for _ in range(pool_size):
            self.pool.put(self._create_connection())

    def _create_connection(self) -> Connection:
        return sqlite3.connect(self.db_name)

    def get_connection(self) -> Connection:
        return self.pool.get()

    def release_connection(self, conn: Connection):
        self.pool.put(conn)

    def execute(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        self.release_connection(conn)

    def fetchone(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        self.release_connection(conn)
        return result

    def fetchall(self, query, params=()):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        self.release_connection(conn)
        return result

db = Database()

def create_table():
    db.execute('''CREATE TABLE IF NOT EXISTS posted_images (
                    id INTEGER PRIMARY KEY,
                    image_name TEXT NOT NULL UNIQUE
                  )''')

def insert_image(image_path):
    image_name = image_path.split('/')[-1]
    db.execute('INSERT INTO posted_images (image_name) VALUES (?)', (image_name,))

def check_image(image_path):
    image_name = image_path.split('/')[-1]
    return db.fetchone('SELECT * FROM posted_images WHERE image_name = ?', (image_name,)) is not None

def print_images():
    rows = db.fetchall('SELECT * FROM posted_images')
    for row in rows:
        print(row)

create_table()