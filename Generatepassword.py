import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    if length < 1:
        return "Error: Password length must be at least 1."
    password = ''.join(random.choices(characters, k=length))
    
    return password
def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
