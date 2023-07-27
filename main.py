import turtle
import pandas

screen = turtle.Screen()
turtle.setup(725, 491, startx=0, starty=0)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()

x_cor = 0
y_cor = 0
guessed_states = []

new_turtle = turtle.Turtle()
new_turtle.hideturtle()
new_turtle.penup()
game_is_on = True
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()
    if answer == "Exit":
        break
    if answer in list_of_states:
        guessed_states.append(answer)

    row_of_state = data[data.state == answer]
    new_turtle.goto(int(row_of_state.x), int(row_of_state.y))

    new_turtle.write(answer)
    list_of_states.remove(answer)

dict_list_of_states = {
    "state": list_of_states
}
states_to_learn = pandas.DataFrame(dict_list_of_states)
states_to_learn.to_csv("states_to_learn.csv")
