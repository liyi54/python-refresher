import unit_tester as ut
import os
# import turtle
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# wn.bgcolor('lightgreen')
# t.pencolor('blue')


# def koch(t, order, size):
#     if order == 0:
#         t.forward(size)
#     else:
#         for angle in [60, -120, 60, 0]:
#            koch(t, order-1, size/3)
#            t.left(angle)

# def koch(t, order, size):
#     """
#        Make turtle t draw a Koch fractal of 'order' and 'size'.
#        Leave the turtle facing the same direction.
#     """
# 
#     if order == 0:          # The base case is just a straight line
#         t.forward(size)
#     else:
#         koch(t, order-1, size/3)   # Go 1/3 of the way
#         t.left(60)
#         koch(t, order-1, size/3)
#         t.right(120)
#         koch(t, order-1, size/3)
#         t.left(60)
#         koch(t, order-1, size/3)
# 
# koch(t, 3, 100)
# wn.mainloop()

def r_sum(nested_list):
    total = 0
    for i in nested_list:
        if type(i) == list:
            total += r_sum(i)
        else:
            total += i
    return total


def r_max(nested_list):
    """
        Find the maximum in a recursive structure of lists
          within other lists.
          Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nested_list:
        if type(e) == list:
            val = r_max(e)
        else:
            val = e

        if first_time:
            largest = val
            first_time = False
        elif val > largest:
            largest = val
    return largest


def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)                    # Print the line
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_files(fullname, prefix + "| ")


def recursive_min(xs):
    smallest = None
    first_time = True
    for elem in xs:
        if type(elem) == list:
            val = recursive_min(elem)
        else:
            val = elem

        if first_time:
            smallest = val
            first_time = False
        else:
            if val < smallest:
                smallest = val
    return smallest


new_list = []


def flatten(nested):
    for elem in nested:
        if type(elem) == list:
            flatten(elem)
        else:
            global new_list
            new_list.append(elem)
    return new_list


tally = 0


def count(value, target):
    for elem in target:
        if type(elem) == list:
            # again = True
            val = count(value, elem)
        else:
            val = elem

        if val == value:
            global tally
            tally += 1

    return tally


def fib(fib_len):
    start = 0
    next = 1
    i = 0
    if fib_len <= 1:
        return 1
    else:
        while i < fib_len:
            val = start + next
            start = next
            next = val
            i += 1
        return val


def print_path(path):
    """Print out path of all the files
    in the directory"""
    dirlist = get_dirlist(path)
    for f in dirlist:                  # Print the line
        fullname = os.path.join(path, f)  # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_path(fullname)
        else:
            print(fullname)


# print_files("/Users/sadeliyi/Documents")


# ut.test(r_max([2, 13, [1, 9], 8, 6]) == 13)
# ut.test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
# ut.test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
# ut.test(r_max(["joe", ["sam", "ben"]]) == "sam")

# ut.test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
# ut.test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
# ut.test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
# ut.test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

# ut.test(count(2, []) == 0)
# ut.test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
# ut.test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
# ut.test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
# ut.test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
# ut.test(count("a",
#      [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)
#
# ut.test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
# ut.test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
# ut.test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
# ut.test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
#               ["this","a","thing","a","is","a","easy"])
# ut.test(flatten([]) == [])

# print(fib(200))

print_path('/Users/sadeliyi/Documents/Data Science')