from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	high = len(arr) - 1
	low = 0
	while low <= high:
		mid = (high + low) // 2
		guess = arr[mid]
		if elem == guess:
			return mid
		elif elem < guess:
			high = mid - 1
		elif elem > guess:
			low = mid + 1
	return None



