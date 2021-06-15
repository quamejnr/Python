# Breadth-first search algorithm with Graph Data Structure
from collections import deque

graph = {'you': ['alice', 'bob', 'claire'], 'bob': ['anuj', 'peggy'], 'alice': ['peggy'], 'claire': ['thom', 'jonny'],
         'anuj': [], 'peggy': [], 'thom': [], 'jonny': []}


def mango_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if mango_seller(person):
                print(f"{person} is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    print('You know no mango seller')
    return False


# search('you')


paths = {'tp': ['a', 'b'], 'a': ['c'], 'b': ["d", 'e'], 'd': ['c'], 'e': ['c'], 'c': ['gg'], 'gg': []}


def get_key(lst, val):
    for key, value in lst.items():
        if val in value:
            return key
    return False


def shortest_path(path, start, end):
    search_path = deque()
    search_path += path[start]

    searched = []
    while search_path:
        bus_stop = search_path.popleft()

        if bus_stop not in searched:
            if bus_stop == end:
                # printing the shortest route taken and appending the destination
                shortest_route = [bus_stop]

                # putting the bus stop into the shortest route list as long as it has a key
                while get_key(path, bus_stop):
                    bus_stop = get_key(path, bus_stop)
                    shortest_route.append(bus_stop)
                print(f'Shortest Path Found')
                print(' --> '.join(shortest_route[::-1]))
                return True
            else:
                search_path += path[bus_stop]
                searched.append(bus_stop)
    print("Not found")
    return False


shortest_path(paths, 'tp', 'gg')

