"""Generate test data for search benchmarking."""
import random
import string
from typing import List, Any, Tuple, Optional

from lvb.approach import DataType, TargetPosition
from lvb.constants import constants
from lvb.bst import BinarySearchTree


def generate_random_integer() -> int:
    """Generate a random integer within the specified range."""
    return random.randint(
        constants.RANDOM_INT_MIN,
        constants.RANDOM_INT_MAX
    )


def generate_random_float() -> float:
    """Generate a random float within the specified range."""
    return random.uniform(
        constants.RANDOM_FLOAT_MIN, 
        constants.RANDOM_FLOAT_MAX
    )


def generate_random_string() -> str:
    """Generate a random string of specified length."""
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits, 
            k=constants.STRING_LENGTH
        )
    )


def generate_dataset(size: int, data_type: DataType, sorted_data: bool = False) -> List[Any]:
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
    data_type: DataType  # Add data_type parameter
) -> List[Any]:
    """Select target elements from the dataset based on position.

    Args:
        dataset: Dataset to select targets from
        position: Where in the dataset to select targets from
        num_targets: Number of targets to select
        data_type: Type of data to generate for NONEXISTENT targets

    Returns:
        List: Selected target elements
    """
    size = len(dataset)
    targets = []

    if size == 0:
        return targets

    if position == TargetPosition.BEGINNING:
        # Select from the first 10% of elements
        end_idx = max(1, int(size * 0.1))
        targets = random.choices(dataset[:end_idx], k=num_targets)

    elif position == TargetPosition.MIDDLE:
        # Select from the middle 10% of elements
        start_idx = int(size * 0.45)
        end_idx = int(size * 0.55)
        segment = dataset[start_idx:end_idx]
        targets = random.choices(segment, k=num_targets) if segment else []

    elif position == TargetPosition.END:
        # Select from the last 10% of elements
        start_idx = int(size * 0.9)
        targets = random.choices(dataset[start_idx:], k=num_targets)

    elif position == TargetPosition.RANDOM:
        # Select random elements from the entire dataset
        targets = random.choices(dataset, k=num_targets)

    elif position == TargetPosition.NONEXISTENT:
        # Generate values guaranteed not to be in the dataset
        if not dataset:
            # Generate based on data_type
            if data_type == DataType.INTEGERS:
                targets = [constants.RANDOM_INT_MAX + i + 1 for i in range(num_targets)]
            elif data_type == DataType.FLOATS:
                targets = [constants.RANDOM_FLOAT_MAX + i + 1.0 for i in range(num_targets)]
            elif data_type == DataType.STRINGS:
                targets = [''.join(random.choices(
                    string.ascii_letters + string.digits, 
                    k=constants.STRING_LENGTH + 10
                )) for _ in range(num_targets)]
        else:
            # Find the max value and generate larger values
            max_val = max(dataset)

            if isinstance(max_val, int):
                targets = [max_val + i + 1 for i in range(num_targets)]
            elif isinstance(max_val, float):
                targets = [max_val + i + 1.0 for i in range(num_targets)]
            else:  # String
                # Generate longer strings
                targets = [''.join(random.choices(
                    string.ascii_letters + string.digits, 
                    k=len(max_val) + 5
                )) for _ in range(num_targets)]

    return targets
