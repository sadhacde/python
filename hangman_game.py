import random
import hangman

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"
# print(f"{' '.join(display)}") comment for hard mode

guesses = []

while not end_of_game:
    guess = input("Guess a letter:").lower()
    if guess in guesses:
        print(f"You have already guessed the letter {guess}")
        continue
    guesses += guess
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose. The word was", chosen_word)
            
    print(stages[lives])
    
    if "_" not in display:
        end_of_game = True
        print("You win!")