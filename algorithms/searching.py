"""Searching algorithms. Binary-search variants expect a list sorted ascending."""


def linear_search(items, target):
    """Return the index of the first match, or -1."""
    for i, value in enumerate(items):
        if value == target:
            return i
    return -1


def binary_search(items, target):
    """Return an index of target, or -1. O(log n)."""
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def lower_bound(items, target):
    """First index whose value is >= target (len(items) if none)."""
    low, high = 0, len(items)
    while low < high:
        mid = (low + high) // 2
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def upper_bound(items, target):
    """First index whose value is > target (len(items) if none)."""
    low, high = 0, len(items)
    while low < high:
        mid = (low + high) // 2
        if items[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


def count_occurrences(items, target):
    """How many times target appears, in O(log n)."""
    return upper_bound(items, target) - lower_bound(items, target)


def exponential_search(items, target):
    """Find the range by doubling, then binary search inside it. Good for unbounded lists."""
    if not items:
        return -1
    if items[0] == target:
        return 0
    bound = 1
    while bound < len(items) and items[bound] < target:
        bound *= 2
    low, high = bound // 2, min(bound, len(items) - 1)
    index = binary_search(items[low:high + 1], target)
    return -1 if index == -1 else low + index
