import re

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def total(tree):
    if tree is None:
        return 0
    return total(tree.left) + total(tree.right) + tree.cargo


def print_tree(tree):   # Recursively traverse the tree
    """Generates a prefix expression"""
    if tree is None:
        return
    print(tree.cargo, end=' ')
    print_tree(tree.left)
    print_tree(tree.right)


def post_tree(tree):
    """Generates a postfix expression"""
    if tree is None:
        return
    post_tree(tree.left)
    post_tree(tree.right)
    print(tree.cargo, end=' ')


def in_tree(tree):
    """Generates an infix expression"""
    if tree is None:
        return
    # print("( ")
    in_tree(tree.left)
    print(tree.cargo, end=' ')
    in_tree(tree.right)


def print_indented(tree, level=0):
    if tree is None:
        return
    print_indented(tree.left, level+1)
    print('  ' * level, tree.cargo)
    print_indented(tree.right, level+1)


def tokenize(expr):
    input_list = re.split("([^0-9])", expr)
    token_list = []
    for elem in input_list:
        try:
            if elem == ' ' or elem == '':
                continue
            token_list.append(int(elem))
        except ValueError:
            token_list.append(elem)
    token_list.append('end')
    # print(token_list)
    return token_list


def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False


def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)
        if not get_token(token_list, ')'):
            raise ValueError("Missing closing parenthesis")
        return x
    else:
        x = token_list[0]
        if type(x) != type(0):
            return None
        del token_list[0]
        return Tree(x, None, None)


def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, '*'):
        b = get_product(token_list)
        return Tree('*', a, b)
    return a


def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, '+'):
        b = get_sum(token_list)
        return Tree('+', a, b)
    return a


# tree = Tree(1, Tree(2), Tree(3))

# Evaluating an expression 1 + (2 x 3)
# tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))

# post_tree(tree)

# print_tree(tree)

# in_tree(tree)
# print(total(tree))

# print_indented(tree)

# print(tokenize("(3 + 7) * 9"))
# tokenize("(3 + 7) * 9")


# token_list = [2, "*", 3, "*", 5 , "*", 7, "end"]
# tree = get_product(token_list)
# in_tree(tree)

# tree = get_sum(tokenize('9 * 11 + 5 * 7'))
# tree = get_sum(tokenize('9 * (11 + 5) * 7'))
# post_tree(tree)