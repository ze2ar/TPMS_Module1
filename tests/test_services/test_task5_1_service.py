import pytest

from core.services import (
    poisson_formatter,
    local_moivre_laplace_formatter,
    integral_moivre_laplace_formatter,
)


@pytest.mark.parametrize(
    "n, p, m, expected",
    [
        (900, 0.005, 3, "4,5^3/3!e^-4,5"),
    ],
)
def test_poisson_formatter(n, p, m, expected):
    result = poisson_formatter(n, p, m)
    assert result == expected


@pytest.mark.parametrize(
    "n, p, x_target, expected",
    [
        (170, 0.55, 90, "1/6,49fi(0,54)"),
    ],
)
def test_local_moivre_laplace_formatter(n, p, x_target, expected):
    result = local_moivre_laplace_formatter(n, p, x_target)
    assert result == expected


@pytest.mark.parametrize(
    "n, p, x1, x2, expected",
    [
        (400, 0.1, 30, 50, "Ф_0(1,67)+Ф_0(1,67)"),
    ],
)
def test_integral_moivre_laplace_formatter(n, p, x1, x2, expected):
    result = integral_moivre_laplace_formatter(n, p, x1, x2)
    assert result == expected
