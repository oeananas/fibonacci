from app import cache


@cache.memoize()
def get_fibonacci_item(index: int) -> int:
    """ Getting the fib value by index. """

    if index in (1, 2):
        return 1
    return get_fibonacci_item(index - 1) + get_fibonacci_item(index - 2)


def get_fibonacci_range_sequence(begin: int, end: int) -> list:
    """ Getting the fib values slice by indexes range. """

    sequence = []
    for index in range(begin, end + 1):
        sequence.append(get_fibonacci_item(index))
    return sequence
