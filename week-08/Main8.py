from crud import get_all_users, insert_user, update_user_role, delete_user
from queries import get_all_incidents_with_details, get_incidents_by_type_count, get_high_severity_by_status
#Show all users
print("\n=== USERS ===")
print(get_all_users())

#Insert a new user
insert_user(10, "testuser", "test@example.com", "password123", "staff")
print("\n=== AFTER INSERT ===")
print(get_all_users())

#Update a user role
update_user_role(10, "manager")
print("\n=== AFTER UPDATE ROLE ===")
print(get_all_users())

#Delete a user
delete_user(10)
print("\n=== AFTER DELETE ===")
print(get_all_users())

#SQL QUERY FUNCTIONS
print("\n=== INCIDENTS WITH DETAILS (JOIN) ===")
print(get_all_incidents_with_details())
print("\n=== INCIDENT COUNT BY TYPE (GROUP BY) ===")
print(get_incidents_by_type_count())
print("\n=== HIGH SEVERITY INCIDENTS (FILTER + GROUP BY) ===")
print(get_high_severity_by_status())
