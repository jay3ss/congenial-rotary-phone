"""Defines different implementations of queues"""
import abc

from exceptions import EmptyException
from node import Node


class QueueInterface(abc.ABC):
    """Defines the interface for a queue"""
    @abc.abstractmethod
    def is_empty(self):
        """Determines if the queue is empty"""

    @abc.abstractmethod
    def dequeue(self):
        """Removes an entry from the front of the queue"""

    @abc.abstractmethod
    def enqueue(self, entry):
        """Adds a new entry to the back of the queue"""

    @abc.abstractmethod
    def peek(self):
        """Returns the front of the queue"""


class LinkedQueue(QueueInterface):
    """Implements a link-based queue"""
    def __init__(self):
        self.front = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        """Determines if the queue is empty"""
        return self.length == 0

    def dequeue(self):
        """Removes an entry from the front of the queue"""
        can_dequeue = not self.is_empty()

        return can_dequeue

    def enqueue(self, entry):
        """Adds a new entry to the back of the queue"""

    def peek(self):
        """Returns the front of the queue"""
        if self.is_empty():
            raise EmptyException("Queue is empty")
