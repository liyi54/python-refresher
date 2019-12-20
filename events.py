# import turtle
#
# turtle.setup(400,500)                # Determine the window size
# wn = turtle.Screen()                 # Get a reference to the window
# wn.title("Handling keypresses!")     # Change the window title
# wn.bgcolor("lightgreen")             # Set the background color
# tess = turtle.Turtle()               # Create our favorite turtle
# size = 1
#
# #The next four functions are our "event handlers".
# def h1():
#    tess.forward(30)
#    # wn.ontimer(h1,1000)
#
# def h2():
#    tess.left(45)
#
# def h3():
#    tess.right(45)
#
# def h4():
#     wn.bye() # Close down the turtle window
#
# def h5():
#     tess.pencolor('red')
#     tess.color('red')
#
# def h6():
#     tess.pencolor('green')
#     tess.color('green')
#
# def h7():
#     tess.pencolor('blue')
#     tess.color('blue')
#
# def h8():
#     global size
#     size += 1
#     if size > 20:
#         size = 20
#     tess.pensize(size)
#
# def h9():
#     global size
#     size -= 1
#     if size < 1:
#         size = 1
#     tess.pensize(size)
#
# #These lines "wire up" keypresses to the handlers we've defined.
# wn.onkey(h1, "Up")
# wn.onkey(h2, "Left")
# wn.onkey(h3, "Right")
# wn.onkey(h4, "q")
# wn.onkey(h5, "r")
# wn.onkey(h6, "g")
# wn.onkey(h7, "b")
# wn.onkey(h8, "+")
# wn.onkey(h9, "-")
#
#
# #Now we need to tell the window to start listening for events,
# #If any of the keys that we're monitoring is pressed, its
# #handler will be called.
# # wn.ontimer(h1,6000)
# wn.listen()
# wn.mainloop()



# turtle.setup(400,500)
# wn = turtle.Screen()
# wn.title("How to handle mouse clicks on the window!")
# wn.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("purple")
# alex = turtle.Turtle()
# alex.color("hotpink")
# tess.pensize(3)
# alex.pensize(3)
# tess.shape("circle")
# alex.shape("circle")
#
#
# def control_alex(x, y):
#     wn.title("Got alex click at coords {0}, {1}".format(x, y))
#     alex.left(45)
#     alex.forward(50)
#     # alex.goto(x, y)
#
#
# def control_tess(x, y):
#     wn.title("Got tess click at coords {0}, {1}".format(x, y))
#     tess.right(45)
#     tess.forward(50)
#     # wn.onclick(tess.goto(x, y))
#
#
# def close():
#     wn.bye()
#
#
# alex.onclick(control_alex)
# tess.onclick(control_tess)
# wn.onkey(close,"q")
# # Wire up a click on the window.
# wn.listen()
# wn.mainloop()

import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()
alex.hideturtle()
rob = turtle.Turtle()
rob.hideturtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.hideturtle()
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("grey")
tess.showturtle()


# Position alex onto the place where the orange light should be
alex.penup()
alex.forward(40)
alex.left(90)
alex.forward(120)
# Turn tess into a big green circle
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("grey")
alex.showturtle()

rob.penup()
# Position rob onto the place where the red light should be
rob.forward(40)
rob.left(90)
rob.forward(190)
# Turn rob into a big green circle
rob.shape("circle")
rob.shapesize(3)
rob.fillcolor("grey")
rob.showturtle()




# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    """ This function alternates the traffic lights
    on/off switch by changing the fill color of each turtle"""

    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        # tess.forward(70)
        # tess.fillcolor("orange")
        # rob.hideturtle()
        tess.fillcolor("grey")
        rob.fillcolor("red")
        state_num = 1
        wn.ontimer(advance_state_machine, 60000)
    elif state_num == 1:     # Transition from state 1 to state 2
        # tess.forward(70)
        # tess.fillcolor("red")
        # tess.hideturtle()
        # alex.showturtle()
        rob.fillcolor("grey")
        alex.fillcolor("orange")
        state_num = 2
        wn.ontimer(advance_state_machine, 3000)
    else:                    # Transition from state 2 to state 0
        # tess.back(140)
        # tess.fillcolor("green")
        # alex.hideturtle()
        # rob.showturtle()
        alex.fillcolor("grey")
        tess.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine, 60000)
# Bind the event handler to the space key.

advance_state_machine()

# wn.listen()                      # Listen for events
wn.mainloop()