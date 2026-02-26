"""
Profiling examples for CPU-intensive and memory-intensive workloads.

These examples are used in the documentation to demonstrate how to profile
Python code using :mod:`cProfile` (CPU) and :mod:`tracemalloc` (memory).
"""


def fibonacci(n):
    """CPU-intensive recursive Fibonacci calculation."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def bubble_sort(lst):
    """CPU-intensive bubble sort algorithm."""
    lst = lst[:]
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def cpu_intensive_work():
    """Run combined CPU-intensive operations."""
    fibonacci(28)
    bubble_sort(list(range(500, 0, -1)))


def memory_intensive_work():
    """Run memory-intensive operations and return total element count."""
    large_list = [i**2 for i in range(500_000)]
    large_dict = {str(i): i * 3.14 for i in range(100_000)}
    nested = [[j for j in range(100)] for _ in range(1_000)]
    return len(large_list) + len(large_dict) + len(nested)
