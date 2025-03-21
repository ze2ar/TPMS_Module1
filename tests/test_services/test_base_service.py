import pytest
from math import factorial

from core.services.base import (
    permutations,
    arrangements,
    combinations,
    combinations_with_repetition,
)


@pytest.mark.parametrize(
    "n, expected",
    [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)],
)
def test_permutations(n, expected):
    assert permutations(n=n) == expected


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (5, 3, 60),
        (4, 4, 24),
        (10, 0, 1),
        # Wrong params
        (3, 5, 0),
        (-1, 2, 0),
        (5, -2, 0),
    ],
)
def test_arrangements(n, k, expected):
    assert arrangements(n=n, k=k) == expected


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (5, 3, 10),
        (4, 4, 1),
        (10, 0, 1),
        # Wrong params
        (3, 5, 0),
        (-1, 2, 0),
        (5, -2, 0),
        # Test (комиссия)
        (9, 3, 84),
        (9, 5, 126),
        (7, 4, 35),
        (8, 4, 70),
        (6, 3, 20),
    ],
)
def test_combinations(n, k, expected):
    assert combinations(n=n, k=k) == expected


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (3, 5, 35),
        (0, 4, 1),
        (3, 1, 1),
        # Wrong params
        (3, 0, 0),
        (-1, 2, 0),
        (2, -1, 0),
        # Test (букеты)
        (11, 5, 1365),
        (11, 3, 78),
        (7, 4, 120),
        (7, 3, 36),
    ],
)
def test_combinations_with_repetition(n, k, expected):
    assert combinations_with_repetition(n=n, k=k) == expected
