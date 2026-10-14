"""Sorting algorithms. Every function returns a new sorted list and leaves the input untouched."""


def bubble_sort(items):
    """O(n^2). Stops early once a full pass makes no swaps."""
    result = list(items)
    n = len(result)
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
    return result


def insertion_sort(items):
    """O(n^2) worst case, O(n) on nearly sorted input."""
    result = list(items)
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def merge_sort(items):
    """O(n log n), stable."""
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(items):
    """O(n log n) average. Three-way partition handles many duplicates well."""
    if len(items) <= 1:
        return list(items)
    pivot = items[len(items) // 2]
    less = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    greater = [x for x in items if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


def heap_sort(items):
    """O(n log n), in-place on a copy using a max-heap."""
    result = list(items)
    n = len(result)

    def sift_down(start, end):
        root = start
        while 2 * root + 1 < end:
            child = 2 * root + 1
            if child + 1 < end and result[child] < result[child + 1]:
                child += 1
            if result[root] >= result[child]:
                return
            result[root], result[child] = result[child], result[root]
            root = child

    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n)
    for end in range(n - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        sift_down(0, end)
    return result


def counting_sort(items):
    """O(n + k) for integers, where k is the value range. Supports negatives."""
    if not items:
        return []
    low, high = min(items), max(items)
    counts = [0] * (high - low + 1)
    for x in items:
        counts[x - low] += 1
    result = []
    for offset, count in enumerate(counts):
        result.extend([offset + low] * count)
    return result
