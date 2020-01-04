import math

class Point:
    """Point class represents and manipulates x,y coords"""

    def __init__(self, x=0, y=0): # The initializer method
        """Create a new point at coordinates x,y """
        self.x = x  # assign attributes to the instance of the class
        self.y = y


    def distance_from_origin(self):
        """Compute my distance from origin"""
        return math.sqrt((self.x**2)+(self.y**2))


    def __str__(self):
        return ("({0}, {1})".format(self.x, self.y))


    def halfway(self,target):
        """return the halfway point between the object and its target"""
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)


    def distance(self,pt2):
        return math.sqrt((self.x - pt2.x) ** 2 + (self.y - pt2.y) ** 2)


    def reflect_x(self):
        return Point(self.x, -self.y)


    def slope_from_origin(self):
        return round(self.y/self.x,1)


    def get_line_to(self,point2):
        m = (point2.y - self.y) / (point2.x - self.x)
        b = self.y - (m * self.x)
        return (m,b)


class SmsStore:

    def __init__(self, has_been_viewed = False, from_number = None, time_arrived = None, text_of_sms = None):
        # self.has_been_viewed = has_been_viewed
        # self.from_number = from_number
        # self.time_arrived = time_arrived
        # self.text_of_sms = text_of_sms
        self.message_store = [(has_been_viewed, from_number, time_arrived, text_of_sms)]

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        has_been_viewed = False
        new_arrival = (has_been_viewed, from_number, time_arrived, text_of_sms)
        self.message_store.append(new_arrival)
        return self.message_store

    def message_count(self):
        total = 0
        for i in self.message_store:
            total += 1
        return total

    def get_unread_indexes(self):
        unread = []
        for i,v in enumerate(self.message_store):
            if v[0] == False:
                unread.append(i)
        return unread


    def get_message(self,index):
        has_been_viewed = True
        message = (has_been_viewed,)
        if index < len(self.message_store):
            result = self.message_store[index]
            result = message+(result[1:])
            return result[1:]
        else:
            return None


    def delete(self,index):
        self.message_store.pop(index)
        return self.message_store

    def clear(self):
        self.message_store.clear()
        return self.message_store


# p = Point(3, 4)
# q = Point(5, 12)
# r = p.halfway(q)
# print(str(p))
# print(Point(3,4).halfway(Point(5,12)))
# print(Point(3,4).distance(Point(5,15)))

# print(Point(3,5).reflect_x())

# print(Point(4, 10).slope_from_origin())
# r = p.distance_from_origin()

# p.x = 4
# p.y = 3

# print(p.x , p.y, q.x, q.y, r)
# print((Point(4, 11).get_line_to(Point(6, 15))))

my_inbox = SmsStore(True,"012347789","11:00am","In a meeting, pls call later")
print(my_inbox.message_store)
print(my_inbox.add_new_arrival("08154329106","10:00pm","Pls call me back"))
# print(my_inbox.message_count())
# print(my_inbox.get_unread_indexes())
print(my_inbox.delete(1))
print(my_inbox.clear())
# print(my_inbox.get_full_message(1))
# print(my_inbox.get_message(2))

