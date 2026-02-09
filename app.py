import sqlite3
from datetime import datetime

DB_NAME = "expense.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def add_transaction(t_type, amount, note=""):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (type, amount, note, date)
        VALUES (?, ?, ?, ?)
    """, (t_type, amount, note, datetime.now()))

    conn.commit()
    conn.close()

# ดึงข้อมูล
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

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    data = get_all_transactions()
    for t in data:
        print(t)
