import random
import string

def generate_password(small, large, digit, special):
    small_letters = string.ascii_lowercase
    large_letters = string.ascii_uppercase
    digits = string.digits
    special_symbols = string.punctuation

    chars = []

    chars.extend(random.choices(small_letters, k=small))
    chars.extend(random.choices(large_letters, k=large))
    chars.extend(random.choices(digits, k=digit))
    chars.extend(random.choices(special_symbols, k=special))

    random.shuffle(chars)
    password = ''.join(chars)

    return password

def main():
    print("Welcome to the Password Generator!")
    

    small = int(input("Enter number of lowercase letters: "))
    large= int(input("Enter number of uppercase letters: "))
    digit = int(input("Enter number of digits: "))
    special = int(input("Enter number of special symbols: "))

    password = generate_password(small, large,digit, special)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
