import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")
        return
    
    if length <= 0:
        print("Invalid input. Please enter a positive integer for the length.")
        return
    
    complexity = input("Enter the complexity of the password (uppercase, lowercase, digits, special - separated by comma): ").split(',')


    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated password:", password)

if __name__ == "__main__":
    main()