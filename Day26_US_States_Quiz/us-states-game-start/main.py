import turtle
import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
correct_guesses = []
maps = pandas.read_csv("50_states.csv")

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the State", prompt = "Whats another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break
    if maps["state"].str.contains(answer_state).any():
        # print("Present")
        writer.goto(int(maps[maps["state"] == answer_state]["x"]), int(maps[maps["state"] == answer_state]["y"]))
        writer.write(answer_state)
        if answer_state not in correct_guesses:
            correct_guesses.append(answer_state)

states_to_learn = list(set(maps["state"].tolist()) - set(correct_guesses))
new_data = pd.DataFrame(states_to_learn)
new_data.to_csv("States_to_learn.csv")
# turtle.mainloop()
#screen.exitonclick()