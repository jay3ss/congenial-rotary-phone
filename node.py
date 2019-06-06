"""Defines a node for link-based data structures"""
class Node:
    """A node in the linked list"""

    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return repr(self.data)
