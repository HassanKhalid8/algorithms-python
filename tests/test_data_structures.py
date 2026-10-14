import random
import unittest

from algorithms.data_structures import LinkedList, MinHeap, Queue, Stack, Trie, UnionFind


class TestStackAndQueue(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        for x in (1, 2, 3):
            stack.push(x)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual([stack.pop(), stack.pop(), stack.pop()], [3, 2, 1])
        with self.assertRaises(IndexError):
            stack.pop()

    def test_queue_interleaved(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3)
        self.assertEqual([queue.dequeue(), queue.dequeue()], [2, 3])
        self.assertEqual(len(queue), 0)
        with self.assertRaises(IndexError):
            queue.dequeue()


class TestMinHeap(unittest.TestCase):
    def test_pops_in_sorted_order(self):
        rng = random.Random(7)
        data = [rng.randint(-50, 50) for _ in range(100)]
        heap = MinHeap()
        for x in data:
            heap.push(x)
        self.assertEqual([heap.pop() for _ in range(len(data))], sorted(data))
        with self.assertRaises(IndexError):
            heap.pop()


class TestLinkedList(unittest.TestCase):
    def test_build_append_remove_reverse(self):
        linked = LinkedList([1, 2, 3])
        linked.append(4)
        self.assertEqual(list(linked), [1, 2, 3, 4])
        self.assertTrue(linked.remove(1))
        self.assertTrue(linked.remove(3))
        self.assertFalse(linked.remove(99))
        linked.reverse()
        self.assertEqual(list(linked), [4, 2])
        self.assertEqual(len(linked), 2)


class TestUnionFind(unittest.TestCase):
    def test_components(self):
        uf = UnionFind(6)
        self.assertTrue(uf.union(0, 1))
        self.assertTrue(uf.union(1, 2))
        self.assertFalse(uf.union(0, 2))
        uf.union(3, 4)
        self.assertTrue(uf.connected(0, 2))
        self.assertFalse(uf.connected(2, 3))
        self.assertEqual(uf.components, 3)


class TestTrie(unittest.TestCase):
    def test_lookup_and_prefix(self):
        trie = Trie()
        for word in ("car", "card", "care", "cat", "dog"):
            trie.insert(word)
        self.assertTrue(trie.contains("car"))
        self.assertFalse(trie.contains("ca"))
        self.assertEqual(trie.starts_with("car"), ["car", "card", "care"])
        self.assertEqual(trie.starts_with("z"), [])


if __name__ == "__main__":
    unittest.main()
