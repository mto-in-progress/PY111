"""
My little Queue
"""
from typing import Any, List

_queue: List = []


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global _queue
    _queue.append(elem)
    print(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    global _queue
    if _queue is not None:
        return _queue.pop(0)
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if ind in range(len(_queue)):
        return _queue[ind]

    if _queue:
        return None

    print(ind)


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    return _queue.clear()
