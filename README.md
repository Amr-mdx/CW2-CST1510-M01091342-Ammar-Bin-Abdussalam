Weak-07: Building a Secure Authentication System

studentname:Ammar
StudentID:M01091342
course:CST1510-CW2
#project explanation
This is a program secure authentication system, here it helps the user to register account and login using bcrypt,A command-line authentication system implementing secure password hashing This system allows users to register accounts and log in with proper pass
#features
- Secure password hashing using bcrypt with automatic salt generation
- User registration with duplicate username prevention
- User login with password verification
- Input validation for usernames and passwords
- File-based user data persistence
#technical implementation
- Hashing Algorithm: bcrypt with automatic salting
- Data Storage: Plain text file (`users.txt`) with comma-separated values
- Password Security: One-way hashing, no plaintext storage
- Validation: Username (3-20 alphanumeric characters), Password (6-50 characters)
