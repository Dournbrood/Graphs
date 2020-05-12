"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.visited = None

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices.keys():
            self.vertices[vertex_id] = []

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices.keys() and v2 in self.vertices.keys():
            self.vertices[v1].append(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Breadth-first algorithms simply use queues as their buffer.

        q = Queue()

        visited = set()

        # Base case:
        #     If queue is empty, stop looping.

        q.enqueue(starting_vertex)

        while q.size() > 0:
            vertex = q.dequeue()
            if vertex not in visited and vertex != None:
                print(vertex)
                visited.add(vertex)

                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        s = Stack()

        visited = set()

        # Base case:
        #     If stack is empty, stop looping.

        s.push(starting_vertex)

        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited and vertex != None:
                print(vertex)
                visited.add(vertex)

                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # print(f"dft_recursive({starting_vertex}, {self.visited})")

        if self.visited == None:
            self.visited = set()

        self.visited.add(starting_vertex)

        print(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in self.visited:
                self.dft_recursive(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        q = Queue()

        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]

            if vertex not in visited:
                visited.add(vertex)

                if vertex == destination_vertex:
                    return path

                for neighbor in self.get_neighbors(vertex):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]

            if vertex not in visited:
                visited.add(vertex)

                if vertex == destination_vertex:
                    return path

                for neighbor in self.get_neighbors(vertex):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # current node is starting vertex
        # If current node is destination, return current node
        # Enqueue all neighbors
        # Dequeue one neighbor, recursively call BFS on it.

        if path == None:
            path = []

        path.append(starting_vertex)

        if visited == None:
            visited = set()

        vertex = path[-1]

        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            print(visited)

            if vertex == destination_vertex:
                print("BASE")
                return path

            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    return self.dfs_recursive(neighbor, destination_vertex, visited, path)

        return path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
