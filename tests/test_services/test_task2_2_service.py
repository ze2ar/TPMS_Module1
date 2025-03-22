import pytest
from math import isclose

from core.services import meeting_probability, probability_of_condition


@pytest.mark.parametrize(
    "start_time, end_time, wait_time, expected",
    [
        (9, 10, 5, 0.159),
        (9, 10, 0, 0),
        (9, 10, 60, 1),
        (14, 16, 15, 0.234),
        # From tests
        (13, 20, 22, 0.102),
        (15, 18, 33, 0.333),
        (10, 11, 5, 0.160),
        (14, 22, 26, 0.105),
        (13, 19, 21, 0.113),
        (11, 13, 9, 0.144),
    ],
)
def test_meeting_probability(start_time, end_time, wait_time, expected):
    result = round(meeting_probability(start_time, end_time, wait_time), 3)
    assert isclose(
        result, expected, abs_tol=1.01e-3
    ), f"Expected {expected}, got {result}"


@pytest.mark.parametrize(
    "start, end, condition_func, sign, expected",
    [
        (0, 20, lambda x: x + 10, ">", 0.125),
        (0, 10, lambda x: 2 * x, "<", 0.750),
        (5, 15, lambda x: x - 3, ">", 0.755),
        (0, 5, lambda x: 10, "<", 1),
        # From tests
        (0, 10, lambda x: 7 / x, ">", 0.744),
        (0, 5, lambda x: 2 * pow(x, 2), ">", 0.211),
        (0, 3, lambda x: 7 * x - 5, "<", 0.690),
    ],
)
def test_probability_of_condition_parametrized(
    start, end, condition_func, sign, expected
):
    prob = round(probability_of_condition(start, end, condition_func, sign), 3)
    assert prob == expected, f"Expected {expected}, got {prob}"


@pytest.mark.parametrize(
    "start, end, condition_func, sign",
    [
        (0, 10, lambda x: x, "!="),
        (0, 10, lambda x: x, "=="),
        (0, 10, lambda x: x, "invalid"),
    ],
)
def test_probability_of_condition_invalid_sign_parametrized(
    start, end, condition_func, sign
):
    with pytest.raises(ValueError, match="Неизвестный знак сравнения"):
        probability_of_condition(start, end, condition_func, sign)
