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
    if not callable(func):
        raise ValueError("The provided `func` must be callable.")

    def wrapped_func():
        func(*args, **kwargs)

    execution_time = timeit.timeit(wrapped_func, number=1000)
    return execution_time / 1000


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
    if not callable(search_func):
        raise ValueError("The provided `search_func` must be callable.")

    # measure the time to find all targets
    def search_all_targets():
        for target in targets:
            search_func(dataset, target, **kwargs)

    return benchmark(search_all_targets)
