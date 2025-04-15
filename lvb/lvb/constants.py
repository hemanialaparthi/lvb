"""Define constants with dataclasses."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Constants:
    """Class to store numerical constants for the searcher module."""
    # Default values for the benchmarking
    DEFAULT_START_SIZE: int
    DEFAULT_RUNS: int
    DEFAULT_SEARCHES: int
    DOUBLING_FACTOR: int

    # For data generation
    RANDOM_INT_MIN: int
    RANDOM_INT_MAX: int
    RANDOM_FLOAT_MIN: float
    RANDOM_FLOAT_MAX: float
    STRING_LENGTH: int

    # For output formatting
    DECIMAL_PLACES: int


constants = Constants(
    DEFAULT_START_SIZE=1000,      # Default starting size for datasets
    DEFAULT_RUNS=5,               # Default number of benchmarking runs
    DEFAULT_SEARCHES=100,         # Default number of searches per run
    DOUBLING_FACTOR=2,            # Factor by which the dataset size increases

    RANDOM_INT_MIN=1,             # Minimum value for random integers
    RANDOM_INT_MAX=10000,         # Maximum value for random integers
    RANDOM_FLOAT_MIN=0.0,         # Minimum value for random floats
    RANDOM_FLOAT_MAX=10000.0,     # Maximum value for random floats
    STRING_LENGTH=10,             # Length of random strings

    DECIMAL_PLACES=6,             # Number of decimal places for output formatting
)
