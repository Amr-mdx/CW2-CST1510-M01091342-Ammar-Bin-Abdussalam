import os
from auth import USER_DATA_FILE, register_user, login_user

# Start with a clean users file for the demo
if os.path.exists(USER_DATA_FILE):
    os.remove(USER_DATA_FILE)

print("Demo: register and login flow")
print("Registering: username=alice, password=TestPass123")
registered = register_user("alice", "TestPass123")
print("Registered:", registered)

print("\nContents of users.txt:")
with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
    print(f.read())

print("Attempt login with correct password:", login_user("alice", "TestPass123"))
print("Attempt login with incorrect password:", login_user("alice", "wrongpassword"))

# Cleanup after demo
os.remove(USER_DATA_FILE)
print("\nDemo complete.")
