import unittest
import DFS
from graph import Graph

class testDFS(unittest.TestCase):
    def test_DFS(self):
        G = Graph()
        G.add_vertex('u', 'v')
        G.add_vertex('u', 'x')
        G.add_vertex('x', 'v')
        G.add_vertex('v', 'y')
        G.add_vertex('y', 'x')
        G.add_vertex('w', 'y')
        G.add_vertex('w', 'z')
        G.add_vertex('z', 'z')

        DFS.recursive_dfs(G)
        G.debug()
        G.clean()

        DFS.iterative_dfs(G, 'u')
        DFS.iterative_dfs(G, 'w')
        G.debug()


if __name__ == "__main__":
    unittest.main()
