"""Test cases for the BST function."""

import pytest

from lvb.binarysearchtree import (
    BinarySearchTree,
)


@pytest.fixture
def sample_bst():
    bst = BinarySearchTree()
    for value in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(value)
    return bst


def test_insert_root():
    bst = BinarySearchTree()
    bst.insert(10)
    value = 10
    assert bst.root is not None
    assert bst.root.data == value


def test_search_existing_value(sample_bst):
    found, duration = sample_bst.search(60)
    assert found is True
    assert duration >= 0


def test_search_non_existing_value(sample_bst):
    found, duration = sample_bst.search(99)
    assert found is False
    assert duration >= 0


def test_search_min_value(sample_bst):
    found, _ = sample_bst.search(20)
    assert found is True


def test_search_max_value(sample_bst):
    found, _ = sample_bst.search(80)
    assert found is True


def test_search_in_empty_tree():
    bst = BinarySearchTree()
    found, _ = bst.search(5)
    assert found is False


def test_insert_duplicates(sample_bst):
    sample_bst.insert(70)
    sample_bst.insert(30)
    found1, _ = sample_bst.search(70)
    found2, _ = sample_bst.search(30)
    assert found1 is True
    assert found2 is True
