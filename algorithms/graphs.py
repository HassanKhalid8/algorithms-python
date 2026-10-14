"""Graph algorithms. Graphs are adjacency dicts: {node: [neighbours]} or, when
weighted, {node: {neighbour: weight}}. Nodes that only appear as neighbours are fine."""

import heapq
from collections import deque


def bfs(graph, start):
    """Nodes in breadth-first order from start."""
    seen = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph.get(node, ()):
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)
    return order


def dfs(graph, start):
    """Nodes in depth-first (preorder) order from start, iterative."""
    seen = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        order.append(node)
        for neighbour in reversed(list(graph.get(node, ()))):
            if neighbour not in seen:
                stack.append(neighbour)
    return order


def shortest_path_unweighted(graph, start, goal):
    """Fewest-edges path from start to goal as a list, or None if unreachable."""
    parents = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parents[node]
            return path[::-1]
        for neighbour in graph.get(node, ()):
            if neighbour not in parents:
                parents[neighbour] = node
                queue.append(neighbour)
    return None


def dijkstra(graph, start):
    """Shortest distance from start to every reachable node. Weights must be non-negative."""
    distances = {start: 0}
    heap = [(0, start)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances.get(node, float("inf")):
            continue
        for neighbour, weight in graph.get(node, {}).items():
            candidate = distance + weight
            if candidate < distances.get(neighbour, float("inf")):
                distances[neighbour] = candidate
                heapq.heappush(heap, (candidate, neighbour))
    return distances


def topological_sort(graph):
    """Kahn's algorithm. Raises ValueError if the directed graph has a cycle."""
    nodes = set(graph)
    for neighbours in graph.values():
        nodes.update(neighbours)
    indegree = {node: 0 for node in nodes}
    for neighbours in graph.values():
        for neighbour in neighbours:
            indegree[neighbour] += 1
    queue = deque(sorted(node for node in nodes if indegree[node] == 0))
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph.get(node, ()):
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    if len(order) != len(nodes):
        raise ValueError("graph contains a cycle")
    return order


def has_cycle(graph):
    """True if the directed graph contains a cycle."""
    try:
        topological_sort(graph)
    except ValueError:
        return True
    return False


def connected_components(graph):
    """Components of an undirected graph, each as a sorted list."""
    nodes = set(graph)
    for neighbours in graph.values():
        nodes.update(neighbours)
    undirected = {node: set() for node in nodes}
    for node, neighbours in graph.items():
        for neighbour in neighbours:
            undirected[node].add(neighbour)
            undirected[neighbour].add(node)
    seen = set()
    components = []
    for node in sorted(nodes):
        if node not in seen:
            component = bfs(undirected, node)
            seen.update(component)
            components.append(sorted(component))
    return components
