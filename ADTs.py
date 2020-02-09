import re  # The regular expression library
from linked_lists import Node


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            self.head = node  # If the queue is empty, the new node goes first
        else:
            last = self.head
            while last.next:
                last = last.next  # Find the last node in the queue
            last.next = node  # Add the new node to the end of the queue
        self.length += 1

    def remove(self):
        cargo = self.head.cargo  # The first node in the queue
        self.head = self.head.next  # Remove the first node and make the next on the queue the first node
        self.length -= 1
        return cargo  # Return the removed node


class ImprovedQueue:
    def __init__(self):
        self.head = None
        self.length = 0
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node  # Add the node to the end of the queue
            self.last = node  # Identify the last node as the last node in the queue
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo


class AlternateQueue:
    def __init__(self):
        self.items = []

    def __str__(self):
        s = '[ '
        c = ', '
        t = ' ]'
        for i in self.items:
            s = s + i + c
        return "{0}".format(s + t)

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        first = self.items[0]
        del self.items[0]
        return first


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:  # Find the item with the highest priority using size
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]  # Remove the item with the highest priority on the queue
        return item


class ImprovedPriority:
    def __init__(self):
        self.head = None

    def insert(self, cargo):
        first = self.head
        if first is None:
            node = Node(cargo)
            self.head = node
            return

        if first.cargo < cargo:
            node = Node(cargo)
            node.next = first
            self.head = node
            return

        while first.next is not None:
            if first.next.cargo < cargo:
                break
            first = first.next
        node = Node(cargo)
        node.next = first.next
        first.next = node
        return

    def remove(self):
        top = self.head
        self.head = self.head.next
        return top

    def is_empty(self):
        return self.head is None


class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{0:16} : {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score  # Less is more in Golfing


# s = Stack()
# s.push(22)
# s.push(15)
# s.push('Table')
# # print(s.items)
# # s.pop()
# # print(s.items)
#
# while not s.is_empty():
#     print(s.pop(),end = " ")


def eval_postfix(expr):
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    for token in token_list:
        if token == '' or token == ' ':
            continue
        elif token == '+':
            sum = int(stack.pop()) + int(stack.pop())
            stack.push(sum)
        elif token == "*":
            prod = int(stack.pop()) * int(stack.pop())
            stack.push(prod)
        else:
            stack.push(token)
    return stack.pop()


# print(eval_postfix("56 47 + 2 *"))
# print(eval_postfix("1 2 + 3 *"))
# print(eval_postfix("3 2 * 1 +"))

# q = PriorityQueue()

#
# for num in [11,10,15,9,18,25]:
#     q.insert(num)
#
# while not q.is_empty():
#     print(q.remove())

# tiger = Golfer("Tiger Woods", 61)
# rory = Golfer("Rory Mcilroy",72)
# phil = Golfer("Phil Mickelson",52)
#
# for g in [rory, phil, tiger]:
#     q.insert(g)
#
# while not q.is_empty():
#     print(q.remove())    # Print the golfers in order of their ranks


# aq = AlternateQueue()
# aq.insert("Bayo")
# aq.insert('Femi')
# aq.insert("Kunle")
#
# aq.remove()
#
# print(aq)

ip = ImprovedPriority()

for g in [3, 1, 2, 4, 7, 5]:
    ip.insert(g)

while not ip.is_empty():
    print(ip.remove())
