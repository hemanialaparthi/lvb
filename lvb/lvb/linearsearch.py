import time


def linear_search(arr, target):
    """Perform linear search and return search time."""
    start = time.perf_counter()
    for elem in arr:
        if elem == target:
            end = time.perf_counter()
            return True, end - start
    end = time.perf_counter()
    return False, end - start
