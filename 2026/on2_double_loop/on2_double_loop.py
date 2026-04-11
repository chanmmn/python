"""O(n^2) quadratic-time sample."""

COMPLEXITY = "O(n^2)"
LABEL = "Double loop"
SIZES = [10, 50, 100, 300]


def operation_count(n: int) -> int:
    """Counts operations in a nested n x n loop."""
    ops = 0
    for _ in range(n):
        for _ in range(n):
            ops += 1
    return ops


def print_demo() -> None:
    print(f"{COMPLEXITY} | {LABEL}")
    print("n -> operations")
    for n in SIZES:
        print(f"{n:>6} -> {operation_count(n):>12}")


if __name__ == "__main__":
    print_demo()