import turtle
import pandas as pd
import os
from SignState import SignState


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


df = pd.read_csv("50_states.csv")
all_states_from_csv_list = df.state.to_list()


def load_states():
    all_states_from_csv_list = df.state.to_list()
    print(all_states_from_csv_list, len(all_states_from_csv_list))


load_states()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/{len(all_states_from_csv_list)} States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state == "Load":
        try:
            dfs = pd.read_csv("states_to_learn.csv")
            print(dfs, "\n loaded")
            all_states_from_csv_list = dfs.state.to_list()
        except FileNotFoundError:
            print("states_to_learn.csv not found")
            load_states()
            print("states_to_learn.csv reloaded")
            all_states_from_csv_list = df.state.to_list()

    if answer_state == "Clear":
        os.remove("states_to_learn.csv")
        print("states_to_learn.csv deleted")
        screen.reset()



    for st in all_states_from_csv_list:
        if answer_state == st and answer_state not in guessed_states:
            state_data = df[df.state == answer_state]
            state_to_show = SignState(answer_state, state_data.x.item(), state_data.y.item())
            # print(state_data.y, state_data.x)
            state_to_show.write_state()
            guessed_states.append(answer_state)


for state in all_states_from_csv_list:
    for guessed_state in guessed_states:
        if state == guessed_state:
            all_states_from_csv_list.remove(state)

# create a pandas DataFrame from the list
df = pd.DataFrame(all_states_from_csv_list, columns=['state'])
# save the DataFrame to a CSV file
df.to_csv('states_to_learn.csv', index=False)

print(all_states_from_csv_list, len(all_states_from_csv_list))




