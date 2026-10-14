import bisect
import unittest

from algorithms import searching


class TestSearching(unittest.TestCase):
    data = [1, 3, 3, 3, 7, 9, 12, 15]

    def test_linear_search(self):
        self.assertEqual(searching.linear_search([4, 2, 2], 2), 1)
        self.assertEqual(searching.linear_search([4, 2], 5), -1)
        self.assertEqual(searching.linear_search([], 1), -1)

    def test_binary_and_exponential_search(self):
        for search in (searching.binary_search, searching.exponential_search):
            with self.subTest(search=search.__name__):
                for target in (1, 7, 15):
                    self.assertEqual(self.data[search(self.data, target)], target)
                self.assertEqual(self.data[search(self.data, 3)], 3)
                self.assertEqual(search(self.data, 8), -1)
                self.assertEqual(search(self.data, 100), -1)
                self.assertEqual(search([], 1), -1)

    def test_bounds_match_bisect(self):
        for target in range(0, 17):
            self.assertEqual(searching.lower_bound(self.data, target), bisect.bisect_left(self.data, target))
            self.assertEqual(searching.upper_bound(self.data, target), bisect.bisect_right(self.data, target))

    def test_count_occurrences(self):
        self.assertEqual(searching.count_occurrences(self.data, 3), 3)
        self.assertEqual(searching.count_occurrences(self.data, 4), 0)


if __name__ == "__main__":
    unittest.main()
