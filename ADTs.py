import re  # The regular expression library

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

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
print(eval_postfix("3 2 * 1 +"))


