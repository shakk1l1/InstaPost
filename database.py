import sqlite3

def create_connection():
    conn = sqlite3.connect('images.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS posted_images (
                        id INTEGER PRIMARY KEY,
                        image_name TEXT NOT NULL UNIQUE
                      )''')
    conn.commit()
    conn.close()

def insert_image(image_path):
    conn = create_connection()
    cursor = conn.cursor()
    if '/' in image_path:
        image_name = image_path.split('/')[-1]
    else:
        image_name = image_path
    cursor.execute('INSERT INTO posted_images (image_name) VALUES (?)', (image_name,))
    conn.commit()
    conn.close()

def check_image(image_path):
    conn = create_connection()
    cursor = conn.cursor()
    image_name = image_path.split('/')[-1]
    cursor.execute('SELECT * FROM posted_images WHERE image_name = ?', (image_name,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def list_images():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posted_images')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

create_table()