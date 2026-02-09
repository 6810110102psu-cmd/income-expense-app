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

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    add_transaction("income", 5000, "เงินเดือน")
    add_transaction("expense", 120, "ข้าวกลางวัน")
    print("เพิ่มข้อมูลเรียบร้อย")
