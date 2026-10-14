import unittest

from algorithms import graphs

GRAPH = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
}


class TestTraversal(unittest.TestCase):
    def test_bfs(self):
        self.assertEqual(graphs.bfs(GRAPH, "a"), ["a", "b", "c", "d", "e", "f"])

    def test_dfs(self):
        self.assertEqual(graphs.dfs(GRAPH, "a"), ["a", "b", "d", "f", "c", "e"])

    def test_shortest_path_unweighted(self):
        self.assertEqual(graphs.shortest_path_unweighted(GRAPH, "a", "f"), ["a", "b", "d", "f"])
        self.assertEqual(graphs.shortest_path_unweighted(GRAPH, "a", "a"), ["a"])
        self.assertIsNone(graphs.shortest_path_unweighted(GRAPH, "f", "a"))


class TestDijkstra(unittest.TestCase):
    def test_prefers_cheaper_longer_route(self):
        weighted = {
            "a": {"b": 10, "c": 1},
            "c": {"d": 1},
            "d": {"b": 1},
            "b": {"e": 2},
        }
        self.assertEqual(graphs.dijkstra(weighted, "a"), {"a": 0, "c": 1, "d": 2, "b": 3, "e": 5})


class TestOrdering(unittest.TestCase):
    def test_topological_sort_respects_edges(self):
        order = graphs.topological_sort(GRAPH)
        position = {node: i for i, node in enumerate(order)}
        for node, neighbours in GRAPH.items():
            for neighbour in neighbours:
                self.assertLess(position[node], position[neighbour])

    def test_cycle_detection(self):
        self.assertFalse(graphs.has_cycle(GRAPH))
        self.assertTrue(graphs.has_cycle({"x": ["y"], "y": ["z"], "z": ["x"]}))
        with self.assertRaises(ValueError):
            graphs.topological_sort({"x": ["x"]})

    def test_connected_components(self):
        graph = {1: [2], 2: [3], 4: [5], 6: []}
        self.assertEqual(graphs.connected_components(graph), [[1, 2, 3], [4, 5], [6]])


if __name__ == "__main__":
    unittest.main()
