"""
Monte Carlo Simulation: Two Dice Rolls
Task 7 - Probability estimation using the Monte Carlo method.
    This module simulates rolling two six-sided dice a large number of times,
    counts the frequency of each possible sum (2-12), and compares the
    empirical probabilities against the exact analytical values.
"""
import random
import json
from pathlib import Path

# Configuration
NUM_SIMULATIONS: int = 1_000_000
RANDOM_SEED: int | None = 42  # Set an integer for reproducible results
# Exact analytical probabilities (number of favourable outcomes / 36)
ANALYTICAL_PROBABILITIES: dict[int, float] = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}

# Simulation
def run_simulation(n: int, seed: int | None = None) -> dict[int, float]:
    """
    Simulate rolling two six-sided dice *n* times.
    Parameters:
        n : int
            Number of dice rolls to simulate.
        seed : int | None
            Optional random seed for reproducibility.
    Returns:
        dict[int, float]
            Empirical probability for each sum from 2 to 12.
    """
    if seed is not None:
        random.seed(seed)

    counts: dict[int, int] = {s: 0 for s in range(2, 13)}
    for _ in range(n):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        counts[roll_sum] += 1

    return {s: count / n for s, count in counts.items()}

# Reporting
def print_comparison_table(
    simulated: dict[int, float],
    analytical: dict[int, float],
    n_simulations: int,
) -> None:
    """Print a formatted comparison table to stdout."""
    width = 60
    print("\n" + "=" * width)
    print("~" * 5, f"{'Monte Carlo Dice Simulation':^{width - 12}}", "~" * 5)
    print("~" * 5, f"{'Simulations: ' + f'{n_simulations:,}':^{width - 12}}", "~" * 5)
    print("=" * width)
    print(f" {'Sum':<8} {'Analytical':^14} {'Monte Carlo':^15} {'|Diff|':^9}")
    print("-" * width)

    for s in range(2, 13):
        ana_pct = analytical[s] * 100
        sim_pct = simulated[s] * 100
        diff = abs(sim_pct - ana_pct)
        print(f"  {s:<6} {ana_pct:>11.4f}%  {sim_pct:>11.4f}%  {diff:>9.4f}%")

    print("=" * width)


def save_results(
    simulated: dict[int, float],
    analytical: dict[int, float],
    n_simulations: int,
    output_path: Path,
) -> None:
    """Persist simulation results to a JSON file."""
    payload = {
        "simulations": n_simulations,
        "simulated": {str(k): round(v, 8) for k, v in simulated.items()},
        "analytical": {str(k): round(v, 8) for k, v in analytical.items()},
    }
    output_path.write_text(json.dumps(payload, indent=2))
    print(f"\nResults saved -> {output_path}")


# Entry point
def main() -> None:
    print(f"\n>>> Running Monte Carlo simulation with {NUM_SIMULATIONS:,} rolls …")
    simulated = run_simulation(NUM_SIMULATIONS, seed=RANDOM_SEED)
    print_comparison_table(simulated, ANALYTICAL_PROBABILITIES, NUM_SIMULATIONS)

    output_path = Path(__file__).parent / "t07_results.json"
    save_results(simulated, ANALYTICAL_PROBABILITIES, NUM_SIMULATIONS, output_path)


if __name__ == "__main__":
    main()