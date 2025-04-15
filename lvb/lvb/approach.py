"""Configuration of the benchmarking tool and its approaches."""
from enum import Enum


# define the enums for the search benchmarking
class DataStructure(str, Enum):
    """Define the type of data structure to search."""
    UNSORTED_LIST = "unsorted_list"
    SORTED_LIST = "sorted_list"
    BINARY_SEARCH_TREE = "binary_search_tree"

    def __str__(self):
        """Define a default string representation."""
        return self.value


class SearchAlgorithm(str, Enum):
    """Define the search algorithm to benchmark."""
    LINEAR_SEARCH = "linear_search"
    BINARY_SEARCH_ITERATIVE = "binary_search_iterative"
    BINARY_SEARCH_RECURSIVE = "binary_search_recursive"
    BST_SEARCH = "bst_search"

    def __str__(self):
        """Define a default string representation."""
        return self.value


class TargetPosition(str, Enum):
    """Define where in the dataset to search for the target."""
    BEGINNING = "beginning"  # first 10% of elements
    MIDDLE = "middle"        # middle 10% of elements
    END = "end"              # last 10% of elements
    RANDOM = "random"        # random position
    NONEXISTENT = "nonexistent"  # element not in dataset

    def __str__(self):
        """Define a default string representation."""
        return self.value


class DataType(str, Enum):
    """Define the type of data to store and search."""
    INTEGERS = "integers"
    FLOATS = "floats"
    STRINGS = "strings"

    def __str__(self):
        """Define a default string representation."""
        return self.value
