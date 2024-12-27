import turtle
import pandas as pd
from SignState import SignState


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
dict_from_csv = df.to_dict(orient="records")
list_states_from_csv = df.state.to_list()

print(list_states_from_csv)

guessed_states = []

while len(guessed_states) < 50:

    answer_state = turtle.textinput(title=f"{len(guessed_states)}/{len(dict_from_csv)} States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    # for st in dict_from_csv:
    #     if answer_state in st["state"] and answer_state not in guessed_states:
    #         print(f"it is finded {answer_state}\n"
    #               f"cordinates: x:{st["x"]}, y:{st["y"]}")
    #         state_to_show = SignState(answer_state, st["x"], st["y"])
    #         state_to_show.write_state()
    #         guessed_states.append(answer_state)

    for st in list_states_from_csv:
        if answer_state == st and answer_state not in guessed_states:
            state_data = df[df.state == answer_state]
            state_to_show = SignState(answer_state, state_data.x.item(), state_data.y.item())
            # print(state_data.y, state_data.x)
            state_to_show.write_state()
            guessed_states.append(answer_state)

        # elif answer_state != st["state"]:
        #     print(f"{answer_state} didn't find!")
        # print(st["state"], st["x"], st["y"])

#     print(answer_state)

for state in list_states_from_csv:
    for guessed_state in guessed_states:
        if state == guessed_state:
            list_states_from_csv.remove(state)

with open("states_to_learn.csv", "w") as file:
    for state in list_states_from_csv:
        file.write(f"{state}\n")

print(list_states_from_csv, len(list_states_from_csv))


    # states_to_learn =

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)




# screen.mainloop()


