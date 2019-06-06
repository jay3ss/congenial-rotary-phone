"""Defines different implementations of queues"""
from exceptions import EmptyException
from interfaces import QueueInterface
from node import Node


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

        if can_dequeue:
            # There is ony one entry in the queue
            if self.front.next is None:
                self.front = None
            else:
                self.front = self.front.next
            self.length -= 1

        return can_dequeue

    def enqueue(self, entry):
        """Adds a new entry to the back of the queue"""
        # There's nothing in the queue
        node = Node(data=entry)
        if self.tail is None:
            self.front = node
        else:
            self.tail.next = node

        self.tail = node
        self.length += 1
        return True


    def peek(self):
        """Returns the front of the queue"""
        if self.is_empty():
            raise EmptyException("Queue is empty")

        return self.front.data


if __name__ == '__main__':
    queue = LinkedQueue()
    queue.enqueue(1)

    num_entries = 3
    for i in range(2, num_entries+1):
        queue.enqueue(i*i)

    test_entry = num_entries * num_entries
    entry = queue.peek()

    queue.dequeue()
