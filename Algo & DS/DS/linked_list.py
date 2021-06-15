# class Node:
#     """
#     An object for storing of a single node of a linked list
#     Model two attributes - data and the reference to the next node in the list
#     """
#
#     def __init__(self, data=None, nxt=None):
#         self.data = data
#         self.nxt = nxt
#
#     def get_data(self):
#         return self.data
#
#     def get_next(self):
#         return self.nxt
#
#     def add(self, data):
#         new_node = Node(data)
#         # new_node.nxt =
#
#     def __str__(self):
#         return self.data
#
#
# def print_list(node):
#     while node is not None:
#         print(node, end=' ')
#         node = node.nxt
#
#
# def print_backwards(node):
#
#     if node is not None:
#
#         # This is a recursive function where when a node is not None,
#         # the function calls itself on the next item in the linked list.
#         # This is done until it gets to the last node with no next item,
#         # then it starts to print the list from the last item thus
#         # printing the list backwards.
#         print_backwards(node.nxt)
#         print(node, end=' ')
#
#
# node1 = Node('1')
# node2 = Node('2')
# node3 = Node('3')
#
# node1.nxt = node2
# node2.nxt = node3

# print(node1)

# print_backwards(node1)


class Node:
    """
    An object for storing of a single node of a linked list
    Model two attributes - data and the reference to the next node in the list
    """

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f'Node: {self.data}'


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False
        return True

    def size(self):
        count = 0
        current = self.head

        while current:
            current = current.next_node
            count += 1

        return count

    def add(self, data):
        """
        Adds new node containing data at the head of the Linked List

        :param data: the data of the node to be added
        :return: None

        Takes O(1) time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Searches for the first Node containing data that matches the key

        :param key: the data being searched for
        :return: True if found, False if not

        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return False

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            nodes.append(f'{current.data}')
            current = current.next_node
        nodes.append("None")
        return '-->'.join(nodes)


l = LinkedList()

l.add(1)
l.add(2)
l.add(3)

print(l)
n = l.search(3)
print(n)