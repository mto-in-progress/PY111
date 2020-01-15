"""
My little Stack
"""
from typing import Any, List

_stack: List = []


def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    _stack.append(elem)
    print(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    if _stack:
        return _stack.pop()


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the  element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    if ind in range(len(_stack)):
         return _stack[-(ind+1)]

    # if not _stack:
    #     return None
    # else:
    #     return _stack[-1]

    print(ind)



def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    return _stack.clear()
