"""Binary search implementations (iterative and recursive)."""

from typing import Any, List, Optional


def binary_search_iterative(dataset: List[Any], target: Any) -> Optional[int]:
    """Perform an iterative binary search on the dataset.

    Note: Dataset must be sorted for binary search to work correctly.

    Args:
        dataset: Sorted list to search through
        target: Element to search for

    Returns:
        int: Index of the target element, or None if not found
    """
    left, right = 0, len(dataset) - 1
    while left <= right:
        mid = (left + right) // 2
        if dataset[mid] == target:
            return mid
        elif dataset[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def binary_search_recursive(
    dataset: List[Any], target: Any, left: int = 0, right: Optional[int] = None
) -> Optional[int]:
    """Perform a recursive binary search on the dataset.

    Note: Dataset must be sorted for binary search to work correctly.

    Args:
        dataset: Sorted list to search through
        target: Element to search for
        left: Left boundary index
        right: Right boundary index

    Returns:
        int: Index of the target element, or None if not found
    """
    if right is None:
        right = len(dataset) - 1
    if left > right:
        return None

    mid = (left + right) // 2
    if dataset[mid] == target:
        return mid
    elif dataset[mid] < target:
        return binary_search_recursive(dataset, target, mid + 1, right)
    else:
        return binary_search_recursive(dataset, target, left, mid - 1)
