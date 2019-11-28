import turtle
import math


# """Testing the begin_fill() and end_fill() methods"""
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")


# alex = turtle.Turtle()
# alex.pencolor("hotpink")
# alex.color("hotpink", "blue")

# alex.begin_fill()
#
# for i in range(2):
#     alex.forward(100)
#     alex.left(120)
#
# alex.end_fill()
# alex.write("Hello")
#
# alex.speed(1)


# xs = [-48, -117, 200, 240, 160, 260, 220]
#
# tess = turtle.Turtle()
# tess.color("blue")
# tess.pensize(3)
#
# def draw_bar(t, height):
#     """ Get turtle t to draw one bar, of height. """
#     if height < 100:
#         t.fillcolor("green")
#     elif height < 200:
#         t.fillcolor("yellow")
#     else:
#         t.fillcolor("red")
#
#     t.setheading(0)
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)     # Draw up the left side
#     t.right(90)
#     if height < 0:
#         t.right(90)
#         t.penup()
#         t.forward(12)
#         t.left(90)
#         t.write("    " + str(height))
#         t.left(90)
#         t.forward(12)
#         t.setheading(0)
#         t.pendown()
#     else:
#         t.write("     " + str(height))
#     t.forward(40)         # Width of bar, along the top
#     # t.write(height)
#     t.right(90)
#     t.forward(height)     # And down again!
#     t.left(90)            # Put the turtle facing the way we found it.
#     t.penup()
#     t.forward(10)         # Leave small gap after each bar
#     t.pendown()
#     t.end_fill()
#
#
# for v in xs:  # Assume xs and tess are ready
#     draw_bar(tess, v)
#
# wn.mainloop()


# def counter_lap(duration, start_date):
#     """This function converts the duration of the stay
#     to the day number"""
#     j = start_date
#     for i in range(duration):
#         j += 1
#         if j > 6:
#             j = 0
#     day_of_the_week(j)
#
#
# def day_of_the_week(day_number):
#     """This function receives the day number from the counter_lap function
#     and returns the day of return"""
#     days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     print("You will return on", days[day_number])
#
#
# start = int(input("Enter the start day of your holiday: "))
# sleeps = int(input("What is the duration of your stay?: "))
#
# counter_lap(sleeps, start)


# def get_grade(mark):
#     """This function is given an exam mark, and it returns a string — the grade for that mark"""
#
#     if mark < 40:
#         print("F3")
#     elif mark < 45:
#         print("F2")
#     elif mark < 50:
#         print("F1 Supp")
#     elif mark < 60:
#         print("Third")
#     elif mark < 70:
#         print("Second")
#     elif mark < 75:
#         print("Upper second")
#     else:
#         print("First")
#
# xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
#                      49.9, 45, 44.9, 40, 39.9, 2, 0]
# for i in xs:
#     get_grade(i)


# def find_hypot(opp, adj):
#     """This function calculates the hypotenuse length of a right angled
#     triangle given the length of two sides"""
#     hypot_squared = opp**2 + adj**2
#     hypot = math.sqrt(hypot_squared)
#     print(str(hypot))
#
#
# opposite = float(input("Enter opposite value: "))
# adjacent = float(input("Enter adjacent value: "))
#
# find_hypot(opposite, adjacent)


def is_right_angled(a, b, c):
    """This function allows us to determine if a triangle is right-angled
    irrespective of the order in which the arguments are passes"""
    sides = [a,b,c]
    oppAdj = []
    for i in sides:
        if i == max(sides):
            hypot = i
        else:
            oppAdj.append(i)
    if oppAdj[0] ** 2 + oppAdj[1] ** 2 != hypot ** 2:
        print("This isn't a right angled triangle")
    else:
        print("This is a right angled triangle")


opposite = int(input("Enter opposite value: "))
adjacent = int(input("Enter adjacent value: "))
hypotenuse = int(input("Enter the hypotenuse value"))

is_right_angled(opposite, hypotenuse, adjacent)

# a = math.sqrt(2.0)
# print(a, a * a)
# print(a * a == 2.0)
