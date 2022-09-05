import unittest
import pathfinder

class TestStringMethods(unittest.TestCase):

    def test_dijkstra(self):
        graph = {
            'A': {'B': 5, 'D': 1},
            'B': {'A': 3, 'C': 1},
            'C': {'A': 10, 'G': 4},
            'D': {'E': 3},
            'E': {'C': 2},
            'F': {'A': 2, 'D': 7, 'G': 4},
            'G': {'C': 1, 'E': 1, 'F': 1}
        }

        self.assertEqual(pathfinder.dijkstra(graph, "G", "B"), "G->F->A->B")

    def test_bfs(self):
        graph = {
            'A': {'B': 5, 'D': 1},
            'B': {'A': 3, 'C': 1},
            'C': {'A': 10, 'G': 4},
            'D': {'E': 3},
            'E': {'C': 2},
            'F': {'A': 2, 'D': 7, 'G': 4},
            'G': {'C': 1, 'E': 1, 'F': 1}
        }
        self.assertEqual(pathfinder.bfs(graph, "G", "B"), ['G', 'C', 'A', 'B'])


if __name__ == '__main__':
    unittest.main()
