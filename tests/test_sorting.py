import random
import unittest

from algorithms import sorting

SORTERS = [
    sorting.bubble_sort,
    sorting.insertion_sort,
    sorting.merge_sort,
    sorting.quick_sort,
    sorting.heap_sort,
    sorting.counting_sort,
]


class TestSorting(unittest.TestCase):
    def test_edge_cases(self):
        for sort in SORTERS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort([]), [])
                self.assertEqual(sort([7]), [7])
                self.assertEqual(sort([3, 3, 3]), [3, 3, 3])
                self.assertEqual(sort([5, -2, 0, -9, 4]), [-9, -2, 0, 4, 5])

    def test_matches_builtin_on_random_input(self):
        rng = random.Random(42)
        for _ in range(50):
            data = [rng.randint(-100, 100) for _ in range(rng.randint(0, 60))]
            for sort in SORTERS:
                with self.subTest(sort=sort.__name__):
                    self.assertEqual(sort(data), sorted(data))

    def test_input_not_mutated(self):
        data = [4, 1, 3, 2]
        for sort in SORTERS:
            sort(data)
            self.assertEqual(data, [4, 1, 3, 2])


if __name__ == "__main__":
    unittest.main()
