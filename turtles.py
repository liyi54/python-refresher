import turtle  # We import the turtle module

bg_color_value = input("Input Background color: ")
aliya_color_value = input("Input Aliya's color: ")
dave_color_value = input("Input Dave's color: ")
aliya_width = int(input("Input Aliya's width: "))
dave_width = int(input("Input Dave's width: "))

window = turtle.Screen()  # Creates a screen for turtles
window.bgcolor(bg_color_value)
window.title("Aliya and Dave")

dave = turtle.Turtle()  # Create a turtle, assign to Dave
dave.color(dave_color_value)

aliya = turtle.Turtle()
aliya.color(aliya_color_value)  # aliya.pencolor("red")
aliya.pensize(aliya_width)


def move_aliya_fuct(x):
    if x <= 3:
        aliya.forward(80)
        aliya.left(120)


move_dave = 0  # Creates a variable to define number of movements to be made
move_aliya = 1

while move_dave < 4:
    dave.forward(50)
    dave.left(90)
    move_aliya_fuct(move_aliya)
    move_dave += 1
    move_aliya += 1

window.mainloop()
