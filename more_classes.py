from classes import Point
from unit_tester import test
import numpy

class Rectangle(Point):
    """A class for manufacturing rectangle objects"""
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "{0}, {1}, {2}".format(self.corner,self.width,self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)

    def flip(self):
        (self.width, self.height) = (self.height, self.width)

    def contains(self, pt):
        boundary1 = numpy.arange(0, self.width, 0.00001)
        boundary2 = numpy.arange(0, self.height, 0.00001)
        return (pt.x in boundary1) and (pt.y in boundary2)




# box = Rectangle(Point(0, 0), 100, 200)
# bomb = Rectangle(Point(100, 80), 5, 10)
# print("box: ", box)
# print("bomb: ", bomb)
# r = Rectangle(Point(0, 0), 100, 200)
# print(r)
# r.grow(25,-10)
# print(r)
# r.move(-10,10)
# print(r)
# s = Rectangle(Point(-10,10), 150, 200)
# print(s.corner.same_coordinates(r.corner))
# t = Rectangle(Point(0, 0), 10, 5)
# test(t.area() == 50)
# test(t.perimeter() == 30)
# t.flip()
# test(t.width == 5 and t.height == 10)
r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))