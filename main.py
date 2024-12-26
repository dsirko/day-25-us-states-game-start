import turtle
# import csv
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
dict_from_csv = df.to_dict(orient="records")



# with open("50_states.csv", "r") as states:
#     reader = csv.DictReader(states)
#     dict_from_csv = [row for row in reader]
#
# print(dict_from_csv)
# print(dict_from_csv[49]["state"])

game_is_on = True

while game_is_on:

    answer_state = turtle.textinput(title="Guess the State", prompt="What's another state's name?").title()

    for st in dict_from_csv:
        if answer_state == st["state"]:
            print(f"it is finded {answer_state}\n"
                  f"cordinates: x:{st["x"]}, y:{st["y"]}")
        # elif answer_state != st["state"]:
        #     print(f"{answer_state} didn't find!")
        # print(st["state"], st["x"], st["y"])


#     print(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)



screen.mainloop()


