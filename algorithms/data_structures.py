"""Core data structures built from scratch."""


class Stack:
    """LIFO stack backed by a Python list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def __len__(self):
        return len(self._items)


class Queue:
    """FIFO queue using two stacks, so each operation is amortised O(1)."""

    def __init__(self):
        self._inbox = []
        self._outbox = []

    def enqueue(self, item):
        self._inbox.append(item)

    def dequeue(self):
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())
        if not self._outbox:
            raise IndexError("dequeue from empty queue")
        return self._outbox.pop()

    def __len__(self):
        return len(self._inbox) + len(self._outbox)


class MinHeap:
    """Binary min-heap."""

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)
        i = len(self._data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self._data[parent] <= self._data[i]:
                break
            self._data[parent], self._data[i] = self._data[i], self._data[parent]
            i = parent

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty heap")
        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            i, n = 0, len(self._data)
            while True:
                smallest = i
                for child in (2 * i + 1, 2 * i + 2):
                    if child < n and self._data[child] < self._data[smallest]:
                        smallest = child
                if smallest == i:
                    break
                self._data[i], self._data[smallest] = self._data[smallest], self._data[i]
                i = smallest
        return top

    def peek(self):
        if not self._data:
            raise IndexError("peek at empty heap")
        return self._data[0]

    def __len__(self):
        return len(self._data)


class _Node:
    __slots__ = ("value", "next")

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """Singly linked list."""

    def __init__(self, values=()):
        self.head = None
        self._size = 0
        for value in reversed(list(values)):
            self.push_front(value)

    def push_front(self, value):
        self.head = _Node(value, self.head)
        self._size += 1

    def append(self, value):
        node = _Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self._size += 1

    def remove(self, value):
        """Remove the first node holding value. Returns True if one was removed."""
        previous, current = None, self.head
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self._size -= 1
                return True
            previous, current = current, current.next
        return False

    def reverse(self):
        previous, current = None, self.head
        while current:
            current.next, previous, current = previous, current, current.next
        self.head = previous

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size


class UnionFind:
    """Disjoint-set union with path compression and union by rank."""

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        """Merge the sets of a and b. Returns False if they were already joined."""
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        self.components -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)


class Trie:
    """Prefix tree for word lookup and autocomplete."""

    def __init__(self):
        self._root = {}

    def insert(self, word):
        node = self._root
        for char in word:
            node = node.setdefault(char, {})
        node["$"] = True

    def _walk(self, prefix):
        node = self._root
        for char in prefix:
            if char not in node:
                return None
            node = node[char]
        return node

    def contains(self, word):
        node = self._walk(word)
        return node is not None and "$" in node

    def starts_with(self, prefix):
        """All stored words beginning with prefix, in sorted order."""
        node = self._walk(prefix)
        if node is None:
            return []
        words = []
        stack = [(node, prefix)]
        while stack:
            current, text = stack.pop()
            for key, child in current.items():
                if key == "$":
                    words.append(text)
                else:
                    stack.append((child, text + key))
        return sorted(words)
