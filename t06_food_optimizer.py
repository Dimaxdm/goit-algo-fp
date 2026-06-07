"""
Food Selection Optimizer
Solves the food selection problem using two approaches:
  1. Greedy Algorithm    -- maximizes calorie/cost ratio iteratively
  2. Dynamic Programming -- finds the globally optimal solution
"""
from typing import Dict, Tuple

# Dataset
ITEMS: Dict[str, Dict[str, int]] = {
    "pizza":     {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog":   {"cost": 30, "calories": 200},
    "pepsi":     {"cost": 10, "calories": 100},
    "cola":      {"cost": 15, "calories": 220},
    "potato":    {"cost": 25, "calories": 350},
}

# Greedy Algorithm
def greedy_algorithm(
    items: Dict[str, Dict[str, int]],
    budget: int,
) -> Tuple[list, int, int]:
    """
    Select food items greedily by the best calorie-to-cost ratio.
    Strategy
        At each step choose the item with the highest calories/cost ratio 
        that still fits within the remaining budget. This is a classic
        greedy heuristic -- fast (O(n log n)) but not guaranteed to be globally optimal.
    Parameters:
        items  : dict  -- food catalogue {name: {cost, calories}}
        budget : int   -- maximum total spend (same currency unit as costs)
    Returns:
        selected : list of item names chosen
        total_cost     : int -- sum of costs for selected items
        total_calories : int -- sum of calories for selected items
    """
    # Sort by calorie-per-unit-cost descending
    ranked = sorted(
        items.items(),
        key=lambda kv: kv[1]["calories"] / kv[1]["cost"],
        reverse=True,
    )

    selected: list = []
    remaining = budget
    total_calories = 0
    total_cost = 0

    for name, attrs in ranked:
        if attrs["cost"] <= remaining:
            selected.append(name)
            remaining       -= attrs["cost"]
            total_cost      += attrs["cost"]
            total_calories  += attrs["calories"]

    return selected, total_cost, total_calories

# Dynamic Programming
def dynamic_programming(
    items: Dict[str, Dict[str, int]],
    budget: int,
) -> Tuple[list, int, int]:
    """
    Find the globally optimal food selection via 0/1 Knapsack DP.
    Algorithm
        Build a 2-D table  dp[i][w]  = maximum calories achievable using the first *i* items with a budget of *w*.  
        Then back-track through the table to recover which items were chosen.
    Complexity: 
        Time  - O(n · W) 
        Space - O(n · W), where n = number of items and W = budget.
    Parameters:
        items  : dict  — food catalogue {name: {cost, calories}}
        budget : int   — maximum total spend
    Returns:
        selected : list of item names chosen
        total_cost     : int  — sum of costs for selected items
        total_calories : int  — sum of calories for selected items
    """
    names    = list(items.keys())
    costs    = [items[n]["cost"] for n in names]
    calories = [items[n]["calories"] for n in names]
    n = len(names)

    # Build DP table (n+1) X (budget+1)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost_i = costs[i - 1]
        cal_i  = calories[i - 1]
        for w in range(budget + 1):
            # Option A: skip item i
            dp[i][w] = dp[i - 1][w]
            # Option B: take item i (if it fits)
            if cost_i <= w:
                take = dp[i - 1][w - cost_i] + cal_i
                if take > dp[i][w]:
                    dp[i][w] = take
    # Back-track to find selected items
    selected: list = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:    # item i was taken
            selected.append(names[i - 1])
            w -= costs[i - 1]

    selected.reverse()      # restore original order
    total_cost = sum(items[name]["cost"] for name in selected)
    total_calories = sum(items[name]["calories"] for name in selected)
    return selected, total_cost, total_calories

# Pretty-printer helper
def print_result(
    label: str,
    selected: list,
    total_cost: int,
    total_calories: int,
    budget: int,
) -> None:
    """Render results in a readable table format."""
    width = 52
    print(f"\n{'─' * width}")
    print(f"  {label}")
    print(f"{'─' * width}")
    print(f"    {'Item':<15} {'Cost':>6}  {'Calories':>9}")
    print(f"    {'─'*15} {'─'*6}  {'─'*9}")
    for name in selected:
        c  = ITEMS[name]["cost"]
        ca = ITEMS[name]["calories"]
        print(f"    {name:<15} {c:>6}  {ca:>9}")
    print(f"    {'─'*15} {'─'*6}  {'─'*9}")
    print(f"    {'TOTAL':<15} {total_cost:>6}  {total_calories:>9}")
    print(f"    Budget remaining:   {budget - total_cost}")

# Entry point
if __name__ == "__main__":
    BUDGET = 100

    print("\n", "~" * 5, f" FOOD SELECTION OPTIMIZER  |  Budget = {BUDGET} ", "~" * 5)
    # Greedy
    g_selected, g_cost, g_cal = greedy_algorithm(ITEMS, BUDGET)
    print_result("GREEDY ALGORITHM", g_selected, g_cost, g_cal, BUDGET)

    # Dynamic Programming
    dp_selected, dp_cost, dp_cal = dynamic_programming(ITEMS, BUDGET)
    print_result("DYNAMIC PROGRAMMING", dp_selected, dp_cost, dp_cal, BUDGET)

    # Comparison
    print("\n", "~" * 5, " COMPARISON SUMMARY ", "~" * 5)
    print(f"  {'Metric':<22} {'Greedy':>10} {'DP':>10}")
    print(f"  {'─'*22} {'─'*10} {'─'*10}")
    print(f"  {'Total Calories':<22} {g_cal:>10} {dp_cal:>10}")
    print(f"  {'Total Cost':<22} {g_cost:>10} {dp_cost:>10}")
    print(f"  {'Items Selected':<22} {len(g_selected):>10} {len(dp_selected):>10}")
    diff = dp_cal - g_cal
    marker = " <- optimal" if diff > 0 else (" <- tied" if diff == 0 else "")
    print(f"  {'Calorie Difference':<22} {diff:>+10}{marker}\n")