import math
from collections import Counter
from typing import List

from core.services import arrangements, combinations


def count_words(word: str, length: int) -> int:
    """
    Вычисляет количество возможных "слов",
    которые можно составить из уникальных букв переданного слова,
    при условии, что длина каждого нового "слова" равна length.

    :param word: Исходное слово, из букв которого составляются новые "слова"
    :param length: Длина составляемого "слова"
    :return: Количество возможных "слов"
    """
    unique_letters = set(word.upper())

    n = len(unique_letters)
    k = length

    return arrangements(n, k)


def count_same_author_selection(
    books_by_authors: List[int], selected_books: int
) -> int:
    """
    Вычисляет количество способов выбрать selected_books книг
    одного автора из books_by_authors.

    :param books_by_authors: Список количеств книг у каждого автора
    :param selected_books: Сколько книг нужно выбрать
    :return: Количество способов выбора
    """
    total_ways = 0

    for books in books_by_authors:
        ways = combinations(books, selected_books)
        total_ways += ways

    return total_ways


def count_author_selection(authors_books: List[int], selected_books: List[int]) -> int:
    """
    Вычисляет количество способов выбрать заданное количество книг у каждого автора.

    :param authors_books: Список количеств книг у каждого автора
    :param selected_books: Список количества книг, которые нужно выбрать у каждого автора
    :return: Количество способов выбора
    """
    if len(authors_books) != len(selected_books):
        raise ValueError(
            "Списки authors_books и selected_books должны быть одинаковой длины."
        )

    total_ways = 1
    for total_books, books_to_select in zip(authors_books, selected_books):
        ways = combinations(total_books, books_to_select)
        total_ways *= ways

    return total_ways


def seating_arrangements(total_people: int, seats: int, eligible_drivers: int) -> int:
    """
    Вычисляет количество способов рассадить людей в машину с ограничением на водителя.

    :param total_people: Общее количество людей
    :param seats: Количество мест в машине
    :param eligible_drivers: Количество людей, которые могут быть водителем
    :return: Количество способов рассадки
    """
    if total_people != seats:
        raise ValueError("Количество людей и мест должно совпадать!")

    driver_choices = eligible_drivers
    remaining_arrangements = math.factorial(total_people - 1)

    return driver_choices * remaining_arrangements


def count_anagrams(word: str) -> int:
    """
    Вычисляет количество уникальных перестановок букв в слове, учитывая повторяющиеся буквы.

    :param word: Исходное слово
    :return: Количество уникальных слов
    """
    word = word.upper()
    total_letters = len(word)

    letter_counts = Counter(word)
    numerator = math.factorial(total_letters)

    denominator = 1
    for count in letter_counts.values():
        if count > 1:
            denominator *= math.factorial(count)

    return numerator // denominator


def group_partitions(n: int, group_sizes: List[int]) -> int:
    """
    Вычисляет количество способов разбиения множества из n элементов на группы заданных размеров.

    📝 Формула: n! / (n1! * n2! * ... * nk!)

    :param n: Общее количество элементов
    :param group_sizes: Список размеров групп
    :return: Количество способов разбиения
    :raises ValueError: Если сумма размеров групп не равна n
    """
    if not group_sizes:
        raise ValueError("Список размеров групп не может быть пустым.")

    if sum(group_sizes) != n:
        raise ValueError(
            f"Сумма размеров групп ({sum(group_sizes)}) не равна общему количеству элементов ({n})."
        )

    numerator = math.factorial(n)
    denominator = 1
    for size in group_sizes:
        denominator *= math.factorial(size)

    return numerator // denominator
