from graph import Graph
testcestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8),
               (8, 9), (11, 8), (10, 1)]


def ancestor_helper(storage, lengths, current_node, current_length=None):

    if current_length == None:
        current_length = 0

    if current_length not in lengths.keys():
        lengths[current_length] = []

    lengths[current_length].append(current_node)

    for neighbor in storage.get_neighbors(current_node):
        ancestor_helper(storage, lengths, neighbor, current_length + 1)


def earliest_ancestor(ancestors, starting_node):
    # Create the graph
    storage = Graph()

    lengths = {}

    # Add everything to our graph:
    for ancestor in ancestors:
        storage.add_vertex(ancestor[0])
        storage.add_vertex(ancestor[1])
        storage.add_edge(ancestor[1], ancestor[0])

    if storage.get_neighbors(starting_node) == []:
        return -1

    ancestor_helper(storage, lengths, starting_node)

    return min(lengths[list(lengths.keys())[-1]])


print(earliest_ancestor(testcestors, 6))
print(earliest_ancestor(testcestors, 2))
