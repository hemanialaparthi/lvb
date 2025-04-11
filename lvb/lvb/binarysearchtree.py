"""Binary Search Tree Function Implementation"""


import time


class Node:
    """Creates the Node class for the BST."""

    def __init__(self, value):
        self.l_child = None
        self.r_child = None
        self.data = value


class BinarySearchTree:
    """Initializing the BST."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts the value into the tree."""
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        """Inserts the value into the tree recursively."""
        if value < node.data:
            if node.l_child is None:
                node.l_child = Node(value)
            else:
                self.insert_recursive(node.l_child, value)
        else:  # noqa: PLR5501
            if node.r_child is None:
                node.r_child = Node(value)
            else:
                self.insert_recursive(node.r_child, value)

    def search(self, target):
        """Search for a value in the BST and return if found + time taken."""
        start = time.perf_counter()
        found = self.search_recursive(self.root, target)
        end = time.perf_counter()
        return found, end - start

    def search_recursive(self, node, target):
        """Search for a value in the BST recursively."""
        if node is None:
            return False
        if node.data == target:
            return True
        elif target < node.data:
            return self.search_recursive(node.l_child, target)   # the left node is smaller
        else:
            return self.search_recursive(node.r_child, target)  # the right node is larger than the target

