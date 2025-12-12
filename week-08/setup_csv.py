import pandas as pd
from pathlib import Path

DATA_DIR = Path("DATA")
DATA_DIR.mkdir(exist_ok=True)

users_data = {"user_id": [1, 2, 3],
    "username": ["admin", "john", "sarah"],
    "email": ["admin@example.com", "john@example.com", "sarah@example.com"],
    "password": ["$2b$12$examplehash1", "$2b$12$examplehash2", "$2b$12$examplehash3"],
    "role": ["admin", "analyst", "staff"]}
pd.DataFrame(users_data).to_csv(DATA_DIR / "users.csv", index=False)

devices_data = {"device_id": [1, 2, 3],
    "device_name": ["Firewall", "Server-01", "Laptop-23"],
    "status": ["active", "active", "inactive"]}
pd.DataFrame(devices_data).to_csv(DATA_DIR / "devices.csv", index=False)

incidents_data = {"incident_id": [1, 2, 3],
    "user_id": [1, 2, 3],
    "device_id": [1, 2, 3],
    "incident_type": ["Malware", "Phishing", "Unauthorized Access"],
    "severity": ["high", "medium", "low"],
    "status": ["open", "investigating", "closed"]}
pd.DataFrame(incidents_data).to_csv(DATA_DIR / "incidents.csv", index=False)
