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

game_is_on = True
guessed_states = []

while game_is_on:

    answer_state = turtle.textinput(title=f"{len(guessed_states)}/{len(dict_from_csv)} States Correct", prompt="What's another state's name?").title()

    for st in dict_from_csv:
        if answer_state == st["state"]:
            print(f"it is finded {answer_state}\n"
                  f"cordinates: x:{st["x"]}, y:{st["y"]}")
            state_to_show = SignState(answer_state, st["x"], st["y"])
            state_to_show.write_state()
            guessed_states.append(answer_state)
            print(len(guessed_states))

        # elif answer_state != st["state"]:
        #     print(f"{answer_state} didn't find!")
        # print(st["state"], st["x"], st["y"])

#     print(answer_state)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)


screen.mainloop()


