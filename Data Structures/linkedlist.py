class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

    def get_data(self):
        return self.data

    def get_next(self):
        return self.nxt

    def __str__(self):
        return self.data


def print_list(node):
    while node is not None:
        print(node, end=' ')
        node = node.nxt


def print_backwards(node):

    if node is not None:

        # This is a recursive function where when a node is not None,
        # the function calls itself on the next item in the linked list.
        # This is done until it gets to the last node with no next item,
        # then it starts to print the list from the last item thus
        # printing the list backwards.
        print_backwards(node.nxt)
        print(node, end=' ')


node1 = Node('1')
node2 = Node('2')
node3 = Node('3')

node1.nxt = node2
node2.nxt = node3


# print_backwards(node1)
