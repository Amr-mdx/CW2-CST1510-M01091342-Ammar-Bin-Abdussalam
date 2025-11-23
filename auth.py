import bcrypt
import os
import re

USER_DATA_FILE = "users.txt"


def hash_password(plain_text_password: str) -> str:
      """Hash a plaintext password using bcrypt and return the hashed string.

      The returned value is a UTF-8 decoded string safe for text file storage.
      """
      if not isinstance(plain_text_password, (str, bytes)):
            raise TypeError("Password must be a string or bytes")
      pw_bytes = (
            plain_text_password.encode("utf-8")
            if isinstance(plain_text_password, str)
            else plain_text_password
      )
      hashed = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())
      return hashed.decode("utf-8")


def verify_password(plain_text_password: str, hashed_password: str) -> bool:
      """Return True if plain_text_password matches the hashed_password.

      hashed_password must be the string form as returned by hash_password.
      """
      if isinstance(plain_text_password, str):
            pw_bytes = plain_text_password.encode("utf-8")
      else:
            pw_bytes = plain_text_password
      try:
            return bcrypt.checkpw(pw_bytes, hashed_password.encode("utf-8"))
      except (ValueError, TypeError):
            return False


def user_exists(username: str) -> bool:
      """Return True if username already exists in the user data file."""
      if not os.path.exists(USER_DATA_FILE):
            return False
      with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                  line = line.strip()
                  if not line:
                        continue
                  stored_user, _ = line.split(":", 1)
                  if stored_user == username:
                        return True
      return False


def register_user(username: str, password: str) -> bool:
      """Register a new user by appending username:hashed_password to the file.

      Returns True on success, False on failure (e.g., user exists).
      """
      if user_exists(username):
            return False
      hashed = hash_password(password)
      with open(USER_DATA_FILE, "a", encoding="utf-8") as f:
            f.write(f"{username}:{hashed}\n")
      return True


def login_user(username: str, password: str) -> bool:
      """Attempt to login. Returns True if credentials are valid."""
      if not os.path.exists(USER_DATA_FILE):
            return False
      with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                  line = line.strip()
                  if not line:
                        continue
                  try:
                        stored_user, stored_hash = line.split(":", 1)
                  except ValueError:
                        continue
                  if stored_user == username:
                        return verify_password(password, stored_hash)
      return False


def validate_username(username: str) -> tuple[bool, str]:
      """Validate username: 3-32 chars, alphanumeric and underscore only."""
      if not username:
            return False, "Username cannot be empty"
      if not re.fullmatch(r"[A-Za-z0-9_]{3,32}", username):
            return (
                  False,
                  "Username must be 3-32 characters and only contain letters, digits, or underscores",
            )
      if user_exists(username):
            return False, "Username already exists"
      return True, ""


def validate_password(password: str) -> tuple[bool, str]:
      """Validate password with basic strength rules."""
      if not password or len(password) < 8:
            return False, "Password must be at least 8 characters"
      if len(password) > 128:
            return False, "Password is too long"
      if not re.search(r"[A-Z]", password):
            return False, "Password must include at least one uppercase letter"
      if not re.search(r"[a-z]", password):
            return False, "Password must include at least one lowercase letter"
      if not re.search(r"[0-9]", password):
            return False, "Password must include at least one digit"
      return True, ""


def display_menu():
      """Displays the main menu options."""
      print("\n" + "=" * 50)
      print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
      print(" Secure Authentication System")
      print("=" * 50)
      print("\n[1] Register a new user")
      print("[2] Login")
      print("[3] Exit")
      print("-" * 50)


def main():
      """Main program loop."""
      print("\nWelcome to the Week 7 Authentication System!")

      while True:
            display_menu()
            choice = input("\nPlease select an option (1-3): ").strip()

            if choice == "1":
                  # Registration flow
                  print("\n--- USER REGISTRATION ---")
                  username = input("Enter a username: ").strip()

                  # Validate username
                  is_valid, error_msg = validate_username(username)
                  if not is_valid:
                        print(f"Error: {error_msg}")
                        continue

                  password = input("Enter a password: ").strip()
                  is_valid, error_msg = validate_password(password)
                  if not is_valid:
                        print(f"Error: {error_msg}")
                        continue

                  # Confirm password
                  password_confirm = input("Confirm password: ").strip()
                  if password != password_confirm:
                        print("Error: Passwords do not match.")
                        continue

                  # Register the user
                  if register_user(username, password):
                        print("Registration successful.")
                  else:
                        print("Registration failed: user may already exist.")

            elif choice == "2":
                  # Login flow
                  print("\n--- USER LOGIN ---")
                  username = input("Enter your username: ").strip()
                  password = input("Enter your password: ").strip()

                  # Attempt login
                  if login_user(username, password):
                        print("\nYou are now logged in.")
                        print("(In a real application, you would now access the dashboard.)")
                  else:
                        print("\nLogin failed: invalid username or password.")

                  # Optional: pause before returning to menu
                  input("\nPress Enter to return to main menu...")

            elif choice == "3":
                  # Exit
                  print("\nThank you for using the authentication system.")
                  print("Exiting...")
                  break

            else:
                  print("\nError: Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
      main()