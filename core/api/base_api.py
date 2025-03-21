from fastapi import APIRouter

from core.models import *
from core.services import *

router = APIRouter(prefix="/base", tags=["Base"])


@router.post(
    "/permutations",
    summary="Перестановки из n",
    description="Вычисляет количество перестановок из n.",
    response_description="Количество перестановок",
    response_model=int,
)
def api_permutations(request: PermutationsRequest):
    """
    Подсчет перестановок из n элементов.

    📝 Формула: P(n) = n!
    Где:
    - **n**: общее количество элементов
    """
    return permutations(n=request.n)


@router.post(
    "/arrangements",
    summary="Размещения из n по k",
    description="Вычисляет количество размещений из n по k элементов.",
    response_description="Количество размещений",
    response_model=int,
)
def api_arrangements(request: ArrangementsRequest):
    """
    Подсчет размещений из n по k.

    📝 Формула: A(n, k) = n! / (n - k)!
    - **n**: общее количество элементов
    - **k**: количество выбираемых элементов
    """
    return arrangements(n=request.n, k=request.k)


@router.post(
    "/combinations",
    summary="Сочетания из n по k",
    description="Вычисляет количество сочетаний из n по k элементов.",
    response_description="Количество сочетаний",
    response_model=int,
)
def api_combinations(request: CombinationsRequest):
    """
    Подсчет сочетаний из n по k.

    📝 Формула: C(n, k) = n! / (k! * (n - k)!)
    Где:
    - **n**: общее количество элементов
    - **k**: количество выбираемых элементов
    """
    return combinations(n=request.n, k=request.k)


@router.post(
    "/combinations-with-repetition",
    summary="Сочетания с повторениями",
    description="Вычисляет количество сочетаний с повторениями из n сортов по k элементов.",
    response_description="Количество сочетаний с повторениями",
    response_model=int,
)
def api_combinations_with_repetition(request: CombinationsWithRepetitionRequest):
    """
    Подсчет сочетаний с повторениями из n сортов по k.

    📝 Формула: C(n + k - 1, k) = (n + k - 1)! / (k! * (n - 1)!)
    Где:
    - **n**: количество сортов
    - **k**: количество выбираемых элементов
    """
    return combinations_with_repetition(n=request.n, k=request.k)
