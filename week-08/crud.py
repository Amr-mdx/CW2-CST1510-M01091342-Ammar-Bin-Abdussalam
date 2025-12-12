#inserting user
import sqlite3
from pathlib import Path
DB_PATH = Path("database/security.db")
def insert_user(user_id, username, email, password, role):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO users (user_id, username, email, password, role)
        VALUES (?, ?, ?, ?, ?)""", (user_id, username, email, password, role))
    conn.commit()
    conn.close()

#get all users
def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

#updating
def update_user_role(user_id, new_role):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""UPDATE users
        SET role = ?
        WHERE user_id = ?""", (new_role, user_id))
    conn.commit()
    conn.close()

#deleting
def delete_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM users
        WHERE user_id = ?""", (user_id,))
    conn.commit()
    conn.close()

