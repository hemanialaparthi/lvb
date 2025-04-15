"""Linear search implementation."""
from typing import List, Any, Optional


def linear_search(dataset: List[Any], target: Any) -> Optional[int]:
    """Perform a linear search on the dataset.

    Args:
        dataset: List to search through
        target: Element to search for

    Returns:
        int: Index of the target element, or None if not found
    """
    # Iterate through the dataset
    for i, item in enumerate(dataset):
        if item == target:
            return i

    # Target not found
    return None
