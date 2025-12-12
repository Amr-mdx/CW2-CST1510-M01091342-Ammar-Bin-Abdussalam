import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("database/security.db")
DATA_DIR = Path("DATA")
def load_csv_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    users_df = pd.read_csv(DATA_DIR / "users.csv")
    for _, row in users_df.iterrows():
        cursor.execute("""INSERT INTO users (user_id, username, email, password, role)
            VALUES (?, ?, ?, ?, ?)
        """, (row["user_id"], row["username"], row["email"], row["password"], row["role"]))

    devices_df = pd.read_csv(DATA_DIR / "devices.csv")
    for _, row in devices_df.iterrows():
        cursor.execute("""INSERT INTO devices (device_id, device_name, status)
            VALUES (?, ?, ?)
        """, (row["device_id"], row["device_name"], row["status"]))
    
    incidents_df = pd.read_csv(DATA_DIR / "incidents.csv")
    for _, row in incidents_df.iterrows():
        cursor.execute("""
            INSERT INTO incidents (incident_id, user_id, device_id, incident_type, severity, status)
            VALUES (?, ?, ?, ?, ?, ?)""", (row["incident_id"], row["user_id"], row["device_id"],
            row["incident_type"], row["severity"], row["status"]))
    conn.commit()
    conn.close()
load_csv_data()
