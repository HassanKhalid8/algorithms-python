"""Classic dynamic programming problems, solved bottom-up."""

from bisect import bisect_left


def fibonacci(n):
    """n-th Fibonacci number in O(n) time and O(1) space. fibonacci(0) == 0."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def knapsack(weights, values, capacity):
    """Best total value of 0/1 knapsack using a 1-D table."""
    best = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for c in range(capacity, weight - 1, -1):
            best[c] = max(best[c], best[c - weight] + value)
    return best[capacity]


def longest_common_subsequence(a, b):
    """One longest common subsequence of two strings."""
    rows, cols = len(a), len(b)
    table = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if a[i] == b[j]:
                table[i][j] = table[i + 1][j + 1] + 1
            else:
                table[i][j] = max(table[i + 1][j], table[i][j + 1])
    result = []
    i = j = 0
    while i < rows and j < cols:
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif table[i + 1][j] >= table[i][j + 1]:
            i += 1
        else:
            j += 1
    return "".join(result)


def longest_increasing_subsequence(items):
    """Length of the longest strictly increasing subsequence, O(n log n)."""
    tails = []
    for x in items:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def edit_distance(a, b):
    """Levenshtein distance: minimum inserts, deletes and substitutions."""
    previous = list(range(len(b) + 1))
    for i, char_a in enumerate(a, 1):
        current = [i]
        for j, char_b in enumerate(b, 1):
            current.append(min(
                previous[j] + 1,
                current[j - 1] + 1,
                previous[j - 1] + (char_a != char_b),
            ))
        previous = current
    return previous[-1]


def coin_change(coins, amount):
    """Fewest coins summing to amount, or -1 if impossible."""
    infinity = amount + 1
    fewest = [0] + [infinity] * amount
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                fewest[total] = min(fewest[total], fewest[total - coin] + 1)
    return -1 if fewest[amount] == infinity else fewest[amount]


def max_subarray_sum(items):
    """Kadane's algorithm: largest sum of a non-empty contiguous slice."""
    if not items:
        raise ValueError("items must not be empty")
    best = current = items[0]
    for x in items[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best
