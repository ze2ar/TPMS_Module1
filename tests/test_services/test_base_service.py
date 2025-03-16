from math import factorial

from core.services.base import permutations, combinations, combinations_with_repetition


# TODO Настроить логгер
def test_permutations_basic():
    # Проверяем количество перестановок из 5 по 3.
    assert permutations(5, 3) == 60
    # Проверяем случай, когда выбираются все элементы.
    assert permutations(4, 4) == factorial(4)
    # Проверяем выбор нуля элементов.
    assert permutations(10, 0) == 1

    # Проверка случая, когда k > n.
    assert permutations(3, 5) == 0
    # Проверка отрицательного значения n.
    assert permutations(-1, 2) == 0
    # Проверка отрицательного значения k.
    assert permutations(5, -2) == 0


def test_combinations_basic():
    # Проверяем количество сочетаний из 5 по 3.
    assert combinations(5, 3) == 10
    # Сочетания из n по n всегда 1 (выбираем всё множество).
    assert combinations(4, 4) == 1
    # Сочетания из n по 0 — всегда 1 (выбираем пустое множество).
    assert combinations(10, 0) == 1

    # k > n — невозможно выбрать больше элементов, чем доступно.
    assert combinations(3, 5) == 0
    # n отрицательное — невозможный случай.
    assert combinations(-1, 2) == 0
    # k отрицательное — нельзя выбрать отрицательное количество элементов.
    assert combinations(5, -2) == 0


def test_combinations_with_repetition_basic():
    # Проверяем количество сочетаний с повторениями из 5 по 3.
    assert combinations_with_repetition(5, 3) == 35
    # Сочетания с повторениями, когда выбираем 0 элементов — всегда 1.
    assert combinations_with_repetition(4, 0) == 1
    # Если есть 1 элемент, а выбираем 3 с повторениями — возможна только одна комбинация.
    assert combinations_with_repetition(1, 3) == 1

    # n <= 0 — невозможный случай для повторений.
    assert combinations_with_repetition(0, 3) == 0
    assert combinations_with_repetition(-1, 2) == 0
    # k < 0 — нельзя выбрать отрицательное количество элементов.
    assert combinations_with_repetition(5, -2) == 0
