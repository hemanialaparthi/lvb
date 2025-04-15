"""Binary search implementations (iterative and recursive)."""

from typing import List, Any, Optional


def binary_search_iterative(dataset: List[Any], target: Any) -> Optional[int]:
    """Perform an iterative binary search on the dataset.

    Note: Dataset must be sorted for binary search to work correctly.

    Args:
        dataset: Sorted list to search through
        target: Element to search for

    Returns:
        int: Index of the target element, or None if not found
    """
    # TODO: Will


def binary_search_recursive(
    dataset: List[Any],
    target: Any,
    left: int = 0,
    right: Optional[int] = None
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
    # TODO: Will
