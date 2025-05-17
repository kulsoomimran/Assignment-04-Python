from hashlib import sha256

def generate_password_hash(password):

    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):

    if email in stored_logins:

        stored_hash = stored_logins[email]

        return stored_hash == generate_password_hash(password_to_check)
    
    return False

def main():

    stored_logins = {
        "user1@gmail.com": generate_password_hash("password123"),
        "user2@gmail.com": generate_password_hash("qwerty"),
        "kulsoom@gmail.com": generate_password_hash("123456"),
    }

    email = input("Enter your email: ")

    password_to_check = input("Enter your password: ")

    if login(email, stored_logins, password_to_check):
        print("Login successful!")
    else:
        print("Login failed!!!\nIncorrect email or password.")

if __name__ == "__main__":
    main()