import unittest
import BFS
from BFS import graph

class testBFS(unittest.TestCase):
    def testBFS(self):
        G = graph()
        G.addEdge('v','r')
        G.addEdge('s','r')
        G.addEdge('s','w')
        G.addEdge('t','w')
        G.addEdge('x','w')
        G.addEdge('x','t')
        G.addEdge('u','t')
        G.addEdge('x','y')
        G.addEdge('x','u')
        G.addEdge('y','u')

        BFS.BFS(G, 's')

        self.assertEqual(G.distance['s'], 0)
        self.assertEqual(G.distance['w'], 1)
        self.assertEqual(G.distance['r'], 1)
        self.assertEqual(G.distance['v'], 2)
        self.assertEqual(G.distance['t'], 2)
        self.assertEqual(G.distance['x'], 2)
        self.assertEqual(G.distance['u'], 3)
        self.assertEqual(G.distance['y'], 3)

        #import pdb;pdb.set_trace()

if __name__ == "__main__":
    unittest.main()
        



