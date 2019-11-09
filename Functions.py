# import turtle
#
# __import__("turtle").__traceable__ = False
#
#
# # def draw_square(name, size):
# """This function draws a simple square of a given size"""
# #     for i in range(4):
# #         name.forward(size)
# #         name.left(90)
#
#
# def draw_mult_square(name, size):
#
#     """Make turtle name draw a multi-colored square of size"""
#
#     for i in ["red", "blue", "orange", "hotpink"]:
#         name.color(i)
#         name.forward(size)
#         name.left(90)
#
#
# name = input("What is the name of your Turtle?: ")
#
# size = int(input("What is the size of your square?: "))
#
# wn = turtle.Screen()
# wn.title(name+" meets a function")
# wn.bgcolor("lightgreen")
#
# name = turtle.Turtle()
# name.pensize(3)
#
# for j in range(15):
#     draw_mult_square(name, size)
#     size += 10
#     name.forward(10)
#     name.right(18)
#
# wn.mainloop()
#
# # name.color("blue")
# #
# # draw_square(name, size)
#
# wn.mainloop()

import turtle

# def compound_interest(p,r,n,t):
#     """This function calculates compound interest"""
#     answer = p*((1+r/n)**(n*t))
#     return answer
#
#
# rate = 0.15
# times = 1
# toInvest = float(input("How much do you want to invest?: "))
# years = int(input("For how many years do you want to invest your money?: "))
#
# result = compound_interest(toInvest, rate, times, years)
#
# print("After ", str(years), " years, you will have ", str(round(result,2)), " Naira" )


def make_window(color, title):
    wn = turtle.Screen()
    wn.bgcolor(color)
    wn.title(title)
    # wn.mainloop()
    return wn


def make_turtle(size, color, speed):
    newTurtle = turtle.Turtle()
    newTurtle.color(color)
    newTurtle.shape("turtle")
    newTurtle.pensize(int(size))
    newTurtle.speed(speed)
    newTurtle.forward(100)
    return newTurtle


make_window("lightgreen","New Turtle")
alex = make_turtle(5,"blue",1)
# alex.forward(100)
#
# def make_window(colr, ttle):
#     """
#       Set up the window with the given background color and title.
#       Returns the new window.
#     """
#     w = turtle.Screen()
#     w.bgcolor(colr)
#     w.title(ttle)
#     # w.mainloop()
#     return w
#
#
# def make_turtle(colr, sz):
#     """
#       Set up a turtle with the given color and pensize.
#       Returns the new turtle.
#     """
#     t = turtle.Turtle()
#     t.color(colr)
#     t.pensize(sz)
#     return t
#
#
# wn = make_window("lightgreen", "Tess and Alex dancing")
# tess = make_turtle("hotpink", 5)
# tess.forward(10)
# alex = make_turtle("black", 1)
# dave = make_turtle("yellow", 2)