import sqlite3

def init_db():
    conn = sqlite3.connect("expense.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            amount REAL,
            note TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()
