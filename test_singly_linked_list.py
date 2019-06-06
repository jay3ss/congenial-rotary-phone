"""Tests for the SinglyLinkedList class"""
import copy

import pytest

from exceptions import InvalidPositionException
from lists import SinglyLinkedList


def test_empty_list():
    """Test the behavior of an a new, empty linked list. The axioms that are
    followed for an empty list are:

        1. (new SinglyLinkedList()).is_empty() = True
        2. (new SinglyLinkedList()).length = 0
        3. (new SinglyLinkedList()).remove(i) = False
        4. (new SinglyLinkedList()).replace(i) = Error
        5. (new SinglyLinkedList()).entry(i) = Error
    """
    lst = SinglyLinkedList()

    assert lst.is_empty()               # 1
    assert lst.length == 0              # 2
    assert not lst.remove(5)            # 3

    with pytest.raises(InvalidPositionException):
        lst.replace(5, 15)              # 4

    with pytest.raises(InvalidPositionException):
        lst.entry(15)                   # 5


def test_adding_and_removing_entries():
    """Test the behavior of adding entries using the following axioms:

        1. a_list.length = (a_list.insert(i, x)).length - 1
        2. a_list.length = (a_list.remove(i)).length + 1
        3. (a_list.insert(i, item)).isEmpty() = False
        4. (a_list.insert(i, x)).remove(i) = a_list
        5. (a_list.insert(i, x)).entry(i) = x
        6. a_list.entry(i) = (a_list.insert(i, x)).entry(i + 1)
        7. a_list.entry(i + 1) = (a_list.remove(i)).entry(i)
        8. (a_list.replace(i, x)).entry(i) = x
    """
    lst = SinglyLinkedList()
    num_entries = 10
    for i in range(1, num_entries):
        lst.insert(i, i*i)

    init_size = lst.length
    lst.insert(num_entries, num_entries*num_entries)
    assert lst.length - 1 == init_size              # 1

    lst.remove(num_entries)
    assert lst.length == init_size                  # 2

    assert not lst.is_empty()                       # 3

    lst_copy = copy.deepcopy(lst)
    lst.insert(num_entries, num_entries*num_entries)
    lst.remove(num_entries)

    assert lst_copy == lst                          # 4

    lst.insert(num_entries, num_entries*num_entries)
    entry = lst.entry(num_entries)
    assert entry.data == num_entries*num_entries    # 5

    lst.remove(num_entries) # reset
    third_entry = lst.entry(3)
    lst.insert(3, num_entries*num_entries)
    fourth_entry = lst.entry(4)
    assert third_entry == fourth_entry              # 6

    lst.remove(3)
    new_third_entry = lst.entry(3)
    assert new_third_entry == third_entry           # 7

    new_entry = 'new entry'
    lst.replace(5, new_entry)
    fifth_entry = lst.entry(5)
    assert fifth_entry.data == new_entry
