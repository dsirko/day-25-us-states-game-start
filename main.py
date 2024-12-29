import turtle
import pandas as pd
from SignState import SignState


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

try:
    list1 = pd.read_csv("50_states.csv")
    list2 = pd.read_csv("states_to_learn.csv")
    merged_list = pd.merge(list1, list2, on='state', how='left')
    print(merged_list)

except FileNotFoundError:
    df = pd.read_csv("50_states.csv")
    list_states_from_csv = df.state.to_list()
    print(list_states_from_csv)


guessed_states = []

def not_guessed_states():
    missing_items = [item for item in list_states_from_csv if item not in guessed_states]
    print(missing_items, len(missing_items))


while len(guessed_states) < 50:

    answer_state = turtle.textinput(title=f"{len(guessed_states)}/{len(list_states_from_csv)} States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    for st in list_states_from_csv:
        if answer_state == st and answer_state not in guessed_states:
            state_data = df[df.state == answer_state]
            state_to_show = SignState(answer_state, state_data.x.item(), state_data.y.item())
            state_to_show.write_state()
            guessed_states.append(answer_state)

for state in list_states_from_csv:
    for guessed_state in guessed_states:
        if state == guessed_state:
            list_states_from_csv.remove(state)


# create a pandas DataFrame from the list
df = pd.DataFrame(list_states_from_csv, columns=['state'])

# save the DataFrame to a CSV file
df.to_csv('states_to_learn.csv', index=False)

not_guessed_states()



