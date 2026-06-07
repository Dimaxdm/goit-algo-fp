import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
from matplotlib.patches import FancyBboxPatch

# Variable: Tree 
TREE_INITIALE: str = "0, 4, 1, 5, 10, 3" # Creating Example Tree from the Original base code
"""
TREE_INITIALE = 
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
"""

# Original base code -- provided in the Problem Statement to The Task:
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the node color
        self.id = str(uuid.uuid4())  # Unique identifier for each node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Use id and store node value
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, ax):
    """
    Draws the binary tree onto the provided Matplotlib Axes object.
    Parameters:
        tree_root : Node  -- root of the tree to render
        ax        : Axes  -- target axes (supports embedded GUI redraws)
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Use node value for labels
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, ax=ax)

# Implemented Heap construction as solution to the Task:
def build_heap_tree(heap: list) -> Node:
    """
    Builds a binary tree from an array representation of a heap.
    Binary heap array property:
        For a node at index i:
            left child  -> index  2*i + 1
            right child -> index  2*i + 2
            parent      -> index  (i - 1) // 2
    Parameters:
        heap : list
            Array of values in level-order (standard binary heap representation).
    Returns:
        Node | None
            Root of the constructed tree, or None for an empty array.
    """
    if not heap:
        return None

    # 1. Create all nodes at once — assign color by role in the heap
    def node_color(index: int) -> str:
        if index == 0:
            return "skyblue"        # root
        return "lightgreen" if index % 2 == 1 else "lightsalmon"

    nodes = [Node(val, color=node_color(i)) for i, val in enumerate(heap)]

    # 2. Link parents to children according to the heap array structure
    for i, node in enumerate(nodes):
        left_idx  = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx  < len(nodes):
            node.left  = nodes[left_idx]
        if right_idx < len(nodes):
            node.right = nodes[right_idx]

    return nodes[0]   # root is always the first element of the array


def validate_heap(heap: list, heap_type: str) -> tuple[bool, str]:
    """
    Checks whether the array satisfies the heap property.
        Parameters
            heap      : list  -- values to validate
            heap_type : str   -- "min" or "max"
    Returns:
        (valid: bool, message: str)
    """
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

# Interactive GUI implementation
def launch_gui() -> None:
    """
    Launches an interactive Matplotlib GUI for binary heap visualization.
    Controls
    - Text box   : enter a comma-separated heap array
    - Radio btns : choose Min-heap or Max-heap type for validation
    - Button     : render / refresh the tree
    """
    # layout
    fig = plt.figure(figsize=(11, 7))
    fig.patch.set_facecolor("#f7f9fc")

    # Tree drawing area (top portion of the figure)
    ax_tree = fig.add_axes([0.05, 0.22, 0.90, 0.72])
    ax_tree.set_facecolor("#1c5ec2")
    ax_tree.set_title("Binary Heap Visualizer", fontsize=14, fontweight="bold", pad=12)

    # Control panel strip at the bottom
    ax_input  = fig.add_axes([0.05, 0.10, 0.50, 0.06])   # text input
    ax_radio  = fig.add_axes([0.60, 0.06, 0.14, 0.12])   # min / max toggle
    ax_button = fig.add_axes([0.78, 0.08, 0.16, 0.08])   # render button
    ax_status = fig.add_axes([0.05, 0.02, 0.90, 0.05])   # status bar
    ax_status.axis("off")

    # widgets
    text_box = widgets.TextBox(
        ax_input,
        label="Heap array: ",
        initial=TREE_INITIALE,
        textalignment="left",
    )

    radio = widgets.RadioButtons(
        ax_radio,
        labels=["Min-heap", "Max-heap"],
        active=0,
    )

    button = widgets.Button(
        ax_button,
        label="Visualize",
        color="#4a90d9",
        hovercolor="#357abd",
    )
    button.label.set_color("white")
    button.label.set_fontweight("bold")

    status_text = ax_status.text(
        0.5, 0.2, "Enter a comma-separated array and press Visualize.",
        ha="center", va="center", fontsize=12,
        color="#555555", transform=ax_status.transAxes,
    )

    # legend (static)
    legend_ax = fig.add_axes([0.01, 0.80, 0.10, 0.13])
    legend_ax.axis("off")
    legend_ax.set_facecolor("#f7f9fc")
    for y, color, label in [(0.75, "skyblue", "Root"),
                            (0.42, "lightgreen", "Left child (odd idx)"),
                            (0.09, "lightsalmon", "Right child (even idx)")]:
        legend_ax.add_patch(plt.Circle((0.08, y), 0.08, color=color,
                                       transform=legend_ax.transAxes, clip_on=False))
        legend_ax.text(0.20, y, label, va="center", fontsize=8,
                       transform=legend_ax.transAxes, color="#333333")

    # render callback
    def render(_event=None) -> None:
        raw = text_box.text.strip()
        # Parse input
        try:
            heap = [int(x.strip()) for x in raw.split(",") if x.strip()]
        except ValueError:
            status_text.set_text("⚠ Invalid input — use integers separated by commas.")
            status_text.set_color("#c0392b")
            fig.canvas.draw_idle()
            return

        if not heap:
            status_text.set_text("⚠ Array is empty.")
            status_text.set_color("#c0392b")
            fig.canvas.draw_idle()
            return

        # Determine selected heap type
        heap_type = "min" if radio.value_selected == "Min-heap" else "max"

        # Build and draw
        ax_tree.clear()
        ax_tree.set_facecolor("#f7f9fc")
        ax_tree.set_title("Binary Heap Visualizer", fontsize=14,
                          fontweight="bold", pad=12)

        root = build_heap_tree(heap)
        draw_tree(root, ax=ax_tree)

        # Annotate array indices below each node (informational)
        ax_tree.set_xlabel(
            f"Array: {heap}",
            fontsize=9, color="#666666", labelpad=6,
        )

        # Validate and update status bar
        valid, message = validate_heap(heap, heap_type)
        status_text.set_text(message)
        status_text.set_color("#27ae60" if valid else "#c0392b")

        fig.canvas.draw_idle()
    button.on_clicked(render)
    text_box.on_submit(render)   # also fires on Enter key
    # Render the default example immediately on startup
    render()
    plt.show()

# Enter point
if __name__ == "__main__":
    launch_gui()