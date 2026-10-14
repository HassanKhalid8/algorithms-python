import unittest

from algorithms import dynamic_programming as dp


class TestDynamicProgramming(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual([dp.fibonacci(n) for n in range(10)], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(dp.fibonacci(90), 2880067194370816120)
        with self.assertRaises(ValueError):
            dp.fibonacci(-1)

    def test_knapsack(self):
        self.assertEqual(dp.knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7), 9)
        self.assertEqual(dp.knapsack([5], [10], 4), 0)

    def test_longest_common_subsequence(self):
        self.assertEqual(len(dp.longest_common_subsequence("ABCBDAB", "BDCABA")), 4)
        self.assertEqual(dp.longest_common_subsequence("abc", "abc"), "abc")
        self.assertEqual(dp.longest_common_subsequence("abc", "xyz"), "")

    def test_longest_increasing_subsequence(self):
        self.assertEqual(dp.longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(dp.longest_increasing_subsequence([7, 7, 7]), 1)
        self.assertEqual(dp.longest_increasing_subsequence([]), 0)

    def test_edit_distance(self):
        self.assertEqual(dp.edit_distance("kitten", "sitting"), 3)
        self.assertEqual(dp.edit_distance("", "abc"), 3)
        self.assertEqual(dp.edit_distance("same", "same"), 0)

    def test_coin_change(self):
        self.assertEqual(dp.coin_change([1, 2, 5], 11), 3)
        self.assertEqual(dp.coin_change([2], 3), -1)
        self.assertEqual(dp.coin_change([1], 0), 0)

    def test_max_subarray_sum(self):
        self.assertEqual(dp.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(dp.max_subarray_sum([-3, -1, -2]), -1)


if __name__ == "__main__":
    unittest.main()
