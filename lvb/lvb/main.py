"""Conduct experiments to evaluate performance of search algorithms."""

# ruff: noqa: PLR0913

import typer
from rich.console import Console
import statistics

from lvb import approach
from lvb.benchmark import benchmark
from lvb.constants import constants
from lvb.generate import generate_dataset, generate_binary_search_tree, select_targets
from lvb.binarysearch import binary_search_iterative, binary_search_recursive
from lvb.bst import BinarySearchTree
from lvb.linearsearch import linear_search

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()


@cli.command()
def main(
    data_structure: approach.DataStructure = typer.Option(
        approach.DataStructure.UNSORTED_LIST,
        "--data-structure", "-d",
    ),
    search_algorithm: approach.SearchAlgorithm = typer.Option(
        approach.SearchAlgorithm.LINEAR_SEARCH,
        "--search-algorithm", "-s",
    ),
    data_type: approach.DataType = typer.Option(
        approach.DataType.INTEGERS,
        "--data-type", "-t",
    ),
    target_position: approach.TargetPosition = typer.Option(
        approach.TargetPosition.RANDOM,
        "--target-position", "-p",
    ),
    start_size: int = typer.Option(constants.DEFAULT_START_SIZE),
    runs: int = typer.Option(constants.DEFAULT_RUNS),
    searches: int = typer.Option(constants.DEFAULT_SEARCHES),
):
    """Evaluate the performance of search algorithms."""
    # Display configuration details
    console.print("\n[bold blue]Search Algorithm Benchmarking Tool[/bold blue]\n")
    console.print(f"Data structure: {data_structure}")
    console.print(f"Search algorithm: {search_algorithm}")
    console.print(f"Data type: {data_type}")
    console.print(f"Target position: {target_position}")
    console.print(f"Number of runs: {runs}")
    console.print(f"Searches per run: {searches}\n")

    # Validate configurations
    if (search_algorithm in [approach.SearchAlgorithm.BINARY_SEARCH_ITERATIVE,
                            approach.SearchAlgorithm.BINARY_SEARCH_RECURSIVE] 
        and data_structure == approach.DataStructure.UNSORTED_LIST):
        console.print("[bold red]Error: Binary search requires sorted list![/bold red]")
        return

    if (search_algorithm == approach.SearchAlgorithm.BST_SEARCH 
        and data_structure != approach.DataStructure.BINARY_SEARCH_TREE):
        console.print("[bold red]Error: BST search requires binary tree![/bold red]")
        return

    # Initialize benchmarking variables
    size = start_size
    times = []
    sizes = []

    for run in range(1, runs + 1):
        # Generate dataset
        needs_sorted = (data_structure == approach.DataStructure.SORTED_LIST or
                       search_algorithm in [approach.SearchAlgorithm.BINARY_SEARCH_ITERATIVE,
                                          approach.SearchAlgorithm.BINARY_SEARCH_RECURSIVE])
        
        dataset = generate_dataset(size, data_type, sorted_data=needs_sorted)

        # Generate BST if needed
        bst = None
        if data_structure == approach.DataStructure.BINARY_SEARCH_TREE:
            bst = generate_binary_search_tree(dataset)

        # Select targets
        targets = select_targets(dataset, target_position, searches, data_type)

        # Select search function
        if search_algorithm == approach.SearchAlgorithm.LINEAR_SEARCH:
            search_func = linear_search
        elif search_algorithm == approach.SearchAlgorithm.BINARY_SEARCH_ITERATIVE:
            search_func = binary_search_iterative
        elif search_algorithm == approach.SearchAlgorithm.BINARY_SEARCH_RECURSIVE:
            search_func = binary_search_recursive
        else:
            search_func = bst.search

        # Benchmark execution
        def perform_searches():
            for target in targets:
                if data_structure == approach.DataStructure.BINARY_SEARCH_TREE:
                    search_func(target)
                else:
                    search_func(dataset, target)

        elapsed_time = benchmark(perform_searches)
        times.append(elapsed_time)
        sizes.append(size)

        # Display run results
        console.print(
            f"Run {run:2d}/{runs}: {search_algorithm} on {data_structure} "
            f"(size {size:8d}) completed in "
            f"{elapsed_time:.{constants.DECIMAL_PLACES}f} seconds"
        )

        size *= constants.DOUBLING_FACTOR

    # Calculate statistics
    min_time = min(times)
    max_time = max(times)
    avg_time = sum(times) / len(times)
    median_time = statistics.median(times)

    console.print("\n[bold green]Benchmark Summary:[/bold green]")
    console.print(f"Minimum time: {min_time:.{constants.DECIMAL_PLACES}f}s (size {sizes[times.index(min_time)]})")
    console.print(f"Maximum time: {max_time:.{constants.DECIMAL_PLACES}f}s (size {sizes[times.index(max_time)]})")
    console.print(f"Average time: {avg_time:.{constants.DECIMAL_PLACES}f}s")
    console.print(f"Median time:  {median_time:.{constants.DECIMAL_PLACES}f}s")
