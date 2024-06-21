import random
import string

def generate_password(length):
    # Define the character sets to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random choices from the characters set
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    # Prompt the user to enter the desired password length
    try:
        length = int(input("Enter the desired length for the password: "))
        
        # Ensure the length is a positive integer
        if length <= 0:
            print("Please enter a positive integer.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
