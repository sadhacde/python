# number guessing game - unconsolidated code
import random
logo = '''
                                        __  .__                                 ___.                ._.
   ____  __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________| |
  / ___\|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \ |
 / /_/  >  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/\|
 \___  /|____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   __
/_____/             \/     \/     \/             \/     \/       \/            \/    \/     \/       \/
'''

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

def easy():
    attempts = 10
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = int(input("Make a guess:"))
        if guess == number:
            return f"You got it! The answer was {number}."
        elif guess < number:
            print("Too low.")
            attempts -= 1
        else:
            print("Too high..")
            attempts -= 1
    if attempts == 0:
        return f"You lost! The number was {number}"

def hard():
    attempts = 5
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = int(input("Make a guess:"))
        if guess == number:
            return f"You got it! The answer was {number}."
        elif guess < number:
            print("Too low.")
            attempts -= 1
        else:
            print("Too high..")
            attempts -= 1
    if attempts == 0:
        return f"You lost! The number was {number}"

number = random.randint(1, 101)
# print(f"For testing purposes, the correct answer is {number}")
mode = input("Choose a difficulty. Type 'easy' or 'hard':").lower()

if mode == "easy":
    print(easy())
elif mode == "hard":
    print(hard())