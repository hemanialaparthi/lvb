"""Generate test data for search benchmarking."""

import random
import string
from typing import Any, List

from lvb.approach import DataType, TargetPosition
from lvb.bst import BinarySearchTree
from lvb.constants import constants


def generate_random_integer() -> int:
    """Generate a random integer within the specified range."""
    return random.randint(constants.RANDOM_INT_MIN, constants.RANDOM_INT_MAX)


def generate_random_float() -> float:
    """Generate a random float within the specified range."""
    return random.uniform(
        constants.RANDOM_FLOAT_MIN, constants.RANDOM_FLOAT_MAX
    )


def generate_random_string() -> str:
    """Generate a random string of specified length."""
    return "".join(
        random.choices(
            string.ascii_letters + string.digits, k=constants.STRING_LENGTH
        )
    )


def generate_dataset(
    size: int, data_type: DataType, sorted_data: bool = False
) -> List[Any]:
    """Generate a dataset of the specified size and type.

    Args:
        size: Size of the dataset to generate
        data_type: Type of data to generate
        sorted_data: Whether to sort the dataset

    Returns:
        List: Generated dataset
    """
    # Generate values based on the data type
    if data_type == DataType.INTEGERS:
        dataset = [generate_random_integer() for _ in range(size)]
    elif data_type == DataType.FLOATS:
        dataset = [generate_random_float() for _ in range(size)]
    elif data_type == DataType.STRINGS:
        dataset = [generate_random_string() for _ in range(size)]
    else:
        raise ValueError(f"Unknown data type: {data_type}")

    # sort the dataset if required
    if sorted_data:
        dataset.sort()

    return dataset


def generate_binary_search_tree(dataset: List[Any]) -> BinarySearchTree:
    """Generate a balanced binary search tree from the dataset.

    Args:
        dataset: Dataset to build the tree from

    Returns:
        BinarySearchTree: Generated binary search tree
    """
    # Sort the dataset first to ensure proper tree balancing
    sorted_dataset = sorted(dataset)

    # Create and populate the binary search tree using a balanced approach
    bst = BinarySearchTree()

    # Helper function to insert middle elements first for balancing
    def build_balanced_bst(arr, start, end):
        if start > end:
            return

        # Get the middle element and insert it
        mid = (start + end) // 2
        bst.insert(arr[mid])

        # Recursively insert left and right subarrays
        build_balanced_bst(arr, start, mid - 1)
        build_balanced_bst(arr, mid + 1, end)

    # Build the balanced BST
    build_balanced_bst(sorted_dataset, 0, len(sorted_dataset) - 1)

    return bst


def select_targets(
    dataset: List[Any],
    position: TargetPosition,
    num_targets: int,
    data_type: DataType,
) -> List[Any]:
    """Select target elements from the dataset based on position."""
    size = len(dataset)
    if size == 0:
        return []

    if position == TargetPosition.NONEXISTENT:
        return _generate_nonexistent_targets(dataset, num_targets, data_type)

    return _select_existing_targets(dataset, position, num_targets)


def _select_existing_targets(
    dataset: List[Any], position: TargetPosition, num_targets: int
) -> List[Any]:
    """Helper function to select existing targets based on position."""
    size = len(dataset)
    if position == TargetPosition.BEGINNING:
        end_idx = max(1, int(size * 0.1))
        return random.choices(dataset[:end_idx], k=num_targets)

    if position == TargetPosition.MIDDLE:
        start_idx = int(size * 0.45)
        end_idx = int(size * 0.55)
        segment = dataset[start_idx:end_idx]
        return random.choices(segment, k=num_targets) if segment else []

    if position == TargetPosition.END:
        start_idx = int(size * 0.9)
        return random.choices(dataset[start_idx:], k=num_targets)

    if position == TargetPosition.RANDOM:
        return random.choices(dataset, k=num_targets)

    return []


def _generate_nonexistent_targets(
    dataset: List[Any], num_targets: int, data_type: DataType
) -> List[Any]:
    """Helper function to generate nonexistent targets."""
    if not dataset:
        if data_type == DataType.INTEGERS:
            return [
                constants.RANDOM_INT_MAX + i + 1 for i in range(num_targets)
            ]
        if data_type == DataType.FLOATS:
            return [
                constants.RANDOM_FLOAT_MAX + i + 1.0
                for i in range(num_targets)
            ]
        if data_type == DataType.STRINGS:
            return [
                "".join(
                    random.choices(
                        string.ascii_letters + string.digits,
                        k=constants.STRING_LENGTH + 10,
                    )
                )
                for _ in range(num_targets)
            ]

    max_val = max(dataset)
    if isinstance(max_val, int):
        return [max_val + i + 1 for i in range(num_targets)]
    if isinstance(max_val, float):
        return [max_val + i + 1.0 for i in range(num_targets)]
    return [
        "".join(
            random.choices(
                string.ascii_letters + string.digits, k=len(max_val) + 5
            )
        )
        for _ in range(num_targets)
    ]
