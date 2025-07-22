import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), '..', 'bill_app.db')

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    mobile TEXT NOT NULL,
                    email TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    product_name TEXT NOT NULL,
                    category TEXT,
                    price REAL NOT NULL,
                    FOREIGN KEY(customer_id) REFERENCES customers(id))''')

    cur.execute('''CREATE TABLE IF NOT EXISTS bills (
                    bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    total REAL,
                    date TEXT,
                    FOREIGN KEY(customer_id) REFERENCES customers(id))''')

    cur.execute('''CREATE TABLE IF NOT EXISTS bill_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    bill_id INTEGER,
                    product_name TEXT,
                    quantity INTEGER,
                    price REAL,
                    FOREIGN KEY(bill_id) REFERENCES bills(bill_id))''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
