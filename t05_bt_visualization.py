"""
Task 5: Binary Tree Traversal Visualization
Visualizes DFS (depth-first search) and BFS (breadth-first search) traversals
of a binary tree, coloring nodes from dark to light shades based on visit order.

Key constraints:
- Uses a stack for DFS (no recursion)
- Uses a queue for BFS (no recursion)
- Colors transition from dark (#1296F0 range) to light as traversal progresses
"""
import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Node definition (original from the task + color storage)
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color           # stores the current hex color of the node
        self.id = str(uuid.uuid4())  # unique id for networkx graph

# Color generation: dark -> light gradient
def generate_color_gradient(n: int) -> list[str]:
    """
    Return a list of n hex colors transitioning from dark blue to light blue.
        First color  -> #1296F0  (dark, vivid blue)
        Last color   -> #D6EEFF  (very light blue)
    The interpolation is done linearly in RGB space.
    """
    start = (0x12, 0x96, 0xF0)   # dark blue  (#1296F0)
    end   = (0xD6, 0xEE, 0xFF)   # light blue (#D6EEFF)

    colors = []
    for i in range(n):
        t = i / max(n - 1, 1)    # 0.0 … 1.0
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        colors.append(f"#{r:02X}{g:02X}{b:02X}")

    return colors

# Traversal algorithms (iterative -- no recursion)
def dfs_iterative(root: Node) -> list[Node]:
    """
    Depth-First Search using an explicit stack (pre-order: root -> left -> right).
    Returns nodes in visit order.
    """
    if root is None:
        return []

    visited_order = []
    stack = [root]          # plain list used as a LIFO stack

    while stack:
        node = stack.pop()  # LIFO
        visited_order.append(node)
        # Push right first so that left is processed first (LIFO semantics)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited_order


def bfs_iterative(root: Node) -> list[Node]:
    """
    Breadth-First Search using an explicit queue (level-order traversal).
    Returns nodes in visit order.
    """
    if root is None:
        return []

    visited_order = []
    queue = deque([root])   # deque used as a FIFO queue

    while queue:
        node = queue.popleft()  # FIFO
        visited_order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited_order

# Graph construction (adapted from original task code)
def add_edges(
        graph: nx.DiGraph, 
        node: Node, 
        pos: dict,
        x: float = 0, 
        y: float = 0, 
        layer: int = 1
    ) -> nx.DiGraph:
    """
    Recursively (graph-building only, not traversal) adds edges/positions
    to a networkx DiGraph. This mirrors the original helper from the task.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            lx = x - 1 / 2 ** layer
            pos[node.left.id] = (lx, y - 1)
            add_edges(graph, node.left, pos, x=lx, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            rx = x + 1 / 2 ** layer
            pos[node.right.id] = (rx, y - 1)
            add_edges(graph, node.right, pos, x=rx, y=y - 1, layer=layer + 1)
    return graph

# Drawing helper
def draw_tree(tree_root: Node, title: str = "Tree") -> None:
    """
    Draw the binary tree using the current .color attribute of each node.
    """
    graph = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    graph = add_edges(graph, tree_root, pos)

    colors = [node[1]["color"] for node in graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in graph.nodes(data=True)}

    ax = plt.gca()
    nx.draw(
        graph, pos=pos, labels=labels, arrows=False,
        node_size=2500, node_color=colors, ax=ax,
        font_size=12, font_weight="bold", font_color="white",
    )
    ax.set_title(title, fontsize=14, fontweight="bold", pad=15)

# Main visualization: side-by-side DFS vs BFS
def visualize_traversals(root: Node) -> None:
    """
    Paint both DFS and BFS traversals and show them side by side.
    For each algorithm:
      1. Determine visit order (iterative, no recursion).
      2. Generate a colour gradient with as many colours as nodes.
      3. Assign colour[i] to the i-th visited node.
      4. Draw the tree.
    """
    # DFS
    dfs_order = dfs_iterative(root)
    dfs_colors = generate_color_gradient(len(dfs_order))
    for node, color in zip(dfs_order, dfs_colors):
        node.color = color
    # BFS
    bfs_order = bfs_iterative(root)
    bfs_colors = generate_color_gradient(len(bfs_order))
    # We need a second pass so BFS colouring doesn't overwrite DFS on the same node objects.
    # Store BFS colors separately, then apply per-subplot.
    bfs_color_map = {node.id: color for node, color in zip(bfs_order, bfs_colors)}
    # Figure layout
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle(
        "Binary Tree Traversal Visualization\n"
        "(darker = visited earlier  ->  lighter = visited later)",
        fontsize=15, fontweight="bold", y=1,
    )

    # Subplot 1: DFS
    plt.sca(axes[0])
    # Colors already set on node.color from dfs pass
    draw_tree(root, title="DFS -- Depth-First Search\n(stack, pre-order)")
    # Print visit order to console
    print("DFS visit order:", [n.val for n in dfs_order])

    # Apply BFS colors before drawing subplot 2
    def _apply_bfs_colors(node):
        if node is None:
            return
        node.color = bfs_color_map[node.id]
        _apply_bfs_colors(node.left)
        _apply_bfs_colors(node.right)

    _apply_bfs_colors(root)

    # Subplot 2: BFS
    plt.sca(axes[1])
    draw_tree(root, title="BFS -- Breadth-First Search\n(queue, level-order)")

    print("BFS visit order:", [n.val for n in bfs_order])

    # Shared colour-scale legend
    n_legend = 6
    legend_colors = generate_color_gradient(n_legend)
    patches = [
        mpatches.Patch(color=c, label=f"Step {i + 1}" if i == 0 else
                        (f"Step {n_legend}" if i == n_legend - 1 else ""))
        for i, c in enumerate(legend_colors)
    ]
    fig.legend(
        handles=patches,
        title="Visit order  (dark -> light)",
        loc="lower center",
        ncol=n_legend,
        frameon=True,
        fontsize=9,
        title_fontsize=10,
        bbox_to_anchor=(0.5, -0.08),
    )

    plt.tight_layout()
    plt.show()

# Entry point
if __name__ == "__main__":
    # Build the tree from the task specification
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    visualize_traversals(root)