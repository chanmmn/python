"""O(1) constant-time sample."""

COMPLEXITY = "O(1)"
LABEL = "Constant"
SIZES = [10, 100, 1_000, 10_000]


def operation_count(n: int) -> int:
    """Returns constant work regardless of n."""
    _ = n * 2
    return 1


def print_demo() -> None:
    print(f"{COMPLEXITY} | {LABEL}")
    print("n -> operations")
    for n in SIZES:
        print(f"{n:>6} -> {operation_count(n):>12}")


if __name__ == "__main__":
    print_demo()