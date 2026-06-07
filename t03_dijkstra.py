"""
Dijkstra's Shortest Path Algorithm using Binary Min-Heap
Finds shortest paths from a source vertex to all other vertices
in a weighted directed/undirected graph.
    Time Complexity:  O((V + E) log V)
    Space Complexity: O(V + E)
"""
import heapq
from collections import defaultdict
from typing import Dict, List, Optional, Tuple
import math

# Graph Data Structure
class WeightedGraph:
    """
    Adjacency-list representation of a weighted graph.
    Supports both directed and undirected edges.
    """
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        self.vertices: set = set()

    def add_edge(self, u: str, v: str, weight: float) -> None:
        """Add a weighted edge u -> v (and v -> u for undirected graphs)."""
        if weight < 0:
            raise ValueError(
                f"Negative weight {weight} on edge ({u}, {v}). "
                "Dijkstra requires non-negative weights."
            )
        self.vertices.update([u, v])
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def add_vertex(self, v: str) -> None:
        """Register an isolated vertex (no edges yet)."""
        self.vertices.add(v)

    def neighbors(self, v: str) -> List[Tuple[str, float]]:
        """Return all (neighbor, weight) pairs for vertex v."""
        return self.adj.get(v, [])

    def __repr__(self) -> str:
        lines = [f"WeightedGraph(directed={self.directed})"]
        for v in sorted(self.vertices):
            edges = ", ".join(f"{u}({w})" for u, w in self.adj.get(v, []))
            lines.append(f"  {v} -> [{edges}]")
        return "\n".join(lines)

# Binary Min-Heap Priority Queue
class MinHeap:
    """
    Binary min-heap built on top of Python's `heapq` module.
    Each element is a (priority, vertex) tuple.
    Supports lazy deletion to avoid O(V) decrease-key operations.
    """
    def __init__(self):
        self._heap: List[Tuple[float, str]] = []
        self._entry_count: int = 0          # tie-breaker counter
        self._removed: set = set()          # vertices already finalised

    def push(self, priority: float, vertex: str) -> None:
        """Insert or re-insert vertex with given priority."""
        # Use entry_count as a tie-breaker so string comparison is never needed
        heapq.heappush(self._heap, (priority, self._entry_count, vertex))
        self._entry_count += 1

    def pop(self) -> Tuple[float, str]:
        """
        Remove and return (priority, vertex) with the smallest priority.
        Skips stale entries (lazy deletion).
        Raises IndexError when heap is empty.
        """
        while self._heap:
            priority, _, vertex = heapq.heappop(self._heap)
            if vertex not in self._removed:
                self._removed.add(vertex)
                return priority, vertex
        raise IndexError("pop from an empty heap")

    def is_empty(self) -> bool:
        return all(v in self._removed for _, __, v in self._heap)

    def __len__(self) -> int:
        return sum(1 for _, __, v in self._heap if v not in self._removed)

# Dijkstra's Algorithm
class DijkstraResult:
    """Container for the algorithm's output."""
    def __init__(
        self,
        source: str,
        dist: Dict[str, float],
        prev: Dict[str, Optional[str]],
    ):
        self.source = source
        self.dist = dist
        self.prev = prev

    def path_to(self, target: str) -> List[str]:
        """
        Reconstruct the shortest path from source → target.
        Returns an empty list if target is unreachable.
        """
        if self.dist[target] == math.inf:
            return []
        path, node = [], target
        while node is not None:
            path.append(node)
            node = self.prev.get(node)
        return path[::-1]

    def distance_to(self, target: str) -> float:
        """Return shortest-path distance; math.inf if unreachable."""
        return self.dist.get(target, math.inf)

    def summary(self) -> str:
        lines = [f"\nShortest paths from source '{self.source}'",
                 "-" * 50]
        for vertex in sorted(self.dist):
            if vertex == self.source:
                continue
            d = self.dist[vertex]
            path = self.path_to(vertex)
            path_str = " -> ".join(path) if path else "unreachable"
            dist_str = f"{d:.2f}" if d != math.inf else "infinity"
            lines.append(f"  {self.source} -> {vertex}: {dist_str:>8}   path: {path_str}")
        return "\n".join(lines)


def dijkstra(graph: WeightedGraph, source: str) -> DijkstraResult:
    """
    Dijkstra's algorithm with a binary min-heap.
    Parameters:
        graph  : WeightedGraph
        source : starting vertex
    Returns:
        DijkstraResult with distances and predecessor map.
    Complexity:
        Time:  O((V + E) log V)
        Space: O(V + E)
    """
    if source not in graph.vertices:
        raise ValueError(f"Source vertex '{source}' not found in graph.")

    # Initialise distances to infinity, source to 0
    dist: Dict[str, float] = {v: math.inf for v in graph.vertices}
    prev: Dict[str, Optional[str]] = {v: None for v in graph.vertices}
    dist[source] = 0.0

    heap = MinHeap()
    heap.push(0.0, source)

    visited: set = set()

    while not heap.is_empty():
        try:
            current_dist, u = heap.pop()
        except IndexError:
            break

        # Skip if we already found a shorter path to u
        if u in visited:
            continue
        visited.add(u)

        # Early-exit: remaining distances can only be larger
        if current_dist > dist[u]:
            continue

        for v, weight in graph.neighbors(u):
            if v in visited:
                continue
            relaxed = dist[u] + weight
            if relaxed < dist[v]:
                dist[v] = relaxed
                prev[v] = u
                heap.push(relaxed, v)  # lazy insertion (no decrease-key)

    return DijkstraResult(source, dist, prev)

# Demo & Tests
def demo_small_undirected():
    """Classic textbook example - undirected graph."""
    print("\n", "~" * 5, " DEMO 1 -- Small undirected graph ", "~" * 5, "\n")

    g = WeightedGraph(directed=False)
    edges = [
        ("A", "B", 4), ("A", "C", 2),
        ("B", "C", 5), ("B", "D", 10),
        ("C", "E", 3),
        ("E", "D", 4),
        ("D", "F", 11),
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)

    print(g)
    result = dijkstra(g, "A")
    print(result.summary())


def demo_directed_weighted():
    """Directed graph with multiple path options."""
    print("\n", "~" * 5, " DEMO 2 -- Directed weighted graph ", "~" * 5, "\n")

    g = WeightedGraph(directed=True)
    edges = [
        ("S", "A", 10), ("S", "C", 5),
        ("A", "B", 1), ("A", "C", 2),
        ("C", "A", 3), ("C", "B", 9), ("C", "D", 2),
        ("B", "D", 4),
        ("D", "E", 6),
        ("E", "B", 6),
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)

    print(g)
    result = dijkstra(g, "S")
    print(result.summary())


def demo_with_isolated_vertex():
    """Graph containing an unreachable vertex."""
    print("\n", "~" * 5, " DEMO 3 -- Graph with isolated (unreachable) vertex ", "~" * 5, "\n")

    g = WeightedGraph(directed=False)
    g.add_edge("1", "2", 7)
    g.add_edge("1", "3", 9)
    g.add_edge("2", "4", 2)
    g.add_edge("3", "4", 11)
    g.add_vertex("X")          # isolated - no edges

    print(g)
    result = dijkstra(g, "1")
    print(result.summary())

    # Verify single path
    print(f"\n  Explicit path 1 -> 4: {' -> '.join(result.path_to('4'))}")
    print(f"  Explicit path 1 -> X: {result.path_to('X') or 'unreachable'}")


def run_unit_tests():
    """Lightweight assertions to validate correctness."""
    print("\n", "~" * 5, " UNIT TESTS ", "~" * 5, "\n")

    # Test 1: known shortest distances
    g = WeightedGraph(directed=False)
    for u, v, w in [("A","B",1),("B","C",2),("A","C",10)]:
        g.add_edge(u, v, w)
    r = dijkstra(g, "A")
    assert r.distance_to("C") == 3, "Should prefer A -> B -> C (cost 3)"
    assert r.path_to("C") == ["A", "B", "C"], "Wrong path"
    print("  Test 1 passed -- prefers shorter multi-hop path")

    # Test 2: single vertex graph
    g2 = WeightedGraph()
    g2.add_vertex("Z")
    r2 = dijkstra(g2, "Z")
    assert r2.distance_to("Z") == 0
    print("  Test 2 passed -- single vertex, distance to self = 0")

    # Test 3: directed - path in one direction only
    g3 = WeightedGraph(directed=True)
    g3.add_edge("X", "Y", 5)
    r3 = dijkstra(g3, "Y")
    assert r3.distance_to("X") == math.inf, "X not reachable from Y"
    print("  Test 3 passed -- directed: reverse direction is unreachable")

    # Test 4: negative weight guard
    g4 = WeightedGraph()
    try:
        g4.add_edge("P", "Q", -1)
        print("  Test 4 FAILED -- should have raised ValueError")
    except ValueError:
        print("  Test 4 passed -- negative weight correctly rejected")


if __name__ == "__main__":
    demo_small_undirected()
    demo_directed_weighted()
    demo_with_isolated_vertex()
    run_unit_tests()