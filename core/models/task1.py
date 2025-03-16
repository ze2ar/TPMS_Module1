from typing import List

from pydantic import BaseModel, Field


class WordRequest(BaseModel):
    """
    Модель для задачи составления новых слов из заданных букв.
    """

    word: str = Field(
        description="Список букв, из которых составляются новые слова",
        examples=["ДИСКЕТА"],
    )
    length: int = Field(
        description="Длина нового слова, которое нужно составить", examples=[5]
    )


class AuthorSelectionRequest(BaseModel):
    """
    Модель для задачи выбора книг у одного автора.
    """

    books_by_authors: List[int] = Field(
        description="Список с количеством книг у каждого автора", examples=[[9, 6, 10]]
    )
    selected_books: int = Field(
        description="Количество книг, которые нужно выбрать у одного автора",
        examples=[2],
    )


class AuthorMultipleSelectionRequest(BaseModel):
    """
    Модель для задачи выбора книг у нескольких авторов.
    """

    authors_books: List[int] = Field(
        description="Список с количеством книг у каждого автора", examples=[[9, 6, 10]]
    )
    selected_books: List[int] = Field(
        description="Сколько книг нужно выбрать у каждого автора (по порядку)",
        examples=[[1, 2, 3]],
    )


class SeatingRequest(BaseModel):
    """
    Модель для задачи рассадки людей по местам.
    """

    total_people: int = Field(
        description="Общее количество людей, которые рассаживаются по местам",
        examples=[6],
    )
    seats: int = Field(
        description="Общее количество мест в машине (включая водителя)", examples=[6]
    )
    eligible_drivers: int = Field(
        description="Количество людей, которые могут быть водителем", examples=[3]
    )


class BouquetRequest(BaseModel):
    """
    Модель для задачи составления букета.
    """

    flowers_in_bouquet: int = Field(
        description="Количество цветов в букете", examples=[7]
    )
    flower_types: int = Field(
        description="Количество различных видов цветов", examples=[4]
    )


class AnagramRequest(BaseModel):
    """
    Модель для задачи генерации анаграмм.
    """

    word: str = Field(
        description="Слово, из которого составляются перестановки",
        examples=["ВЕРОЯТНОСТЬ"],
    )


class CommitteeRequest(BaseModel):
    """
    Модель запроса на выбор комиссии.
    """

    people_count: int = Field(ge=0, description="Общее количество людей", examples=[9])
    committee_size: int = Field(ge=0, description="Размер комиссии", examples=[3])
