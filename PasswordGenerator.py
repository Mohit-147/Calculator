import random
import string

def generate_password(length):
    # Defining the different characters for password generator
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Taking input from user for password length
    length = int(input("Enter the desired length of the password: "))
    
    # Generating password
    if length < 6:
        print("Password length should be at least 6 characters.")
    else:
        password = generate_password(length)
        print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
