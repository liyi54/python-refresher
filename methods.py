import turtle

tess = turtle.Turtle()
wn = turtle.Screen()
wn.title("Method Turtles")

tess.shape("turtle")
tess.speed(5)

tess.pencolor("blue")
wn.bgcolor("lightgreen")

size = 15
tess.penup()

for j in range(30):
    tess.stamp()
    size += 3
    tess.forward(size)
    tess.right(15)

tess.pendown()
tess.pencolor("red")  # the real tess

wn.mainloop()