from dataclasses import dataclass

@dataclass
class Node:
    """
    A data type that stores data and a reference to the next node
    """
    data: int
    nxt: int = None


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False
        return True

    @property
    def length(self):
        current_node = self.head
        count = 0

        while current_node:
            count += 1
            current_node = current_node.nxt

        return count

    def search(self, element):
        """
        Prints position of an element if found in a Linked List
        :param element: element being searched for
        :return: None
        """
        current_node = self.head
        position = 0

        while current_node:
            if current_node.data == element:
                print(f'Node found in position: {position}')
                return
            current_node = current_node.nxt
            position += 1
        print('Node not found')


    def insert_at_head(self, data):
        """
        inserts node at head
        :param data: data
        :return: None
        """
        node = Node(data, self.head)
        self.head = node
        return

    def insert_at_tail(self, data):
        """
        inserts node at the end
        :param data: data
        :return: None
        """
        node = Node(data)
        current_node = self.head
        previous_node = None

        if current_node is None:
            self.head = node
            return

        while current_node:
            previous_node = current_node
            current_node = current_node.nxt

        previous_node.nxt = node
        node.nxt = None

    def append_values(self, data_list):
        """
        Inserts multiple data to the end of linked list
        :param data_list: list
        :return: None
        """
        for data in data_list:
            self.insert_at_tail(data)
        # self.insert_at_tail(None)

    def insert_at(self, position, data):
        """
        inserts node at a position
        :param position: position
        :param data: data
        :return: None
        """
        if position < 0 or position > self.length:
            raise Exception("Invalid Index")

        if position == 0:
            self.insert_at_head(data)
            return

        node = Node(data)
        current_node = self.head
        previous_node = None

        for _ in range(position):
            previous_node = current_node
            current_node = current_node.nxt

        next_node = current_node
        previous_node.nxt = node
        node.nxt = next_node

    def remove_at(self, position):
        """
        Removes element at a position
        :param position: position
        :return: None
        """

        if position < 0 or position >= self.length:
            raise Exception("Invalid Index")

        if position == 0:
            self.head = self.head.nxt
            return

        current_node = self.head
        previous_node = None
        for _ in range(position):
            previous_node = current_node
            current_node = current_node.nxt

        next_node = current_node.nxt
        previous_node.nxt = next_node
        return

    def reverse(self):
        """ Reverse a linked list """
        current_node = self.head
        previous_node = None

        while current_node:
            current_node.nxt, previous_node, current_node = previous_node, current_node, current_node.nxt

        self.head = previous_node
        return

    def reverse_rec(self, head):
        current_node = head
        # print(current_node.data)
        if current_node is None:
            return current_node
        if current_node.nxt is None:
            current_node = self.head
            return current_node
        else:
            next_node = current_node.nxt
            # previous_node = current_node
            self.reverse_rec(current_node.nxt)

            next_node.nxt = current_node

            print(current_node.data, next_node.data, )
            # print(current_node.data)
        current_node.nxt = None
        return
    # TODO: Still not working

    def print_forwards(self):
        current_node = self.head

        if current_node is None:
            print('Linked List is empty')
            return

        while current_node:
            print(current_node.data, end=' --> ')
            current_node = current_node.nxt
        print('None')

    def print_forwards_rec(self, head):
        """
        print the linked list forwards using recursion
        :param head: head of the linked list
        :return: None
        """
        if head:
            print(head.data, end=" --> ")
            self.print_forwards_rec(head.nxt)
            return
        print("None")

    def print_backwards(self, head):
        """
        prints a linked list backwards using recursion
        :param head: the head of a linked list
        :return: None
        """
        if head:
            self.print_backwards(head.nxt)
            print(head.data, end=' --> ')
        return

    def __repr__(self):
        nodes = []
        current_node = self.head

        while current_node:
            nodes.append(f'{current_node.data}')
            current_node = current_node.nxt
        nodes.append('None')
        return ' --> '.join(nodes)


if __name__ == '__main__':
    ll = LinkedList()

    ll.append_values([3, 4, 5, 6, 19, 8])
    ll.search(5)
    # # ll.print_forwards()
    # ll.reverse()
    # ll.print_forwards()
    # # ll.print_backwards(ll.head)




