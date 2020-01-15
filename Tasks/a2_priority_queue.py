"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any, Dict

_enqueue: Dict = {}


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    try:
        _enqueue[priority].append(elem)

    except KeyError:
        _enqueue[priority] = [elem]


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if _enqueue:
        return None
    else:
        return _enqueue.pop(0)


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return _enqueue[priority][ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    # global _enqueue
    # _enqueue = {}
    _enqueue.clear()
