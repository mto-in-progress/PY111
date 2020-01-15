"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array

    """
    minimal = arr[0]
    min_index = 0
    try:
        for i in range(len(arr)):
            if arr[i] < minimal:
                minimal = arr[i]
                min_index = i
        print(arr)
        return min_index
    except IndexError:
        pass


    # elem = arr[0]
    #
    # for i in range(1, len(arr)):
    #     if i > arr[0]:
    #         elem = i
    # return elem

    # def search(arr, x):
    #     for i in range(len(arr)):
    #
    #         if arr[i] == x:
    #             return i
    #
    #     return -1
    #
    #
    # print(search([5, 9, 8, -3], -3))

