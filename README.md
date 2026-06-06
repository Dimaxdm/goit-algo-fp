# Task 01 $\textemdash$ Singly Linked List: Reverse, Sort, Merge

A focused Python implementation of a singly linked list covering three classic operations: reversal, insertion sort, and merging two sorted lists. The implementation is numerically typed and includes input validation and a self-contained demo.

## Structure 

> └── t01_linkedlist.py          # Node, LinkedList, helpers, and demo

## Classes & Functions

| Name | Type | Description | 
| --- | --- | --- |
| `Node` | class | A single list node. Accepts only `int` or `float`; raises `TypeError` otherwise |
| `LinkedList` | class | Singly linked list with `append`, `to_list`, `reverse`, and `insertion_sort` | 
| `_sorted_insert` | function | Helper $\textemdash$ inserts a node into the correct position in a sorted list | 
| `merge_sorted` | function | Merges two sorted lists into one sorted list, in-place ($O(1)$ space) |
| `demo` | function | Runs all three operations with printed output and an assertion check | 

## Implemented Operations

### 1. Reverse

Reverses the list in-place by writing `next` pointers $\textemdash$ no auxiliary data structure needed. 

```python
 Before:  5 -> 3 -> 8 -> 1 -> 6
  After:  6 -> 1 -> 8 -> 3 -> 5
```
#### Complexity: 

  * Time  - $O(n)$
  * Space - $O(1)$

The algorithm keeps three pointers (`previous`, `current`, `next_node`) and iterates once through the list, flipping each link direction. 

### 2. Insertion Sort 

Sorts the list in-place using insertion sort $\textemdash$ each node is removed from the original chain and re-inserted at the correct position in a growing sorted sub-list.

```python
 Before:  7 -> 2.5 -> 9 -> 4.1 -> 1 -> 6
  After:  1 -> 2.5 -> 4.1 -> 6 -> 7 -> 9
```

#### Complexity: 
  * Time  - $O(n^2)$
  * Space - $O(1)$

Chosen for its simplicity and constant space usage. For large lists, merge sort $(O(n \space \log{} n))$ would be preferable $\textemdash$ insertion sort is practical here given typical interview/homework list sizes.

### 3. Merge Two Sorted Lists

Merges two already-sorted linked lists into a single sorted list without allocating new nodes $\textemdash$ only pointers are reassigned.

```python
 A:      1 -> 4 -> 7 -> 11
 B:      2 -> 5 -> 8 -> 10 -> 14
 Merged: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10 -> 11 -> 14
```

#### Complexity: 
  * Time  - $O(n + m)$
  * Space - $O(1)$

Uses a dummy sentinel node to simplify edge-case handling at the head, then appends the remaining non-exhausted list in $O(1)$.

## Type Safety 

`Node` enforces numeric-only input at construction time. Booleans are explicitly rejected despite being a subclass of `int` in Python.

```python
l_list = LinkedList()    # TypeError
l_list.append("hello")   # TypeError 
l_list.append([1, 2])    # TypeError
l_list.append(None)      # TypeError
l_list.append(True)      # TypeError
l_list.append(3.14)      # OK
l_list.append(42)        # OK
```

## Running

No dependencies beyond the Python standard library.

```bash
python t01_linkedlist.py
```

## Expected output: 

```python

 ~~~~~  LINKED LIST  ~~~~~

Reverse a LinkedList --------------------------------
 Before:  5 -> 3 -> 8 -> 1 -> 6
  After:  6 -> 1 -> 8 -> 3 -> 5

Insertion sorting -----------------------------------
 Before:  7 -> 2.5 -> 9 -> 4.1 -> 1 -> 6
  After:  1 -> 2.5 -> 4.1 -> 6 -> 7 -> 9

Sorted LinkedLists Merge ----------------------------
  A:      1 -> 4 -> 7 -> 11
  B:      2 -> 5 -> 8 -> 10 -> 14
  Merged: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10 -> 11 -> 14

Data type validation --------------------------------
  [OK]   String → Node accept only integers or float.Received type: "'str'"
  [OK]   List   → Node accept only integers or float.Received type: "'list'"
  [OK]   None   → Node accept only integers or float.Received type: "'NoneType'"
  [OK]   bool   → Node accept only integers or float.Received type: "'bool'"
```

## Design Notes 

* No external libraries $\textemdash$ pure Python, zero dependencies.
* `_sorted_insert` is module-level, not a method, to keep `LinkedList` focused on list-level concerns and make the helper independently testable.
* `merge_sorted` operates on `Node` references, not `LinkedList` objects $\textemdash$ intentional, to keep the function generic and composable.
* Boolean rejection is explicit (`isinstance(data, bool)` check before the numeric check) because `bool` is a subclass of `int` in Python and would otherwise pass silently.


# Task 02 $\textemdash$ Recursion: Pythagoras Tree Fractal

A Python implementation of the Pythagoras Tree fractal using recursion, `turtle` for rendering, and `tkinter` for an interactive GUI.

## Overview 

The **Pythagoras Tree** is a plane fractal constructed from squares. Each square spawns two smaller squares rotated at a user-defined angle, forming a self-similar branching structure that resembles a tree. The construction is inherently recursive: every branch is a smaller copy of the whole.

This implementation exposes the recursion depth and several visual parameters through an interactive control panel, allowing real-time exploration of how the fractal behaves at different configurations.

## Features 

* **Pure recursive drawing** $\textemdash$ `draw_branch()` calls itself for the left and right child branches, terminating when the maximum depth is reached or the branch length drops below 1 px.
* **Adjustable recursion depth** $\textemdash$ slider from 1 to 15 levels.
* **Configurable branch angle** $\textemdash$ controls the spread between child branches $(5\degree – 85\degree)$.
* **Configurable scale ratio** $\textemdash$ how much each child branch shrinks relative to its parent $(0.50–0.90)$.
* **Configurable trunk length** $\textemdash$ base branch length in pixels $(60–250)$.
* **Colour gradient** $\textemdash$ branches transition from dark brown (trunk) to green (leaves) based on current depth.
* **Adaptive line width** $\textemdash$ thicker near the root, thinner toward the tips.
* **Presets** $\textemdash$ four named configurations (Classic, Symmetrical, Asymmetrical, Wide) for quick exploration.
* **Performance feedback** $\textemdash$ displays total branch count and rendering time after each draw.

## Project Structure
```bash
└── t02_pythagoras_tree.py   # Single-file implementation
```

## Requirements

* Python 3.8+
* Standard library only: `turtle`, `tkinter`, `math`, `time`

No external dependencies are required.

## Usage
```bash
python t02_pythagoras_tree.py
```
The GUI opens with the control panel on the left and the canvas on the right. Adjust any slider and click Draw a Tree, or pick a preset to render immediately.

## Expected output: 

<img width="942" height="659" alt="image" src="https://github.com/user-attachments/assets/f5a4da22-a44e-4c1f-aa04-0dffebe7e57f" />

## Implementation Details

### Core recursive function
```python
def draw_branch(t: turtle.Turtle,
                x: float, y: float,
                length: float, angle: float,
                depth: int, max_depth: int,
                branch_angle: float, ratio: float) -> int:

    # Draw current branch 
    left  = draw_branch(t, x2, y2, length * ratio, angle - branch_angle,
                        depth + 1, max_depth, branch_angle, ratio)
    right = draw_branch(t, x2, y2, length * ratio, angle + branch_angle,
                        depth + 1, max_depth, branch_angle, ratio)
    return 1 + left + right
```
### At each call the function:
1. Checks the base case $\textemdash$ stops if `depth > max_depth` or the branch is too short to be visible.
2. Computes the endpoint of the current branch using trigonometry.
3. Draws the segment and recurses into two children, each rotated by `branch_angle` and scaled by `ratio`.
4. Returns the total count of branches drawn (useful for performance logging).

### Complexity
| Depth | Max branches $(2^d)$ |
| --- | --- |
| 5 | 63 | 
| 8 | 511 |
| 10 | 2,047 | 
| 12 | 8,191 | 
| 15 | 65,535 |

Rendering is fast for depth $\leq 12$; at depth $15$ the branch count approaches $65 k$, which may take a few seconds depending on hardware. The app warns the user when the estimated count exceeds $50,000$.

Animation is disabled (`screen.tracer(0)`) and the canvas is updated in a single flush after all recursion completes, which keeps rendering time minimal.

### Example Configurations
| Preset | Depth | Angle | Ration | Trunk |
| --- | --- | --- | --- | --- |
| Classic | 8 | $45\degree$ | 0.70 | 130 |
| Symmetrical | 9 | $30\degree$ | 0.72 | 120 |
| Asymmetrical | 9 | $55\degree$ | 0.65 | 110 |
| Wide | 6 | $65\degree$ | 0.75 | 140 |

## Key Concepts Demonstrated
* **Recursion as a design pattern** $\textemdash$ the fractal structure maps directly onto the call stack; no explicit stack or loop is needed.
* **Base-case design** $\textemdash$ two independent termination conditions (`depth` and `length`) prevent infinite recursion and unnecessary work on imperceptibly small branches.
* **Parametric fractals** $\textemdash$ small changes to `branch_angle` and `ratio` produce visually distinct trees, illustrating sensitivity to initial conditions.
* **Separation of concerns** $\textemdash$ drawing logic (`draw_branch`) is fully decoupled from the GUI (`PythagorasTreeApp`), making the core algorithm easy to test or reuse independently.

# Task 03 $\textemdash$ Dijkstra's Shortest Path Algorithm: Binary Min-Heap Implementation

## Overview

This project implements Dijkstra's single-source shortest path algorithm from scratch in pure Python, with a custom binary min-heap as the priority queue. The goal is to find the minimum-cost path from one starting vertex to every other reachable vertex in a weighted graph $\textemdash$ a fundamental building block in routing, navigation, network analysis, and operations research.

## Algorithm Explanation

### Core Idea

Dijkstra's algorithm is a greedy, label-correcting procedure. It maintains a set of *finalised vertices* (those whose shortest distance is proven optimal) and a *frontier* priority queue of candidate vertices.

At each step it: 
1. **Extracts** the frontier vertex `u` with the smallest tentative distance.
2. **Relaxes** every outgoing edge `(u -> v, w)`: if `dist[u] + w < dist[v]`, update `dist[v]` and record u as the predecessor of `v`.
3. **Inserts** the updated `(dist[v], v)` into the heap (lazy re-insertion).
4. **Repeats** until the heap is empty or every vertex is finalised.

Because a vertex's distance can only decrease, once it is popped from the min-heap its distance is guaranteed to be optimal $\textemdash$ **provided all edge weights are non-negative**.

### Why a Binary Min-Heap?
| Priority Queue | Extract-Min | Decrease-Key | Overall |
| --- | --- | --- | --- |
| Unsorted array | $O(V)$ | $O(1)$ | $O(V^2)$ | 
| Binary min-heap (lazy) | $O(\log{}V)$ | $O(\log{}V)$ | $O((V + E) \log{}V)$ |
| Fibonacci heap | $O(\log{}V)$ | $O(1)$ amonrtised | $O(E + V \space \log{}V)$ |

For sparse graphs $(E \approx V \space or \space E \approx V \space \log{}V)$ the binary heap is the practical sweet spot: it is cache-friendly, simple to implement correctly, and already built into Python's `heapq` module.

### Lazy Deletion (Decrease-Key Avoidance)

Standard heap implementations require an expensive "decrease-key" operation. This project avoids it with lazy **deletion**:
* When a shorter distance to `v` is found, a new `(new_dist, v)` entry is pushed $\textemdash$ the old one stays in the heap.
* **When a vertex is popped**, it is checked against a `visited` set; stale (superseded) entries are simply discarded.

This trades a small amount of extra heap space for a dramatically simpler implementation with identical asymptotic complexity.

## Complexity

| Metric | Value |
| --- | --- |
| Time | $O((V + E) \log{}V)$ | 
| Space | $O(V + E)$ | 

Where **V** = number of vertices, **E** = number of edges.

## Constraints & Assumptions

* All edge weights must be $\geq 0$. A `ValueError` is raised otherwise (negative weights require Bellman-Ford).
* The graph may be **directed or undirected** $\textemdash$ controlled by the `directed` flag at construction time.
* Vertex identifiers are strings for readability; any hashable type works.
* **Unreachable vertices** receive distance `math.inf`; `path_to()` returns `[]`.

## Usage 

```python
from dijkstra import WeightedGraph, dijkstra

# Build a graph
g = WeightedGraph(directed=False)
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)
g.add_edge("C", "B", 1)
g.add_edge("B", "D", 5)
g.add_edge("C", "D", 8)

# Run the algorithm
result = dijkstra(g, source="A")

# Query results
print(result.distance_to("D"))   # -> 8.0  (A→C→B→D)
print(result.path_to("D"))       # -> ['A', 'C', 'B', 'D']
print(result.summary())          # -> full table of distances & paths
```
### Running the demos

```bash
python t03_dijkstra.py     # Single-file implementation
```

### This executes three built-in demos and a suite of unit tests:

| Demo | Description | 
| --- | --- |
| Demo 1 | Small undirected graph $\textemdash$ textbook example | 
| Demo 2 | Directed graph with multiple competing paths | 
| Demo 3 | Graph containing an isolated, unreachable vertex | 
| Unit tests | Correctness assertions including negative-weight guard | 

### Sample Output 

```
Shortest paths from source 'A'
--------------------------------------------------
  A -> B:     4.00   path: A -> B
  A -> C:     2.00   path: A -> C
  A -> D:     9.00   path: A -> C -> E -> D
  A -> E:     5.00   path: A -> C -> E
  A -> F:    20.00   path: A -> C -> E -> D -> F
```

## Design Decisions

### 1. Lazy insertion over decrease-key

Python's `heapq` is a min-heap but provides no decrease-key primitive. Rebuilding the heap or maintaining a position map would add significant complexity for marginal gain. Lazy insertion keeps the code readable and correct.

### 2. Tie-breaking counter

Heap entries are `(distance, counter, vertex)` tuples. The integer `counter` prevents Python from attempting to compare vertex strings when two distances are equal $\textemdash$ a subtle but important correctness detail.

### 3. Separation of concerns

`WeightedGraph`, `MinHeap`, `DijkstraResult`, and `dijkstra()` are independent classes/functions. This makes each component individually testable and allows swapping the heap implementation (e.g., for a Fibonacci heap) without touching the graph or result logic.

## Potential Extensions 

* **Multi-source Dijkstra** $\textemdash$ initialise all sources with distance 0 simultaneously.
* **Bidirectional Dijkstra** $\textemdash$ run from both source and target, meet in the middle; roughly halves the explored vertices.
* **A\* search** $\textemdash$ add a heuristic to guide expansion toward the target (useful for spatial graphs).
* **Negative-weight** support $\textemdash$ replace with Bellman-Ford or Johnson's algorithm.
* **Visualisation** $\textemdash$ export the predecessor tree as a DOT file for Graphviz rendering.


# Task 04 $\textemdash$ Binary Heap Tree Visualizer

An interactive GUI tool for visualizing binary heaps as trees, built on top of NetworkX and Matplotlib

## Problem Statement 

Binary heaps are typically stored as flat arrays $\textendash$ a compact, cache-friendly structure that underpins priority queues, heap sort, and task scheduling. While efficient in memory, the array form makes it difficult to reason about the tree topology at a glance, particularly when debugging heap construction, verifying the heap property, or communicating algorithmic behavior to others.

The challenge: given an existing codebase that renders arbitrary binary trees from linked `Node` objects, extend it with an interactive GUI that accepts a raw heap array, builds the corresponding tree, validates the heap property, and redraws everything in real time $\textendash$ without modifying the original tree-building infrastructure.

## Architecture Overview

```
┌─────────────────────────────────────────┐
│              launch_gui()               │  <- Interactive layer (Matplotlib widgets)
├─────────────────────────────────────────┤
│  build_heap_tree()   validate_heap()    │  <- Heap logic layer
├─────────────────────────────────────────┤
│         draw_tree()  add_edges()        │  <- Rendering layer
├─────────────────────────────────────────┤
│                 Node                    │  <- Data model
└─────────────────────────────────────────┘
```

Each layer has a single responsibility and no layer reaches downward by more than one level.

## Base Code (unchanged) 

The original codebase provides three components that are preserved verbatim:

`Node` $\textendash$ a linked tree node holding a value, a display color, and a **UUID** (used as the NetworkX node key to avoid collisions when duplicate values appear in the heap).

`add_edges(graph, node, pos, x, y, layer)` $\textendash$ a recursive DFS that populates a `nx.DiGraph` and computes `(x, y)` positions using a layer-aware horizontal offset:

```
x_left  = x_parent − 1 / 2^layer
x_right = x_parent + 1 / 2^layer
```
Each level halves the spread, producing a balanced layout regardless of tree depth.

`draw_tree(tree_root, ax)` $\textendash$ **wraps** `add_edges`, extracts per-node colors and labels, and calls `nx.draw()`. The only change from the original signature is the addition of an `ax` parameter so the function draws onto a caller-supplied `Axes` object rather than creating a new figure $\textendash$ this is the minimal change required to support GUI redraws.

## New Components

`build_heap_tree(heap)`
Constructs a linked `Node` tree from a heap array using the standard index arithmetic:

| Relationship | Formula |
| --- | --- |
| Left child | `2 * i + 1` |
| Right child | `2 * i + 2` | 
| Parent | `(i - 1) // 2` | 

### Two-pass approach:

```python
# Pass 1 -- instantiate all nodes, preserving index-to-node mapping
nodes = [Node(val, color=node_color(i)) for i, val in enumerate(heap)]

# Pass 2 -- wire left/right pointers using heap index arithmetic
for i, node in enumerate(nodes):
    left_idx, right_idx = 2 * i + 1, 2 * i + 2
    if left_idx  < len(nodes): node.left  = nodes[left_idx]
    if right_idx < len(nodes): node.right = nodes[right_idx]
```
Creating all nodes first and linking in a second pass avoids forward-reference issues and keeps both passes linear and readable. The function returns `nodes[0]` $\textendash$ the root $\textendash$ which is passed directly to `draw_tree`.

### Node colors encode structural role:

| Color | Role |
| --- | --- |
| Sky blue | Root (index 0) |
| Light green | Left children (odd indices) |
| Light salmon | Right children (even indices > 0) | 


`validate_heap(heap, heap_type)`
Walks the array once and checks every parent-child pair against the selected heap property:

```python
for i in range(len(heap)):
    left_idx  = 2 * i + 1
    right_idx = 2 * i + 2
    for child_idx in (left_idx, right_idx):
        if child_idx >= len(heap):
            continue
        if heap_type == "min" and heap[child_idx] < heap[i]:
            return False, (f"Min-heap violated: parent[{i}]={heap[i]} "
                           f"> child[{child_idx}]={heap[child_idx]}")
        if heap_type == "max" and heap[child_idx] > heap[i]:
            return False, (f"Max-heap violated: parent[{i}]={heap[i]} "
                           f"< child[{child_idx}]={heap[child_idx]}")
return True, f"Valid {heap_type}-heap"
```

Returns `(bool, message)` $\textendash$ intentionally decoupled from rendering so it can be unit-tested independently or reused in non-GUI contexts.

`launch_gui()`

Builds the interactive window using `matplotlib.widgets` $\textendash$ no additional GUI framework required. The layout splits the figure into a tree drawing area (top 72%) and a control panel strip (bottom 28%):

```
┌──────────────────────────────────────────────────┐
│                                                  │
│              Tree drawing area                   │
│                  (ax_tree)                       │
│                                                  │
├──────────────────────────────────────────────────┤
│  [Heap array: _________]  Min○ Max○  [Visualize] │
│  Status: Valid min-heap                          │
└──────────────────────────────────────────────────┘
```
### Controls: 
* **TextBox** $\textendash$ comma-separated integer input; also fires on Enter key.
* **RadioButtons** $\textendash$ toggles between Min-heap and Max-heap validation mode
* **Button** $\textendash$ triggers a full redraw of the tree.
* **Status bar** $\textendash$ shows validation result in green (valid) or red (violated), with the exact parent-child indices that break the property when invalid.
* **Legend** $\textendash$ static color key rendered in its own `Axes` panel.

The `render()` callback clears `ax_tree`, rebuilds the tree from scratch, redraws, and updates the status bar. Using `fig.canvas.draw_idle()` instead of `plt.draw()` ensures redraws are efficient and non-blocking.

## Requirements

```bash
python >= 3.10
networkx
matplotlib
```

### Install dependencies:

```
pip install networkx matplotlib uuid
```

## Usage 

```bash
python t04_heap_tree.py
```

The GUI launches with a default min-heap `[0, 4, 1, 5, 10, 3]` pre-rendered. From there:

1. Type any comma-separated integer array into the text box (e.g. `10, 9, 8, 5, 6, 3, 2`).
2. Select Min-heap or Max-heap from the radio buttons.
3. Press **Visualize** or hit Enter.
4. The tree redraws and the status bar reports whether the heap property holds.

The tool intentionally accepts arrays that violate the heap property $\textendash$ this is useful for debugging insertion errors or inspecting intermediate states during heap construction.

## Default output

<img width="1107" height="778" alt="image" src="https://github.com/user-attachments/assets/302764db-e1ed-4091-a53e-3bf96933d424" />

## Design Decisions 

### Why keep `build_heap_tree` and `validate_heap` separate from the GUI?

Both functions are pure $\textendash$ given the same input they always return the same output, with no dependency on figure state. This makes them independently testable and reusable outside the GUI context (e.g. in a notebook or a script that batch-validates heaps).

### Why `matplotlib.widgets` instead of `Tkinter` or `PyQt`?

The project already depends on Matplotlib for rendering. Using `matplotlib.widgets` adds zero new dependencies while keeping the entire tool in a single file. For a visualization-first tool, this is the right trade-off.

### Why not use `heapq` for validation?

`heapq` only handles min-heaps and mutates the input list. `validate_heap` supports both min and max variants, is non-destructive, and reports the exact index pair that violates the property $\textendash$ information heapq does not provide.

### Why `draw_idle()` instead of `plt.draw()`?

`fig.canvas.draw_idle()` schedules a redraw on the next GUI event loop tick rather than forcing an immediate repaint. This prevents the interface from locking up on larger trees and is the idiomatic approach for Matplotlib interactive applications.



