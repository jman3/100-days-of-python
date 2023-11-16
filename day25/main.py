import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_data = pd.read_csv("50_states.csv")
answer_dict = answer_data.to_dict()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        answer_list = answer_data.state.to_list()
        missed_state_series = {"state": []}
        for state in answer_list:
            if state not in guessed_states:
                missed_state_series["state"].append(state)

        df = pd.DataFrame(missed_state_series)
        df.to_csv("states_to_learn.csv")
        break

    for answer in answer_dict["state"].values():
        if answer == answer_state and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            x_cor = int(answer_data[answer_data["state"] == answer]["x"])
            y_cor = int(answer_data[answer_data["state"] == answer]["y"])
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            new_turtle.goto(x_cor, y_cor)
            new_turtle.write(answer_state)

