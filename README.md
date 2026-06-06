# Task 01 $\textemdash$ Singly Linked List: Reverse, Sort, Merge

A focused Python implementation of a singly linked list covering three classic operations: reversal, insertion sort, and merging two sorted lists. The implementation is numerically typed and includes input validation and a self-contained demo.

## Structure (Related to Task 01)

```
...
└── t01_linkedlist.py          # Node, LinkedList, helpers, and demo
```

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

## Project Structure (Related to Task 02)

```
...
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

### Design Decisions 

#### Why keep `build_heap_tree` and `validate_heap` separate from the GUI?

Both functions are pure $\textendash$ given the same input they always return the same output, with no dependency on figure state. This makes them independently testable and reusable outside the GUI context (e.g. in a notebook or a script that batch-validates heaps).

#### Why `matplotlib.widgets` instead of `Tkinter` or `PyQt`?

The project already depends on Matplotlib for rendering. Using `matplotlib.widgets` adds zero new dependencies while keeping the entire tool in a single file. For a visualization-first tool, this is the right trade-off.

#### Why `draw_idle()` instead of `plt.draw()`?

`fig.canvas.draw_idle()` schedules a redraw on the next GUI event loop tick rather than forcing an immediate repaint. This prevents the interface from locking up on larger trees and is the idiomatic approach for Matplotlib interactive applications.


# Task 05 $\textemdash$ Binary Tree Traversal Visualization

A Python program that visually demonstrates **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** traversals of a binary tree, with node colours shifting from dark $\rightarrow$ light to reflect the order in which each node is visited.

### Output Preview 

| DFG (Stack) | BFS (Queue) | 
| --- | --- |
| Nodes coloured in pre-order | Nodes coloured level by level | 

The figure renders both traversals side by side with a shared colour legend.

### Tree Structure

<img width="1246" height="758" alt="image" src="https://github.com/user-attachments/assets/cc85dbd5-1179-4699-9ead-0cbfcb8c295a" />

#### Node visit sequences: 
* **DFS:** `0 -> 4 -> 5 -> 10 -> 1 -> 3`
* **BFS:** `0 -> 4 -> 1 -> 5 -> 10 -> 3`

### Features
* **Iterative DFS** via an explicit stack (LIFO) $\textendash$ no recursion.
* **Iterative BFS** via an explicit queue (`collections.deque`, FIFO) $\textendash$ no recursion.
* **Hex-colour gradient** from `#1296F0` (dark blue, visited first) to `#D6EEFF` (light blue, visited last).
* Each node receives a **unique colour** that encodes its position in the traversal sequence.
* Side-by-side matplotlib figure for direct comparison

### Requirements

| Package | Purpose |
| --- | --- | 
| `networkx` | Graph construction & layout | 
| `matplotlib` | Rendering & saving the figure | 

#### Install with

```bash
pip install networkx matplotlib uuid
```

### Usage

```bash
python t05_bt_visualization.py
```
### Console output:

```
DFS visit order: [0, 4, 5, 10, 1, 3]
BFS visit order: [0, 4, 1, 5, 10, 3]
```
### Code Architecture

```
t05_bt_visualization.py
│
├── Node                      # Binary tree node (val, left, right, color, id)
│
├── generate_color_gradient() # Produces n hex colours from dark→light
│
├── dfs_iterative()           # Pre-order DFS using a stack []
├── bfs_iterative()           # Level-order BFS using deque()
│
├── add_edges()               # Builds networkx DiGraph with positions
├── draw_tree()               # Renders a single tree subplot
│
└── visualize_traversals()    # Orchestrates both traversals & saves figure
```

Key implementation decisions
#### DFS with an explicit stack

```python
stack = [root]          # plain list used as a LIFO stack
while stack:
    node = stack.pop()  # LIFO
    visited_order.append(node)
    if node.right:
        stack.append(node.right)
    if node.left:
        stack.append(node.left)
```

#### BFS with an explicit queue

```python
queue = deque([root])   # deque used as a FIFO queue
while queue:
    node = queue.popleft()  # FIFO
    visited_order.append(node)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
```

#### Colour gradient

```python
start = (0x12, 0x96, 0xF0)   # #1296F0  dark blue
end   = (0xD6, 0xEE, 0xFF)   # #D6EEFF  light blue

t = i / (n - 1)              # linear interpolation in RGB space
color = f"#{R:02X}{G:02X}{B:02X}"
```

## Algorithm Comparison

| Property | DFS (stack) | BFS (queue) | 
| --- | --- | --- | 
| Data structure | Stack `[]` | Queue `[]` | 
| Traversal style | Pre-order (root -> left -> right) | Level-order |
| Memory usage | $O(h) \textendash \text{tree height}$ | $O(w) \textendash \text{max tree width}$ | 
| Finds shortest path | *NO* | *YES* |
| Explores deep first | *YES* | *NO* |


## Conclusions

1. **Iterative vs recursive traversal** $\textendash$ Both DFS and BFS can be implemented without recursion by making the call stack explicit (a list for DFS, a deque for BFS). This avoids Python's default recursion limit and reduces stack-overflow risk on deep trees.
2. **Visual encoding of traversal order** $\textendash$ Mapping visit order to a colour gradient makes the algorithmic difference between DFS and BFS immediately obvious: DFS dives deep along a branch before backtracking, whereas BFS fans out level by level. What would take paragraphs to explain in prose is self-evident in a single image.
3. **Separation of concerns** $\textendash$ Keeping traversal logic (`dfs_iterative`, `bfs_iterative`), colour generation (`generate_color_gradient`), graph construction (`add_edges`), and rendering (`draw_tree`, `visualize_traversals`) in distinct functions makes each part independently testable and reusable.
4. **Hex-RGB gradient design** $\textendash$ Interpolating linearly in RGB space between two anchor colours produces a perceptually smooth, readable gradient. The dark-to-light direction reinforces the intuition that "darker = older / visited earlier."



# Task 06 $\textemdash$ Food Selection Optimizer $\textendash$ Greedy vs Dynamic Programming

## Problem Statement

Given a menu of food items $\textendash$ each with a fixed cost and calorie count $\textendash$ select a combination that maximises total calories without exceeding a specified budget.

```python
ITEMS = {
    "pizza":     {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog":   {"cost": 30, "calories": 200},
    "pepsi":     {"cost": 10, "calories": 100},
    "cola":      {"cost": 15, "calories": 220},
    "potato":    {"cost": 25, "calories": 350},
}
```
## Algorithms

### Greedy Algorithm 

`greedy_algorithm(items, budget)`
**Core idea**: At every step, pick the item with the highest calorie-to-cost ratio that still fits within the remaining budget.

| Step | Action | 
| --- | --- |
| 1 | Compute `ratio = calories / cost` for every item |
| 2 | Sort items by ratio in descending order | 
| 3 | Iterate: add each item if it fits; skip if it doesn't | 
| 4 | Stop when the budget is exhausted or all items are checked | 

#### Properties

| Property | Value | 
| --- | --- | 
| Time complexity | $O(n \space \log{}n)$ | 
| Space complexity | $O(n)$ | 
| Optimality | Not guaranteed $\textendash$ locally optimal $\neq$ globally optimal |
| Speed | Very fast | 

The greedy approach is a powerful heuristic and often delivers near-optimal results, but it can miss opportunities when a cheaper-but-filling item is rejected early.

### Dynamic Programming

`dynamic_programming(items, budget)`
**Core idea**: Build a 2-D table `dp[i][w]` representing the maximum calories achievable using the first `i` items with budget `w`. Back-track through the table to recover the chosen items.

#### Recurrence 
```python
dp[i][w] = max(
    dp[i-1][w],                          # skip item i
    dp[i-1][w - cost[i]] + cal[i]        # take item i (if cost[i] ≤ w)
)
```
#### Properties

| Property | Value | 
| --- | --- | 
| Time complexity | $O(n \cdot W)$ | 
| Space complexity | $O(n \cdot W)$ | 
| Optimality | Always optimal $\textendash$ exhaustive state-space search | 
| Speed | Slower for large W, but polynomial | 

Where `n` = number of items and `W` = budget cap.

### Usage

```bash
python t06_food_optimizer.py  # No external dependencies required -- pure Python 3.8+
```
## Results (Budget = 100)

### Greedy Algorithm 

| Item | Cost | Calories | Ratio | 
| --- | --- | --- | --- |
| cola | 15 | 220 | 14.67 | 
| potato | 25 | 350 | 14.00 | 
| pepsi | 10 | 100 | 10.00 | 
| hot-dog | 30 | 200 | 6.67 | 
| **TOTAL** | **80** | **870** | $\textendash$ | 

***Budget remaining: 20***

### Dynamic Programming 

| Item | Cost | Calories | 
| --- | --- | --- |
| pizza | 50 | 300 | 
| pepsi | 10 | 100 | 
| cola | 15 | 220 |
| potato | 25 | 350 | 
| **TOTAL** | **100** | **970** |

***Budget remaining: 0***

## Head-to-Head Comparison

| Metric | Greedy | Dynamic Programming | 
| --- | --- | --- | --- |
| Total Calories | 870 | ***970*** |
| Total Cost | 80 | 100 | 
| Items Selected | 4 | 4 | 
| Budget Utilisation | 80% | 100% | 
| Calorie Advantage | $\textemdash$ | +100 kcal | 

## Key Observations

#### 1. The greedy algorithm left 20 units of budget unspent.

It skipped `pizza` (cost 50, ratio 6.00) in favour of cheaper high-ratio items, but never found a suitable item to fill the remaining 20-unit gap.

#### 2. Dynamic programming identified that adding `pizza` was worthwhile

Despite `pizza` having the worst calorie-to-cost ratio in the catalogue, including it unlocked a budget-exhausting combination that yielded 100 extra calories.

#### 3. This is the textbook failure mode of greedy for 0/1 Knapsack.

Greedy is optimal for the *fractional* knapsack (where items can be split). For indivisible items it can under-perform by exactly the kind of margin shown here.

#### 4. Both algorithms agree on the core (`cola`, `potato`, `pepsi`) 
The disagreement is only in the fourth slot, where DP correctly prefers `pizza` over `hot-dog` to maximise budget utilisation.

##  When to Use Each Approach 

| Scenario | Recommended Approach | 
| --- | --- |
| Budget/capacity is very large (millions) | Greedy + heuristics | 
| Need a guaranteed optimal answer | Dynamic Programming | 
| Fractional items allowed | Greedy (always optimal there) | 
| Real-time / embedded systems | Greedy |
| Small-to-medium budget, indivisible items | Dynamic Programming | 

## Conclusions 

This exercise demonstrates why algorithm selection matters beyond raw performance numbers:

* **Greedy** is elegant, intuitive, and fast $\textendash$ an excellent first attempt and often "good enough" in practice.
* **Dynamic Programming** trades memory and computation for a **correctness** guarantee, which is non-negotiable in domains where the optimal solution has real consequences (resource allocation, financial planning, logistics).

The 100-calorie difference found here may seem small, but in scaled, real-world applications the gap between a greedy heuristic and the true optimum can represent significant value $\textendash$ making DP the right tool whenever exact optimality is required and budget `W` is tractable.

# Task 7 $\textemdash$ Monte Carlo Dice Simulation 

## Overview 

This project implements a **Monte Carlo simulation** for the classic two-dice problem. By rolling a pair of fair six-sided dice **1,000,000** times, the program estimates the empirical probability of each possible sum (2–12) and compares the results against the exact analytical values derived from combinatorics.

The core principle of the Monte Carlo method is simple but powerful: the more trials you run, the closer the empirical frequency converges to the true probability — a direct application of the *Law of Large Numbers*.

## Project Structure (Related to Task 07)

```
...
├── t07_rolling_dice_simulation.py        # Core Monte Carlo engine
├── t07_rolling_dice_visualization.py         # Matplotlib chart generator
├── t07_results.json        # Simulation output (generated at runtime)
├── t07_figures/
│   ├── bar_comparison.png   # Monte Carlo vs Analytical bar chart
│   └── deviation_plot.png   # Absolute deviation per sum
└── README.md
```
## How It Works

### Analytical probabilities

When rolling two fair six-sided dice, there are 36 equally likely outcomes $(6 \times 6)$. The number of ways to achieve each sum determines its exact probability:

| Sum | Combinations | Probability |
| --- | --- | --- | 
| 2 | 1 | 2.7778% (1/36) | 
| 3 | 2 | 5.5556% (2/36) | 
| 4 | 3 | 8.3333% (3/36) | 
| 5 | 4 | 11.1111% (4/36) | 
| 6 | 5 | 13.8889% (5/36) | 
| 7 | 6 | 16.6667% (6/36) | 
| 8 | 5 | 13.8889% (5/36) | 
| 9 | 4 | 11.1111% (4/36) | 
| 10 | 3 | 8.3333% (3/36) | 
| 11 | 2 | 5.5556% (2/36) | 
| 12 | 1 | 2.7778% (1/36) | 

Sum 7 is the most probable $\textendash$ it can be rolled in 6 different ways.

### Monte Carlo estimation

```python
counts = {i: 0 for i in range(2, 13)}
for _ in range(1_000_000):
    roll = random.randint(1, 6) + random.randint(1, 6)
    counts[roll] += 1

probabilities = {s: count / 1_000_000 for s, count in counts.items()}
```

Each die roll is drawn from a discrete uniform distribution U{1,6}. After all trials, the relative frequency of each sum converges to its theoretical probability.

### Results

Running 1,000,000 simulations produced the following comparison:

| Sum | Analytical | Monte Carlo | \|Diffrence\| | 
| --- | --- | --- | --- |
| 2 | 2.7778% | 2.8068% | 0.029% |
| 3 | 5.5556% | 5.5336% | 0.022% |
| 4 | 8.3333% | 8.3168% | 0.0165% |
| 5 | 11.1111% | 11.1004% | 0.0107% |
| 6 | 13.8889% | 13.8835% | 0.0054% |
| 7 | 16.6667% | 16.6297% | 0.037% |
| 8 | 13.8889% | 13.9322% | 0.0433% |
| 9 | 11.1111% | 11.1468% | 0.0357% |
| 10 | 8.3333% | 8.2918% | 0.0415% |
| 11 | 5.5556% | 5.5859% | 0.0303% |
| 12 | 2.7778% | 2.7725% | 0.0053% |

#### Maximum deviation: 0.0433% (Sum = 8)
#### Average deviation: 0.0252% 

## Visualizations 

### Bar chart $\textendash$ Monte Carlo vs Analytical: 

<img width="1398" height="690" alt="image" src="https://github.com/user-attachments/assets/2226c6bc-1136-4f7e-aba4-830e3a3b7739" />

### Absolute deviation per sum: 

<img width="1503" height="605" alt="image" src="https://github.com/user-attachments/assets/bac07f12-5559-4915-ac02-6a2db48f5317" />

## How to Run 

### Prerequisites 

```bash
pip install matplotlib
```

### Step 1 $\textendash$ Run the simulation 

```bash
python t07_rolling_dice_simulation.py
```

This generates `t07_results.json` with empirical and analytical probabilities. 

### Step 2 $\textendash$ Generate charts 

```bash
python t07_rolling_dice_visualization.py
```

Charts are saved to `t07_figures/`.

### Configuration

Open `t07_rolling_dice_simulation.py` and adjust the constants at the top:

```python
NUM_SIMULATIONS = 1_000_000  # Increase for higher precision
RANDOM_SEED = 42             # Set an integer for reproducible runs
```

## Key Findings & Conclusions

#### 1. The Law of Large Numbers in practice

With 1,000,000 simulations, every sum achieves a deviation of **less than 0.044%** from the theoretical value. This is the Monte Carlo method at its best $\textemdash$ simple random sampling converges to the true distribution as trial count grows.

#### 2. Convergence quality

| Deviation band | Sums | 
| --- | --- | 
| < 0.01% (excellent) | Sums 6, 12 |
| 0.01 - 0.05% (good) | Sums 1-5, 7-11 | 
| 0.05 - 0.10% (notable) | $\textendash$ |

Sum 8 shows the largest absolute deviation, but relative to its probability (13.93%) the error is only ~0.037% $\textendash$ well within acceptable bounds.

#### 3. Symmetry preserved

The simulated distribution maintains the expected triangular symmetry around sum 7. This validates that Python's `random.randint` produces an unbiased uniform distribution.

#### 4. Scalability of the approach

| Simulations | Expected max deviation | 
| 10,000 | ~0.5% |
| 100,000 | ~0.2% |
| 1,000,000 | ~0.06% | 
| 10,000,000 | ~0.02% |

Doubling precision requires roughly 100× more simulations $\textendash$ a classic O(1/√n) convergence rate.

#### 5. Broader applicability

While the two-dice problem has a trivial analytical solution, the Monte Carlo method shines for problems where closed-form answers are intractable: pricing options, simulating particle physics, optimising logistics networks, or estimating high-dimensional integrals. This exercise demonstrates its core mechanics in the simplest possible setting.

## Technologies
* **Python 3.12** $\textendash$ simulation engine
* **random (stdlib)** $\textendash$ uniform random number generation
* **json (stdlib)** $\textendash$ result persistence
* **matplotlib 3.x** $\textendash$ chart generation
