import sqlite3

def get_connection():
    conn = sqlite3.connect("data/database.db")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clicks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            click_id TEXT NOT NULL UNIQUE,
            offer_id INTEGER NOT NULL,
            ip_address TEXT NOT NULL,
            user_agent TEXT NOT NULL,
            referer TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()