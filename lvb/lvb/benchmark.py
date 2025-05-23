"""Run a benchmark on search operations."""

import timeit
from typing import Any, Callable, List


def benchmark(func: Callable, *args, **kwargs) -> float:
    """Run a benchmark on a function using timeit.

    Args:
        func (Callable): Function to benchmark.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        float: Average execution time in seconds.

    Raises:
        ValueError: If the provided `func` is not callable.
    """
    if not callable(func):  # Check if func is callable
        raise ValueError("The provided `func` must be callable.")  # raise ValueError

    def wrapped_func():
        """Wrap the function call for timeit."""
        func(*args, **kwargs)  # Call the function with arguments

    execution_time = timeit.timeit(wrapped_func, number=1000)  # Measure execution time
    return execution_time / 1000 # Average over 1000 runs


def benchmark_search(
    search_func: Callable, dataset: List[Any], targets: List[Any], **kwargs
) -> float:
    """Benchmark a search function with multiple targets.

    Args:
        search_func (Callable): Search function to benchmark.
        dataset (List[Any]): Dataset to search through.
        targets (List[Any]): List of target elements to search for.
        **kwargs: Additional keyword arguments for the search function.

    Returns:
        float: Average execution time in seconds.

    Raises:
        ValueError: If the provided `search_func` is not callable.
    """
    if not callable(search_func):  # Check if search_func is callable
        raise ValueError("The provided `search_func` must be callable.")  # raise ValueError

    # measure the time to find all targets
    def search_all_targets():  # Define a function to search all targets
        for target in targets:  # Iterate through each target
            search_func(dataset, target, **kwargs)  # Call the search function
    return benchmark(search_all_targets)  # Measure the average execution time
