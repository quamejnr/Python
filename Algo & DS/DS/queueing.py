class Queues:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == 0

    def enqueue(self, entry):
        # New items are inserted
        # into the 0th index thus
        # becoming the first item.
        self.items.insert(0, entry)

    def dequeue(self):
        # Removes first item added
        # to the list
        self.items.pop()

    def __str__(self):
        return f'Queue: {self.items}'


q = Queues()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.dequeue()
print(q)


# Using collections.deque module to implement
# queuing.

from collections import deque

# Initializing deque
d = deque()

# Appending items to queue
d.append('a')
d.append('b')

# Removing items from queue
d.popleft()

print(d)


# Implementation of queue using the queue.Queue module

from queue import Queue

# Initializing a queue
queue = Queue(maxsize=3)

# qsize() give the maxsize of the Queue
print(queue.qsize())

# Adding of element to queue
queue.put('a')
queue.put('b')
queue.put('c')

# Return Boolean for Full Queue
print("\nFull: ", queue.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(queue.get())
print(queue.get())
print(queue.get())

# Return Boolean for Empty
# Queue
print("\nEmpty: ", queue.empty())

queue.put(1)
print("\nEmpty: ", queue.empty())
print("Full: ", queue.full())

# This would result into Infinite Loop as the Queue is empty.
print(queue.get())

