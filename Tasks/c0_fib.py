def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 1:
        return 1
    if n == 2:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if 1 < n <= 2:
        return 1
    else:
        number = [0, 1]
        try:
            for i in range(2, (n + 1)):
                number.append(number[i - 1] + number[i - 2])
            return number[n]
        except IndexError:
            pass
