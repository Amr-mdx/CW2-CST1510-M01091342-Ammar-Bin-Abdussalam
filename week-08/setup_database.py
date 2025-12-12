import sqlite3
from pathlib import Path

DB_PATH = Path("database/security.db")
DB_PATH.parent.mkdir(exist_ok=True)
def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS devices (
            device_id INTEGER PRIMARY KEY,
            device_name TEXT NOT NULL,
            status TEXT NOT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS incidents (
            incident_id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            device_id INTEGER NOT NULL,
            incident_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (device_id) REFERENCES devices(device_id))""")
    conn.commit()
    conn.close()
create_tables()
