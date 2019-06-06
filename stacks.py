"""Different implementations of stacks"""
from exceptions import EmptyException
from interfaces import StackInterface
from node import Node


class LinkedStack(StackInterface):
    """Defines a link-based stack"""
    def __init__(self):
        self.top = None
        self.length = 0

    def is_empty(self):
        """Determines if the stack is empty"""
        return self.length == 0

    def peek(self):
        """Returns the top of the stack"""
        if self.top is None:
            raise EmptyException("Stack is empty")

        return self.top.data

    def pop(self):
        """Removes the top of the stack"""
        can_pop = self.length > 0
        if can_pop:
            # Advance the top of the stack to the next node
            self.top = self.top.next

        return can_pop


    def push(self, entry):
        """Adds a new entry to the top of the stack"""
        node = Node(data=entry)
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node

        self.length += 1
        return True

    def __repr__(self):
        nodes = []
        curr = self.top
        while curr:
            nodes.append(repr(curr))
            curr = curr.next

        return '[' + ', '.join(nodes) + ']'
