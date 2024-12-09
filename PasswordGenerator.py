import random
import string
import re

class PasswordGenerator:
    def __init__(self, length=12, use_digits=True, use_special=True, use_upper=True, use_lower=True):
        self.length = length
        self.use_digits = use_digits
        self.use_special = use_special
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.characters = ''
        self.password = ''
        self.validate_settings()

    def validate_settings(self):
        if not (self.use_digits or self.use_special or self.use_upper or self.use_lower):
            raise ValueError("At least one character type must be enabled.")

    def generate_characters(self):
        if self.use_digits:
            self.characters += string.digits
        if self.use_special:
            self.characters += string.punctuation
        if self.use_upper:
            self.characters += string.ascii_uppercase
        if self.use_lower:
            self.characters += string.ascii_lowercase

    def generate_password(self):
        self.generate_characters()
        self.password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return self.password

    def check_strength(self):
        strength = "Weak"
        if len(self.password) >= 12 and re.search(r'[A-Z]', self.password) and re.search(r'[a-z]', self.password) and re.search(r'\d', self.password) and re.search(r'[^\w\s]', self.password):
            strength = "Strong"
        elif len(self.password) >= 8:
            strength = "Moderate"
        return strength

    def display_password_info(self):
        print(f"Generated Password: {self.password}")
        print(f"Password Strength: {self.check_strength()}")
    
def main():
    try:
        print("Welcome to the Password Generator!\n")
        length = int(input("Enter desired password length: "))
        use_digits = input("Include digits (y/n)? ").lower() == 'y'
        use_special = input("Include special characters (y/n)? ").lower() == 'y'
        use_upper = input("Include uppercase letters (y/n)? ").lower() == 'y'
        use_lower = input("Include lowercase letters (y/n)? ").lower() == 'y'

        generator = PasswordGenerator(length, use_digits, use_special, use_upper, use_lower)
        password = generator.generate_password()
        generator.display_password_info()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
