import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
n_letters= int(input("How many letters would you like in your password?\n")) 
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))

length = n_letters + n_symbols + n_numbers

password = ""
for n in range(0, length + 1):
    if n <= n_letters - 1:
        password += random.choice(letters)
    elif n <= (n_letters + n_symbols - 1):
        password += random.choice(symbols)
    elif n <= (n_letters + n_symbols + n_numbers - 1):
        password += random.choice(numbers)

pwd = list(password)
random.shuffle(pwd)

password = ""
for p in pwd:
    password += p

print("Your password is", password)