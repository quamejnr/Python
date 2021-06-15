import heapq

# Implementation of heap data structure
# using heapq module.
# The default heap invariant is min heap

heap = [8, 2, 3, 4, 5, 6]

# Converting list into heap.
heapq.heapify(heap)
print(heap)


# Pushing element into heap with heappush.
heapq.heappush(heap, 10)
print(heap)


# Removing the smallest element in heap using heappop.
heapq.heappop(heap)
print(heap)


# Using heapreplace makes it easier to pop
# and push an element into heap.
# Heapreplace removes the smallest element
# and pushes another element into heap.
heapq.heapreplace(heap, 12)
print(heap)


# Using heappushpop is similar to heapreplace.
# The only difference is heapreplace returns
# the smallest item in the heap that was popped
# while heappushpop returns the smallest item in the heap
# after popping and pushing
heapq.heappushpop(heap, 5)


# nlargest returns the k largest numbers in a heap
# where k is the key: the number of numbers to be returned.
print(heapq.nlargest(3, heap))


# nsmallest does the opposite of nlargest,
# returns the k smallest numbers.
print(heapq.nsmallest(3, heap))

