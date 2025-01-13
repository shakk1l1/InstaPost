import sqlite3

def create_connection():
    conn = sqlite3.connect('images.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS posted_images (
                        id INTEGER PRIMARY KEY,
                        image_path TEXT NOT NULL UNIQUE
                      )''')
    conn.commit()
    conn.close()

def insert_image(image_path):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posted_images (image_path) VALUES (?)', (image_path,))
    conn.commit()
    conn.close()

def check_image(image_path):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posted_images WHERE image_path = ?', (image_path,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

create_table()