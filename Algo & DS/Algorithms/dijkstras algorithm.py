""" The Dijkstra's algorithm """

graph = dict()

# weights of neighbours of start
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

# weights of neighbours of a
graph['a'] = {}
graph['a']['fin'] = 1

# weights of neighbours of b
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

# final node
graph['fin'] = {}


# Costs Table
infinity = float('inf')

costs = {'a': 6, 'b': 2, 'fin': infinity}

# Parents Table
parents = {'a': 'start', 'b': 'start', 'fin': None}

# An array of processed nodes
processed = []


def find_lowest_cost_node(costs):
    processed_node = []

    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed_node:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    print(parents)
    print(costs)
