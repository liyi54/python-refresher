import turtle


# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# def draw_squares():
"""This function allows draws 5 squares 
 side by side"""
#     square = turtle.Turtle()
#     square.color("hotpink")
#     square.pensize(3)
#
#     for i in range(5):
#         for i in range(4):
#             square.pendown()
#             square.forward(20)
#             square.left(90)
#         square.penup()
#         square.forward(40)
#
#
# draw_squares()
#
# wn.mainloop()

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# dave = turtle.Turtle()
# dave.speed(1)
# dave.color("hotpink")
# dave.pensize(3)
#
# dave.setheading(0)
#
"""This program draws 5 squares
over one another"""
# j = 20
# for i in range(5):
#     for i in range(4):
#         dave.pendown()
#         dave.forward(j)
#         dave.left(90)
#
#     j += 20
#
#     dave.right(90)
#     dave.penup()
#     dave.forward(10)
#     dave.setheading(0)
#     dave.back(10)
#     dave.left(45)
#
#
# wn.mainloop()

#
# def draw_poly(t, n, sz):
#     """This function allows you to draw
#     any shape of any size"""
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     wn.title(t)
#     t = turtle.Turtle()
#     t.color("hotpink")
#     t.pensize(3)
#
#     for i in range(n):
#         t.forward(sz)
#         t.left(360 / n)
#
#     wn.mainloop()
#
#
# tess = "Tess"
# draw_poly(tess, 5, 50)

# def draw_equitriangle():
#     draw_poly("tess",3,100)
#
# draw_equitriangle()


"""This program draws a beautiful spiral
using a combination of squares drawn at different
angles"""

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.color("blue")
# tess.pensize(2)
# tess.speed(10)
#
# tess.setheading(0)
#
# j = 50
#
# for i in range(20):
#     for t in range(4):
#         tess.forward(j)
#         tess.left(90)
#     tess.right(20)
#
# tess.penup()
# wn.mainloop()


"""Drawing square spirals"""

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# julie = turtle.Turtle()
# julie.pencolor("blue")
# julie.speed(10)
#
#
# # angle = 70
#
# julie.right(90)
# julie.forward(5)
# julie.setheading(-180)
#
# julie.forward(10)
# julie.right(90)
# julie.forward(15)
# julie.right(90)
#
# size = 20
#
# for i in range(50):
#     for j in range(2):
#         julie.forward(size)
#         """Changing the angle a little
#         creates another form of spiral"""
#         # julie.right(90)
#         julie.right(89)
#     size += 5
#     # angle += 1
#
#
# wn.mainloop()


# def sum_to(n):
#     total = 0
#     i = 1
#     while i <= n:
#         total += i
#         i += 1
#
#     return total
#
#
# print(sum_to(10))

"""Drawing five stars in a 
particular order"""

wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.pencolor("hotpink")
alex.color("hotpink")
alex.pensize(2)

for j in range(5):
    for i in range(5):    # Drawing a Star with a Turtle
        alex.forward(120)
        alex.right(144)
    alex.penup()
    alex.forward(350)
    alex.right(144)
    alex.pendown()

# alex.hideturtle()
wn.mainloop()

