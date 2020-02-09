class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def print_list(self):
        while self is not None:
            print(self.cargo, end=' ')
            self.cargo = self.next
        print()

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=", ")


    # def remove_second(self):
    #     if self is None:
    #         return
    #     if self.next is None:
    #         return
    #     # first = self.cargo
    #     self.cargo = self.next
    #     self.cargo = second.next
    #     second.next = None
    #     return second


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
        print('[', end=' ')
        if self.head is not None:
            self.head.print_backward()
        print(']')


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node()
#
# node1.next = node2
# node2.next = node3

# print(node1.remove_second())