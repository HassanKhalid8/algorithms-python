import random
import re
import unittest

from algorithms import strings


def naive_find_all(text, pattern):
    return [m.start() for m in re.finditer("(?=" + re.escape(pattern) + ")", text)]


class TestStrings(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(strings.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(strings.is_palindrome(""))
        self.assertFalse(strings.is_palindrome("python"))

    def test_are_anagrams(self):
        self.assertTrue(strings.are_anagrams("Dormitory", "dirty room"))
        self.assertFalse(strings.are_anagrams("abc", "abd"))

    def test_pattern_search(self):
        for search in (strings.kmp_search, strings.rabin_karp_search):
            with self.subTest(search=search.__name__):
                self.assertEqual(search("abababa", "aba"), [0, 2, 4])
                self.assertEqual(search("hello", "xyz"), [])
                self.assertEqual(search("ab", "abc"), [])

    def test_pattern_search_matches_regex_on_random_text(self):
        rng = random.Random(3)
        for _ in range(100):
            text = "".join(rng.choice("ab") for _ in range(rng.randint(0, 40)))
            pattern = "".join(rng.choice("ab") for _ in range(rng.randint(1, 4)))
            expected = naive_find_all(text, pattern)
            self.assertEqual(strings.kmp_search(text, pattern), expected)
            self.assertEqual(strings.rabin_karp_search(text, pattern), expected)

    def test_run_length_round_trip(self):
        encoded = strings.run_length_encode("aaabccdddd")
        self.assertEqual(encoded, [("a", 3), ("b", 1), ("c", 2), ("d", 4)])
        self.assertEqual(strings.run_length_decode(encoded), "aaabccdddd")
        self.assertEqual(strings.run_length_encode(""), [])

    def test_longest_palindromic_substring(self):
        self.assertIn(strings.longest_palindromic_substring("babad"), ("bab", "aba"))
        self.assertEqual(strings.longest_palindromic_substring("cbbd"), "bb")
        self.assertEqual(strings.longest_palindromic_substring(""), "")


if __name__ == "__main__":
    unittest.main()
