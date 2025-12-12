import sqlite3
from pathlib import Path
import pandas as pd
DB_PATH = Path("database/security.db")
def get_all_incidents_with_details():
    conn = sqlite3.connect(DB_PATH)
    query = """SELECT 
            incidents.incident_id,
            users.username,
            devices.device_name,
            incidents.incident_type,
            incidents.severity,
            incidents.status
        FROM incidents
        JOIN users ON incidents.user_id = users.user_id
        JOIN devices ON incidents.device_id = devices.device_id"""
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

#counting incidents by severity
def get_incidents_by_type_count():
    conn = sqlite3.connect(DB_PATH)
    query = """SELECT incident_type, COUNT(*) AS count
        FROM incidents
        GROUP BY incident_type
        ORDER BY count DESC"""
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

#high severity incidents
def get_high_severity_by_status():
    conn = sqlite3.connect(DB_PATH)
    query = """SELECT status, COUNT(*) AS count
        FROM incidents
        WHERE severity = 'high'
        GROUP BY status"""
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

