"""
The Pythagoras' Tree fractal -> a recursive implementation in Python.
`turtle` used for drawing and `tkinter` for GUI controls.
"""
import turtle
import tkinter as tk
from tkinter import ttk
import math
import time

# Variables
RECURSION_DEPTH = 15

# Drawning Recursive function 
def draw_branch(t: turtle.Turtle,
                x: float, y: float,
                length: float, angle: float,
                depth: int, max_depth: int,
                branch_angle: float, ratio: float) -> int:
    """
    Recursively draws a branch of the Pythagoras tree.

    Parameters:
        t            -> Turtle objects
        x, y         -> the coordinates of the branch's base
        length       -> the current branch length
        angle        -> angle direction (in degrees, where 0 is upwards)
        depth        -> current recursive depth
        max_depth    -> recursion maximum depth 
        branch_angle -> left/right branching angle
        ratio        -> length reduction ratio 
        base_r/g/b   -> base color of the trunk

    Return quantity of drawning branches
    """
    if depth > max_depth or length < 1:
        return 0

    # The thickness of the line depends on the depth
    line_width = max(0.5, (max_depth - depth + 1) * 1.5)
    t.pensize(line_width)

    # Colour: ranging from dark brown to green as the depth increases
    t_ratio = depth / max_depth if max_depth > 0 else 1
    r = int(130 - t_ratio * 80)
    g = int(60  + t_ratio * 100)
    b = int(20)
    t.pencolor(r / 255, g / 255, b / 255)

    # Calculating the end point of the branch
    rad = math.radians(angle)
    x2 = x + length * math.sin(rad)
    y2 = y + length * math.cos(rad)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x2, y2)

    # Recursion: left and right branch
    left  = draw_branch(t, x2, y2, length * ratio, angle - branch_angle,
                        depth + 1, max_depth, branch_angle, ratio)
    right = draw_branch(t, x2, y2, length * ratio, angle + branch_angle,
                        depth + 1, max_depth, branch_angle, ratio)

    return 1 + left + right


class PythagorasTreeApp:
    """A Tkinter application with a Turtle canvas for displaying the Pythagoras tree."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Pythagoras Tree - Fractal")
        self.root.resizable(True, True)

        self._build_ui()
        self._setup_turtle()
        self.draw()

    # Interface building
    def _build_ui(self) -> None:
        # Control panel on the left 
        ctrl = ttk.Frame(self.root, padding=12)
        ctrl.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Label(ctrl, text="The Pythagoras' Tree",
                  font=("Helvetica", 14, "bold")).pack(pady=(0, 16))

        # Recursion depth
        self.depth_var = tk.IntVar(value=8)
        self._slider(ctrl, "Recursion depth", self.depth_var, 1, RECURSION_DEPTH)

        # Branch agle
        self.angle_var = tk.DoubleVar(value=45.0)
        self._slider(ctrl, "Angle", self.angle_var, 5, 85, resolution=1)

        # Branch scale factor 
        self.ratio_var = tk.DoubleVar(value=0.70)
        self._slider(ctrl, "Branch scale factor", self.ratio_var,
                     0.50, 0.90, resolution=0.01)

        # Branch lenght
        self.trunk_var = tk.IntVar(value=152)
        self._slider(ctrl, "Branch lenght", self.trunk_var, 60, 250)

        ttk.Separator(ctrl).pack(fill=tk.X, pady=10)

        # Presets
        ttk.Label(ctrl, text="Presets", font=("Helvetica", 12, "bold")).pack(anchor=tk.W)
        presets = [
            ("Classic",      8, 45, 0.70, 130),
            ("Symmetrical",  9, 30, 0.72, 120),
            ("Asymmetrical", 9, 55, 0.65, 110),
            ("Wide",         6, 65, 0.75, 140),
        ]
        for name, d, a, r, tr in presets:
            ttk.Button(ctrl, text=name,
                       command=lambda _d=d, _a=a, _r=r, _t=tr: self._apply_preset(_d, _a, _r, _t)
                       ).pack(fill=tk.X, pady=2)

        ttk.Separator(ctrl).pack(fill=tk.X, pady=10)

        ttk.Button(ctrl, text="Draw a Tree",
                   command=self.draw).pack(fill=tk.X, pady=4)

        # Status string
        self.status_var = tk.StringVar(value="Done")
        ttk.Label(ctrl, textvariable=self.status_var,
                  foreground="gray", font=("Helvetica", 9)).pack(pady=(8, 0))

    def _slider(self, parent, label: str, var, from_, to,
                resolution: float = 1) -> None:
        """Alternative method: label + slider + value display."""
        frm = ttk.Frame(parent)
        frm.pack(fill=tk.X, pady=4)

        ttk.Label(frm, text=label, width=18, anchor=tk.W).pack(side=tk.LEFT)
        val_lbl = ttk.Label(frm, width=5, anchor=tk.E)
        val_lbl.pack(side=tk.RIGHT)

        def _update(v):
            if resolution < 1:
                val_lbl.config(text=f"{float(v):.2f}")
            else:
                val_lbl.config(text=str(int(float(v))))

        s = ttk.Scale(parent, from_=from_, to=to,
                      orient=tk.HORIZONTAL, variable=var, command=_update)
        s.pack(fill=tk.X, pady=(0, 2))
        _update(var.get())

    # Turtle
    def _setup_turtle(self) -> None:
        canvas_frame = ttk.Frame(self.root)
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk_canvas = tk.Canvas(canvas_frame, width=700, height=620, bg="white")
        tk_canvas.pack(fill=tk.BOTH, expand=True)

        self.screen = turtle.TurtleScreen(tk_canvas)
        self.screen.tracer(0)   # turn off the animation for faster result

        self.t = turtle.RawTurtle(self.screen)
        self.t.hideturtle()
        self.t.speed(0)

    # Drawning method
    def draw(self) -> None:
        depth      = int(self.depth_var.get())
        angle      = float(self.angle_var.get())
        ratio      = float(self.ratio_var.get())
        trunk_len  = int(self.trunk_var.get())

        # Drawning duration notation 
        est_branches = sum(2**i for i in range(depth + 1))
        if est_branches > 50_000:
            self.status_var.set(f"drawning ~{est_branches:,} branches…")
            self.root.update()

        self.screen.bgcolor("white")
        self.t.clear()

        t0 = time.perf_counter()
        count = draw_branch(
            self.t,
            x=0, 
            y=-280,
            length=trunk_len,
            angle=0,
            depth=0, 
            max_depth=depth,
            branch_angle=angle,
            ratio=ratio,
        )
        self.screen.update()
        elapsed = time.perf_counter() - t0

        self.status_var.set(
            f"Branches: {count:,}  | Time: {elapsed:.2f} с"
        )

    def _apply_preset(self, d, a, r, tr) -> None:
        self.depth_var.set(d)
        self.angle_var.set(a)
        self.ratio_var.set(r)
        self.trunk_var.set(tr)
        self.draw()


# Entry point
def main() -> None:
    root = tk.Tk()
    app = PythagorasTreeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()