# algorithms-python

Clean, tested implementations of classic algorithms and data structures in pure Python (standard library only).

## Contents

| Module | What's inside |
| --- | --- |
| `algorithms/sorting.py` | bubble, insertion, merge, quick, heap, counting sort |
| `algorithms/searching.py` | linear, binary, lower/upper bound, exponential search |
| `algorithms/data_structures.py` | stack, queue, min-heap, linked list, union-find, trie |
| `algorithms/graphs.py` | BFS, DFS, Dijkstra, topological sort, cycle detection |
| `algorithms/dynamic_programming.py` | fibonacci, knapsack, LCS, LIS, edit distance, coin change |
| `algorithms/strings.py` | palindrome, anagram, KMP search, Rabin-Karp, run-length encoding |

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
