# for i in range(1000):   #Basic for loop
#     print("We like Python's turtles!")

# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]  #for loop with square
# for i in xs:
#     square = i ** 2
#     print(str(i), str(square))

# total = 0     # Rolling sum
# for i in xs:
#     total += i
#     i += 1
# print(str(total))

# product = 1   # Rolling product
# for i in xs:
#     product *= i
#     i += 1
# print(str(product))

import turtle

alex = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex.shape("turtle")
alex.speed(2)

alex.color("blue")

# for i in range(3):  # Drawing an equilateral triangle with a Turtle
#     alex.forward(100)
#     alex.left(120)

# for i in range(4):  # Drawing a square with a Turtle
#     alex.forward(100)
#     alex.left(90)

# for i in range(6):  # Drawing a hexagon with a Turtle
#     alex.left(60)
#     alex.forward(100)

# for i in range(8):  # Drawing an octagon with a Turtle
# #     alex.left(45)
# #     alex.forward(100)
# #
# # wn.mainloop()

# import turtle
#
# pirate = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# pirate.shape("turtle")
# pirate.pencolor("blue")
#
# pirate.speed(2)
# pirate.setheading(0)
#
# steps = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# x = 100
# i = 0
#
# while i < len(steps):
#     pirate.forward(x)
#     pirate.left(steps[i])
#     i += 1
#
# print(pirate.heading())

# wn.mainloop()

#
# for i in range(18):  # Drawing a shape of 18 sides with a Turtle
#     alex.left(20)
#     alex.forward(100)
#
# wn.mainloop()

# for i in range(5):    # Drawing a Star with a Turtle
#     alex.forward(120)
#     alex.right(144)
#
# alex.hideturtle()
# wn.mainloop()
#
# alex.stamp()
# alex.penup()
# alex.pensize(3)
#
# angle = 0
# count = 0
#
# while count < 12:   # Drawing a clock with a turtle
#     alex.right(angle)
#     alex.forward(80)
#     alex.pendown()
#     alex.forward(20)
#     alex.penup()
#     alex.forward(20)
#     alex.stamp()
#     alex.back(120)
#     alex.setheading(0)
#     angle += 30
#     count += 1
#
# alex.hideturtle()
#
# for i in range(11):
#     alex.forward(80)
#     alex.stamp()
#     alex.left(30)

wn.mainloop()