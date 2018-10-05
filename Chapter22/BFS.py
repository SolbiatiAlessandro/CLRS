class graph:
    """
    implementation of a non-weighed
    non-directed graph
    """
    def __init__(self):
        self.color = {}  # dict of char
        self.distance = {}  # dict of int
        self.adj = {}  # dict of sets
        self.prev = {}  # dict of int

    def addVertex(self, u, v):
        if self.adj.get(u) is None:
            self.adj[u] = set(v)
        else:
            self.adj[u].add(v)

    def addEdge(self, u, v):
        self.addVertex(u, v)
        self.addVertex(v, u)
        

def BFS(G, s):
    """
    BFS implementation following CLRS pg. 533
    """
    queue = [s]
    G.distance[s] = 0
    G.prev[s] = None
    while queue:
        vertex = queue.pop()
        distance = G.distance[vertex]
        for adjVertex in G.adj[vertex]:
            if G.color.get(adjVertex) is None:
                G.color[adjVertex] = "grey"
                G.distance[adjVertex] = distance+1
                G.prev[adjVertex] = vertex
                queue.insert(0, adjVertex)
        G.color[vertex] = "black"

def printPath(G, v):
    """
    iterative function to print the path from s to v
    """
    curr = v
    print curr
    while G.prev[curr] is not None:
        print G.prev[curr]
        curr = G.prev[curr]



