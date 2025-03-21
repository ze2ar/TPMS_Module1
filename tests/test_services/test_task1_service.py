import pytest

from core.services import (
    count_words,
    count_same_author_selection,
    count_author_selection,
    seating_arrangements,
    count_anagrams,
    group_partitions,
)


@pytest.mark.parametrize(
    "word, length, expected",
    [
        ("abc", 2, 6),
        ("aabbcc", 3, 6),
        ("xyz", 1, 3),
        ("aaa", 1, 1),
        ("abcdef", 0, 1),
        # Test
        ("ДИСКЕТА", 5, 2520),
        ("ДИСКРЕТНЫЙ", 4, 5040),
        ("ВЕРШИНА", 4, 840),
        ("КОМПЬЮТЕР", 4, 3024),
        ("ВЕРОЯТНЫЙ", 3, 504),
    ],
)
def test_count_words(word, length, expected):
    assert count_words(word, length) == expected


@pytest.mark.parametrize(
    "books_by_authors, selected_books, expected",
    [
        ([5, 10, 15], 2, 160),
        ([3, 7], 1, 10),
        ([4, 4, 4], 3, 12),
        ([0, 5], 1, 5),
        ([1, 1, 1], 1, 3),
        # Test
        ([7, 9, 8], 2, 85),
        ([7, 9, 8], 3, 175),
        ([11, 10, 6], 3, 305),
        ([10, 7, 11], 2, 121),
    ],
)
def test_count_same_author_selection(books_by_authors, selected_books, expected):
    assert count_same_author_selection(books_by_authors, selected_books) == expected


@pytest.mark.parametrize(
    "authors_books, selected_books, expected",
    [
        ([5, 10], [1, 2], 225),
        ([3, 4, 5], [1, 1, 1], 60),
        ([6], [3], 20),
        ([2, 3], [0, 2], 3),
        # Test
        ([6, 8, 7], [1, 2, 3], 5880),
        ([8, 5, 9], [1, 2, 3], 6720),
        ([9, 6, 10], [1, 2, 3], 16200),
        ([9, 7, 10], [1, 2, 3], 22680),
        ([11, 10, 6], [1, 2, 3], 9900),
    ],
)
def test_count_author_selection(authors_books, selected_books, expected):
    assert count_author_selection(authors_books, selected_books) == expected


@pytest.mark.parametrize(
    "total_people, seats, eligible_drivers, expected",
    [
        (5, 5, 2, 48),
        (3, 3, 1, 2),
        (4, 4, 4, 24),
        # Test
        (5, 5, 1, 24),
        (5, 5, 4, 96),
        (6, 6, 3, 360),
        (5, 5, 2, 48),
        (5, 5, 3, 72),
    ],
)
def test_seating_arrangements(total_people, seats, eligible_drivers, expected):
    assert seating_arrangements(total_people, seats, eligible_drivers) == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("abc", 6),
        ("aabb", 6),
        ("aaaa", 1),
        ("ab", 2),
        ("aabbb", 10),
        # Test
        ("ВЕРОЯТНОСТЬ", 9979200),
        ("КОМБИНАТ", 40320),
        ("КОНСУЛЬТАЦИЯ", 479001600),
        ("ВЫЧИТАНИЕ", 181440),
        ("МАГИСТР", 5040),
        ("УМНОЖЕНИЕ", 90720),
        ("ЕВРОПА", 720),
        ("УРАВНЕНИЕ", 90720),
        ("ТЯНУЧКА", 5040),
    ],
)
def test_count_anagrams(word, expected):
    assert count_anagrams(word) == expected


@pytest.mark.parametrize(
    "n, group_sizes, expected",
    [
        (6, [2, 2, 2], 90),
        (4, [1, 3], 4),
        (5, [2, 3], 10),
        (7, [1, 2, 4], 105),
        (3, [1, 1, 1], 6),
        (5, [5], 1),
        (1, [1], 1),
        # Tests
        (15, [7, 4, 4], 450450),
    ],
)
def test_group_partitions(n, group_sizes, expected):
    assert group_partitions(n, group_sizes) == expected
