from fastapi import APIRouter

from core.models import *
from core.services import *

router = APIRouter(prefix="/task1", tags=["Task1"])


@router.post(
    "/count-words",
    response_model=int,
    summary="Подсчет уникальных слов",
    description="""
    Вычисляет количество уникальных \"слов\", которые можно составить 
    из неповторяющихся букв исходного слова, заданной длины.
    
    📚 Пример: Сколько «слов» можно образовать из букв слова ДИСКЕТА, если «слова» должны состоять из 5 букв?
    """,
    response_description="Количество возможных слов",
)
def api_count_words(request: WordRequest):
    return count_words(word=request.word, length=request.length)


@router.post(
    "/count-same-author-selection",
    response_model=int,
    summary="Выбор книг одного автора",
    description="""
    Вычисляет количество способов выбрать заданное количество книг у одного автора из списка авторов.
    
    📚 Пример: Имеется 7 разных книг Пушкина, 9 — Лермонтова, 8 — Чехова.  Каким числом 
    способов можно выбрать две книги одного автора?
    """,
    response_description="Количество способов выбора книг одного автора",
)
def api_count_same_author_selection(request: AuthorSelectionRequest):
    return count_same_author_selection(
        books_by_authors=request.books_by_authors, selected_books=request.selected_books
    )


@router.post(
    "/count-author-selection",
    response_model=int,
    summary="Выбор книг у нескольких авторов",
    description="""
    Подсчитывает количество способов выбрать определенное количество книг у каждого автора из списка.
    
    📚 Пример: Имеется 6 разных книг Пушкина, 8 — Лермонтова, 7 — Чехова. Каким числом
    способов можно выбрать 1 книгу Пушкина, две — Лермонтова, три — Чехова?
    """,
    response_description="Количество способов выбора книг у нескольких авторов",
)
def api_count_author_selection(request: AuthorMultipleSelectionRequest):
    return count_author_selection(
        authors_books=request.authors_books, selected_books=request.selected_books
    )


@router.post(
    "/seating-arrangements",
    response_model=int,
    summary="Рассадка в машину с ограничением на водителя",
    description="""
    Вычисляет количество способов рассадить людей в машину, учитывая ограничение,
    что водителем может быть только определённое количество людей.
    
    📚 Пример: В автомашине 5 мест, включая место водителя. Сколькими способами 5 человек
    могут усесться в эту машину, если занять место водителя может только 1 человек?
    """,
    response_description="Количество способов рассадки людей в машину",
)
def api_seating_arrangements(request: SeatingRequest):
    return seating_arrangements(
        total_people=request.total_people,
        seats=request.seats,
        eligible_drivers=request.eligible_drivers,
    )


@router.post(
    "/bouquet-combinations",
    response_model=int,
    summary="Комбинации букетов из цветов",
    description="""
    Вычисляет количество способов составить букет из цветов разных сортов, 
    с возможностью повторения цветов.
    
    📚 Пример: Сколькими способами можно составить букет из 11 цветов, если в наличии есть
    цветы 5 сортов?     
    """,
    response_description="Количество способов составления букета",
)
def api_bouquet_combinations(request: BouquetRequest):
    return combinations_with_repetition(
        n=request.flower_types, k=request.flowers_in_bouquet
    )


@router.post(
    "/anagram",
    response_model=int,
    summary="Подсчет уникальных перестановок букв",
    description="""
    Подсчитывает количество уникальных слов, которые можно получить перестановкой всех букв во входном слове.
    Учитываются одинаковые буквы, поэтому используется формула перестановок с повторениями.
    
    📚 Пример: Сколько различных «слов» можно получить, переставляя буквы в слове ВЕРОЯТНОСТЬ?
    """,
    response_description="Количество уникальных слов (перестановок)",
)
def api_count_anagrams(request: AnagramRequest):
    return count_anagrams(word=request.word)


@router.post(
    "/count-committee",
    response_model=int,
    summary="Подсчет способов выбора комиссии",
    description="""
    Вычисляет количество способов выбрать комиссию из заданного количества человек.
    Используются сочетания без повторений по формуле C(n, k).
    
    📚 Пример: Сколькими способами из 9 человек можно избрать комиссию, состоящую из 3 членов?
    """,
    response_description="Количество способов выбора комиссии",
)
def api_count_committee(request: CommitteeRequest):
    return combinations(n=request.people_count, k=request.committee_size)
