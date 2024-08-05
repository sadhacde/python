"""
guess the U.S. states game. continues until all states are guessed
unless player types "exit" which then displays list of states that
were not guessed in a csv file, states_to_learn.csv

50_states.csv contains all states with their x, y coordinates 
where the state's name should be displayed upon a correct guess

blank_states_img.gif is the image of the U.S.A map used for gameplay

"""

import pandas as pd
import turtle

FONT = ("Monospace", 10, "bold")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

correct_guesses = []
while len(correct_guesses) < 50:
    guess = screen.textinput(title=f"{len(correct_guesses)}/50 Correct",
                             prompt="What's another state's name?").title()

    if guess.lower() == "exit":  # creates new csv file with states that weren't guessed
        missed_states = [state for state in states if state not in correct_guesses]
        df = pd.DataFrame(missed_states)
        df.to_csv("states_to_learn.csv")
        break

    if guess in states:  # displays state name on map if guess is correct
        if guess not in correct_guesses:  # and has not been guessed already
            state_data = data[data.state == guess]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(guess, font=FONT)
            correct_guesses.append(guess)
            
