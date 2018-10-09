"""implementation of Graph class for BFS/DFS"""


class Graph(object):
    """
    implementation of a non-weighed
    non-directed graph

    Args:
        color: dict of char, where key is the node and value is the color

        distance: dict of int, key is the node and value is
            the distance from root

        adj: adjacency list, dict of sets, key is node and value is
            set of adjacent nodes

        prev: dict of int, where key is node val is prev node

        discovery: dict of int, discovery time for every node (DFS)

        finishing: dict of int, finishing time for every node (DFS)
    """
    def __init__(self):
        self.color = {}  # dict of char
        self.distance = {}  # dict of int
        self.adj = {}  # dict of sets
        self.prev = {}  # dict of int
        self.discovery = {}  # dict of int
        self.finishing = {}   # dict of int

    def clean(self):
        """clean the dicts to repopulated them later"""
        self.color = {}  # dict of char
        self.distance = {}  # dict of int
        self.prev = {}  # dict of int
        self.discovery = {}  # dict of int
        self.finishing = {}   # dict of int

    def debug(self):
        """debug function to print out graph data"""
        for attr in dir(self):
            if attr[0] != '_':
                print "{} {}".format(attr, getattr(self, attr))

    def add_vertex(self, first_vertex, second_vertex):
        """
        helper to add second_vertex to first_vertex adj list
        Args:
            u: first vertex
            v: second vertex
        """
        if self.adj.get(first_vertex) is None:
            self.adj[first_vertex] = set(second_vertex)
        else:
            self.adj[first_vertex].add(second_vertex)

    def add_edge(self, first_vertex, second_vertex):
        """
        adds edges in a non-directed graph A->B and B->A
        Args:
            first_vertex
            second_vertex
        """
        self.add_vertex(first_vertex, second_vertex)
        self.add_vertex(second_vertex, first_vertex)
