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


# def draw_poly(t, n, sz):
"""This function allows you to draw
any shape of any size"""
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

