"""Tests the linked queue"""
import pytest

from exceptions import EmptyException
from queues import LinkedQueue


def test_empty_queue():
    """Tests the behavior of a new, empty queue

    The axioms that are being tested are:

    1. (new LinkedQueue()).is_empty() = True
    2. (new LinkedQueue()).length = 0
    3. (new LinkedQueue()).peek() = Error
    4. (new LinkedQueue()).dequeue() = False
    """
    queue = LinkedQueue()

    assert queue.is_empty()             # 1
    assert queue.length == 0            # 2
    with pytest.raises(EmptyException):
        queue.peek()                    # 3

    assert not queue.dequeue()          # 4


def test_adding_and_removing_entries():
    """Test the behavior of adding and removing entries to and from the
    queue.

    The axioms that are being tested are:

    1. queue.enqueue(x) = True
    2. (queue.enqueue(x)).is_empty() = False
    3. queue.length = (queue.enqueue(x)).length - 1
    4. (queue.enqueue(x)).peek() = x
    5. queue.dequeue() = True
    6. queue.length = (queue.dequeue()).length + 1
    """
    queue = LinkedQueue()
    assert queue.enqueue(1)                         # 1
    assert not queue.is_empty()                     # 2
    assert queue.length - 1 == 0                    # 3

    num_entries = 15
    for i in range(2, num_entries+1):
        queue.enqueue(i*i)

    test_entry = 1
    entry = queue.peek()
    assert test_entry == entry                      # 4

    pre_dequeue_length = queue.length

    assert queue.dequeue()                          # 5
    assert pre_dequeue_length - 1 == queue.length   # 6
