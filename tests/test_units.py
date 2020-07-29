from fib.fibonacci import get_fibonacci_item, get_fibonacci_range_sequence


def test_get_fibonacci_item_1_equals():
    assert get_fibonacci_item(1) == 1


def test_get_fibonacci_item_2_equals():
    assert get_fibonacci_item(2) == 1


def test_get_fibonacci_item_4_equals():
    assert get_fibonacci_item(4) == 3


def test_get_fibonacci_item_6_equals():
    assert get_fibonacci_item(6) == 8


def test_get_fibonacci_item_10_equals():
    assert get_fibonacci_item(10) == 55


def test_get_fibonacci_slice_sequence_10():
    assert get_fibonacci_range_sequence(1, 8) == [1, 1, 2, 3, 5, 8, 13, 21]


def test_get_fibonacci_slice_sequence_1():
    assert get_fibonacci_range_sequence(1, 1) == [1]

