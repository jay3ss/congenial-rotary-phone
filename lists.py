"""Defines different implementations of lists"""
from exceptions import InvalidPositionException
from interfaces import ListInterface
from node import Node


class SinglyLinkedList(ListInterface):
    """Implements a linked-list"""
    def __init__(self):
        self.head = None
        self.length = 0

    def clear(self):
        """Clears the list of all data"""
        while self.head:
            self.remove(1)

    def entry(self, position):
        """Get an entry at a certain position"""
        if position < 1 or position > self.length:
            raise InvalidPositionException(f"{position} is invalid")

        return self._node_at(position)

    def insert(self, position, data):
        """Inserts an entry at a desired position"""
        can_insert = 1 <= position <= self.length + 1
        if can_insert:
            node = Node(data=data)

            # The list is empty
            if self.head is None:
                self.head = node
            # The list isn't empty, traverse it until the end is found
            else:
                # Find the node before the insertion position
                previous = self._node_at(position-1)

                # Insert the node after the one that previous points to
                node.next = previous.next
                previous.next = node


            # The node has been added, so increase the length of the list
            self.length += 1
        return can_insert

    def is_empty(self):
        """Determines if the list is empty or not"""
        return self.length == 0

    def remove(self, position):
        """Removes an entry at the given position"""
        can_remove = 1 <= position <= self.length

        if can_remove:
            if position == 1:
                self.head = self.head.next

            else:
                # Get the node that preceds the node that we want to remove
                previous = self._node_at(position-1)

                # Get the desired node
                current = previous.next

                # Bypass the node that we wish to remove
                previous.next = current.next


            self.length -= 1

        return can_remove

    def replace(self, position, data):
        """Replaces an entry in the list at the desired position"""
        node = self._node_at(position)
        node.data = data

    def _node_at(self, position):
        """Gets the node a desired position"""
        # Trying to insert into an invalid position
        if self.length < position or position < 0:
            raise InvalidPositionException(f"{position} is invalid")

        current = self.head
        for _ in range(1, position):
            current = current.next

        return current

    def _is_invalid_position(self, position):
        """Determines if a position is invalid"""
        return self.length < position or position < 0

    def __eq__(self, other):
        same = self.length == other.length
        if same:
            for position in range(1, self.length):
                this_entry = self.entry(position)
                that_entry = other.entry(position)

                if this_entry != that_entry:
                    return False
        return same

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next

        return '[' + ', '.join(nodes) + ']'
