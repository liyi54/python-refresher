import sys


def add_vectors(u, v):
    sum_list = []
    for i in range(len(u)):
        sum_list.append(u[i]+v[i])
    return sum_list


def scalar_mult(s,v):
    scalar = []
    for i in v:
        scalar.append(s*i)
    return scalar


def dot_product(u,v):
    product = []
    total = 0
    for i in range(len(u)):
        product.append(u[i]*v[i])
    for i in product:
        total += i
    return total


def replace(s, old, new ):
    prev = s.split(old)
    return prev.join(new)


def test(did_pass):
    line_num = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else:
        msg = "Test at line {0} FAILED.".format(line_num)
    print(msg)


def test_suite():
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

    test(replace("Mississippi", "i", "I") == "MIssIssIppI")

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") ==
         "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a") ==
         "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

test_suite()