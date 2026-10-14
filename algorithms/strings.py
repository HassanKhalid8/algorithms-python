"""String algorithms."""

from collections import Counter


def is_palindrome(text):
    """Ignores case and anything that isn't a letter or digit."""
    cleaned = [char.lower() for char in text if char.isalnum()]
    return cleaned == cleaned[::-1]


def are_anagrams(a, b):
    """Ignores case and spaces."""
    def normalise(text):
        return Counter(text.replace(" ", "").lower())
    return normalise(a) == normalise(b)


def _prefix_function(pattern):
    """failure[i] = length of the longest proper prefix of pattern[:i+1] that is also a suffix."""
    failure = [0] * len(pattern)
    k = 0
    for i in range(1, len(pattern)):
        while k and pattern[i] != pattern[k]:
            k = failure[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        failure[i] = k
    return failure


def kmp_search(text, pattern):
    """Start index of every (possibly overlapping) match, in O(n + m)."""
    if not pattern:
        return list(range(len(text) + 1))
    failure = _prefix_function(pattern)
    matches = []
    k = 0
    for i, char in enumerate(text):
        while k and char != pattern[k]:
            k = failure[k - 1]
        if char == pattern[k]:
            k += 1
        if k == len(pattern):
            matches.append(i - k + 1)
            k = failure[k - 1]
    return matches


def rabin_karp_search(text, pattern, base=256, modulus=1_000_000_007):
    """Start index of every match using a rolling hash, verified to rule out collisions."""
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []
    high = pow(base, m - 1, modulus)
    pattern_hash = window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % modulus
        window_hash = (window_hash * base + ord(text[i])) % modulus
    matches = []
    for start in range(n - m + 1):
        if window_hash == pattern_hash and text[start:start + m] == pattern:
            matches.append(start)
        if start + m < n:
            window_hash = (window_hash - ord(text[start]) * high) % modulus
            window_hash = (window_hash * base + ord(text[start + m])) % modulus
    return matches


def run_length_encode(text):
    """'aaabcc' -> [('a', 3), ('b', 1), ('c', 2)]"""
    encoded = []
    for char in text:
        if encoded and encoded[-1][0] == char:
            encoded[-1] = (char, encoded[-1][1] + 1)
        else:
            encoded.append((char, 1))
    return encoded


def run_length_decode(pairs):
    return "".join(char * count for char, count in pairs)


def longest_palindromic_substring(text):
    """Expand around each centre, O(n^2)."""
    best_start, best_length = 0, 0
    for centre in range(len(text)):
        for left, right in ((centre, centre), (centre, centre + 1)):
            while left >= 0 and right < len(text) and text[left] == text[right]:
                left -= 1
                right += 1
            length = right - left - 1
            if length > best_length:
                best_start, best_length = left + 1, length
    return text[best_start:best_start + best_length]
