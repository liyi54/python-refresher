import turtle
import time


def exists():
    try:
        # f = open(filename, 'r')
        # f.close()
        # return True
        raise FileNotFoundError
    except FileNotFoundError as err:
        print("File Error: {0}".format(err))
    finally:
        print("I will execute")


# exists()

def divide(x, y):
    try:
        result = x//y
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print("result is "+ str(result))
    finally:
        print("Division completed")


# divide(2,4)


def get_age():
    age = int(input("Please enter your age: "))
    if age < 0:
        # Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age".format(age))
        raise my_error
    return age


def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole.")

# recursion_depth(0)


def show_poly():
    try:
        win = turtle.Screen()   # Grab/create a resource, e.g. a window
        tess = turtle.Turtle()

        # This dialog could be cancelled,
        #   or the conversion to int might fail, or n might be zero.
        n = int(input("How many sides do you want in your polygon?"))
        angle = 360 / n
        for i in range(n):      # Draw the polygon
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)           # Make program wait a few seconds
    finally:
        win.bye()               # Close the turtle's window

# show_poly()


def readposint():
    try:
        value = int(input("Input a positive integer: "))
        if value < 0:
            raise ValueError
    except ValueError:
        print("Wrong value inputed: {0}".format(ValueError))

readposint()