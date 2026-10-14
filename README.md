# algorithms-python

![tests](https://github.com/HassanKhalid8/algorithms-python/actions/workflows/tests.yml/badge.svg)

Clean, tested implementations of classic algorithms and data structures in pure Python (standard library only).

## Contents

| Module | What's inside |
| --- | --- |
| `algorithms/sorting.py` | bubble, insertion, merge, quick, heap, counting sort |
| `algorithms/searching.py` | linear, binary, lower/upper bound, exponential search |
| `algorithms/data_structures.py` | stack, queue, min-heap, linked list, union-find, trie |
| `algorithms/graphs.py` | BFS, DFS, shortest path, Dijkstra, topological sort, cycle detection, connected components |
| `algorithms/dynamic_programming.py` | fibonacci, knapsack, LCS, LIS, edit distance, coin change, max subarray (Kadane) |
| `algorithms/strings.py` | palindrome, anagram, KMP, Rabin-Karp, run-length encoding, longest palindromic substring |

## Usage

```python
from algorithms.sorting import merge_sort
from algorithms.graphs import dijkstra

merge_sort([5, 2, 9, 1])          # [1, 2, 5, 9]
dijkstra({"a": {"b": 4, "c": 1}, "c": {"b": 2}}, "a")
# {'a': 0, 'b': 3, 'c': 1}
```

## Running the tests

```bash
python -m unittest discover -s tests -v
```

Requires Python 3.9+.
