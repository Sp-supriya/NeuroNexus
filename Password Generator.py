import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("Password length should be greater than 0.")
            return
        
        # Define the characters to use
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        print(f"\nGenerated Password: {password}")
    
    except ValueError:
        print("Please enter a valid number.")

# Run the password generator
generate_password()
