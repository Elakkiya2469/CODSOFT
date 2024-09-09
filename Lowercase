import random
import string

class PasswordGenerator:
    def _init_(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.symbols = string.punctuation
        self.all_characters = self.lowercase + self.uppercase + self.numbers + self.symbols

    def generate_password(self, length):
        password = ""
        for _ in range(length):
            password += random.choice(self.all_characters)
        return password

generator = PasswordGenerator()  
generator._init_()  

while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be a positive integer. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

print("Generated Password:", generator.generate_password(length))
