"""Tests for the LinkedStack class"""
import pytest

from exceptions import EmptyException
from stacks import LinkedStack


def test_empty_stack():
    """Tests the behavior of a new, empty stack

    The axioms that are being tested are:

    1. (new LinkedStack()).is_empty() = True
    2. (new LinkedStack()).pop() = False
    3. (new LinkedStack()).peek() = Error
    """
    stack = LinkedStack()

    assert stack.is_empty()         # 1
    assert not stack.pop()          # 2
    with pytest.raises(EmptyException):
        stack.peek()                # 3


def test_adding_and_removing_entries():
    """Tests the behavior of adding and removing entries from the stack

    The axioms that are being tested are:

    1. (stack.push(item)).is_empty() = false
    2. (stack.push(item)).peek() = item
    3. (stack.push(item)).pop() = true
    """
    stack = LinkedStack()

    final_entry = 15
    for i in range(final_entry):
        stack.push(i*i)

    assert not stack.is_empty()     # 1

    test_entry = (final_entry - 1) ** 2
    entry = stack.peek()
    assert test_entry == entry      # 2

    assert stack.push(entry)        # 3
