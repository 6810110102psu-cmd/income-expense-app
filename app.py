import sqlite3
from datetime import datetime

DB_NAME = "expense.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            amount REAL,
            note TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(t_type, amount, note=""):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (type, amount, note, date)
        VALUES (?, ?, ?, ?)
    """, (t_type, amount, note, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_all_transactions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT type, amount, note, date
        FROM transactions
        ORDER BY date DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()   # ⭐ สำคัญ
    data = get_all_transactions()
    for t in data:
        print(t)
