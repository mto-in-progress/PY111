"""
Taylor series
"""
from typing import Union
import math
import itertools


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

    ex0 = 1
    dx = x  # приращение
    i = 2  # номер приращения
    while abs(dx) > 0:
        ex0 = ex0 + dx
        dx = dx * x / i
        i = i + 1
    return ex0


print(ex(2))
print(math.exp(2))


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    result = x
    if x == 0:
        return 0
    else:
        for i in itertools.count(1, 1):
            n = 2 * i + 1
            result += ((-1) ** i) * (x ** n / math.factorial(n))
            if 0.001 > (x ** i / math.factorial(i)):
                break
        print(x)
        return result


print(sinx(3))
print(math.sin(3))
