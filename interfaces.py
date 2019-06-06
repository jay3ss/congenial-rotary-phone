"""Module that holds the interfaces that define different data structures"""
import abc


class ListInterface(abc.ABC):
    """Abstract base class that defines a list"""
    @abc.abstractmethod
    def clear(self):
        """Removes all entries from the list"""

    @abc.abstractmethod
    def entry(self, position):
        """Returns the entry at the given position"""

    @abc.abstractmethod
    def insert(self, position, data):
        """Inserts the data at a given position"""

    @abc.abstractmethod
    def is_empty(self):
        """Determines if the list is empty"""

    @abc.abstractmethod
    def remove(self, position):
        """Removes an entry at the given position"""

    @abc.abstractmethod
    def replace(self, position, data):
        """Replaces an entry in the list at the desired position"""


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


class StackInterface(abc.ABC):
    """An abstract base class that defines a stack"""
    @abc.abstractmethod
    def is_empty(self):
        """Determines if the stack is empty"""

    @abc.abstractmethod
    def peek(self):
        """Returns the top of the stack"""

    @abc.abstractmethod
    def pop(self):
        """Removes the top of the stack"""

    @abc.abstractmethod
    def push(self, entry):
        """Adds a new entry to the top of the stack"""
