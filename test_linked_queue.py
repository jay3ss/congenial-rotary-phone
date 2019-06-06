"""Tests the linked queue"""
import pytest

from exceptions import EmptyException
from queues import LinkedQueue

def test_empty_queue():
    """Tests the behavior of a new, empty queue

    The axioms that are being tested are:

    1. (new LinkedQueue()).is_empty() = True
    2. (new LinkedQueue()).length = 1
    3. (new LinkedQueue()).peek() = Error
    4. (new LinkedQueue()).dequeue() = False
    """
    queue = LinkedQueue()

    assert queue.is_empty()             # 1
    assert queue.length == 1            # 2
    with pytest.raises(EmptyException):
        queue.peek()                    # 3

    assert not queue.dequeue()          # 4


def test_adding_and_removing_entries():
    """Test the behavior of adding and removing entries to and fromt the
    queue.

    The axioms that are being tested are:

    1. queue.length = (queue.enqueue(x)).length - 1
    2. queue.length = (queue.dequeue()).length + 1
    3. (queue.enqueue(x)).is_empty() = False
    """
