import math


def permutations(n: int, k: int) -> int:
    """
    Вычисляет количество перестановок из n по k.

    Формула: P(n, k) = n! / (n - k)!

    :param n: Общее количество элементов
    :param k: Количество выбираемых элементов
    :return: Количество перестановок
    """
    if k > n or n < 0 or k < 0:
        return 0
    return math.factorial(n) // math.factorial(n - k)


def combinations(n: int, k: int) -> int:
    """
    Вычисляет количество сочетаний из n по k.

    Формула: C(n, k) = n! / (k! * (n - k)!)

    :param n: Общее количество элементов
    :param k: Количество выбираемых элементов
    :return: Количество сочетаний
    """
    if k > n or n < 0 or k < 0:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def combinations_with_repetition(n: int, k: int) -> int:
    """
    Вычисляет количество сочетаний с повторениями.

    Формула: C(n + k - 1, k) = (n + k - 1)! / (k! * (n - 1)!)

    :param n: Общее количество элементов
    :param k: Количество выбираемых элементов
    :return: Количество сочетаний с повторениями
    """
    if n <= 0 or k < 0:
        return 0
    return math.factorial(n + k - 1) // (math.factorial(k) * math.factorial(n - 1))
