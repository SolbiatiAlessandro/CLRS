"""implementation of DFS functions from CLRS 22.3 Depth-first search"""


def recursive_dfs(graph):
    """main DFS function for recursive DFS:
    explores all white vertices and call recursion as in CLRS pg. 541
    """
    graph.time = 0
    for vertex in graph.adj.keys():
        if vertex not in graph.color:
            recursive_dfs_call(graph, vertex)


def recursive_dfs_call(graph, vertex):
    """recursive function for DFS:
    updates graph.time and populate discovery and finishing dict
    for the given vertex, exploring white adj vertices as in CLRS pg. 541
    """
    graph.color[vertex] = 'grey'
    graph.time += 1
    graph.discovery[vertex] = graph.time
    for elem in graph.adj[vertex]:
        if elem not in graph.color:
            graph.prev[elem] = vertex
            recursive_dfs_call(graph, elem)
    graph.color[vertex] = 'black'
    graph.time += 1
    graph.finishing[vertex] = graph.time


def iterative_dfs(graph, start):
    """iterative function for DFS:
    exercise 22.3-6 CLRS pg. 548
    Args:
        graph: Graph instance
        start: starting vertex
    """
    graph.time = 0
    stack = [start]
    while stack:
        vertex = stack[-1]
        if vertex in graph.color:
            if graph.color[vertex] == 'grey':
                graph.color[vertex] = 'black'
                graph.time += 1
                graph.finishing[vertex] = graph.time
            stack.pop()
        elif vertex not in graph.color:
            graph.color[vertex] = 'grey'
            graph.time += 1
            graph.discovery[vertex] = graph.time
            for elem in graph.adj[vertex]:
                if elem not in graph.color:
                    graph.prev[elem] = vertex
                    stack.append(elem)
