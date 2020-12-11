class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def all_items(self):
        return self.items


def get_reverse(item):

    rev = {
        '[': ']',
        ']': '[',
        '}': '{',
        '{': '}',
        ')': '(',
        '(': ')',
    }

    return rev[item]


left_bracket = ['[', '{', '(']

b_list = ['[', ']', '(', ')']

s = Stack()


def stacking(stack, sequence):
    for bracket in sequence:

        # This finds the reverse of the bracket.
        reverse = get_reverse(bracket)

        # Checks if the bracket is a left bracket,
        # then adds to stack if it is.
        if bracket in left_bracket:
            stack.push(bracket)

        # If the bracket is not a left bracket,
        # it checks if the stack is empty or
        # if the last item in the stack is not the reverse of the current bracket.
        # If none of them is true then the sequence is invalid.
        elif stack.is_empty() or stack.pop() != reverse:
            return False

    # If after all the checks the stack is empty,
    # then the sequence is valid
    return stack.is_empty()


# print(stacking(s, b_list))





