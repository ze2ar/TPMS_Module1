from fastapi import APIRouter

from core.models import (
    PoissonRequest,
    LocalMoivreLaplaceRequest,
    IntegralMoivreLaplaceRequest,
)
from core.services import (
    poisson_formatter,
    local_moivre_laplace_formatter,
    integral_moivre_laplace_formatter,
)

router = APIRouter(prefix="/task5_1", tags=["task5_1"])


@router.post(
    "/poisson-formula",
    response_model=str,
    summary="Теорема Пуассона",
    description="""
    📌 **Описание**:

    Вычисляет вероятность по теореме Пуассона.

    📝 Формула: `P(m) ≈ a^m / m! * e^(-a)`

    ℹ️ Где:
    - a — математическое ожидание
    - m — количество наступлений события

    📚 Примеры:
    1. Если a = 2.57, m = 2, результат: `"2,57^2/2!e^-2,57\\\\"`
    """,
    response_description="Форматированный результат по формуле Пуассона.",
)
def api_poisson_formula(request: PoissonRequest):
    return poisson_formatter(request.a, request.m)


@router.post(
    "/local-moivre-laplace",
    response_model=str,
    summary="Локальная теорема Муавра-Лапласа",
    description="""
    📌 **Описание**:

    Вычисляет вероятность по локальной теореме Муавра-Лапласа.

    📝 Формула: `P(m) ≈ 1 / (σ√(2π)) * e^(-x_m²/2)`

    ℹ️ Где:
    - σ — стандартное отклонение
    - x_m — нормированное значение
    - Функция φ(-x) = φ(x)

    📚 Примеры:
    1. Если σ = 2.57, x_m = -3.48, результат: `"1/2,57fi(3,48)\\\\"`
    """,
    response_description="Форматированный результат по локальной теореме Муавра-Лапласа.",
)
def api_local_moivre_laplace(request: LocalMoivreLaplaceRequest):
    return local_moivre_laplace_formatter(request.sigma, request.x_m)


@router.post(
    "/integral-moivre-laplace",
    response_model=str,
    summary="Интегральная теорема Муавра-Лапласа",
    description="""
    📌 **Описание**:

    Вычисляет вероятность того, что случайная величина попадёт в интервал [a, b] по интегральной теореме Муавра-Лапласа.

    📝 Формула: `P(a < x < b) ≈ Φ(b) - Φ(a)`

    ℹ️ Свойство функции: Φ(-x) = -Φ(x)

    📚 Примеры:
    1. Если a = -3.48 и b = 3.48, результат: `"Ф_0(3,48)+Ф_0(3,48)\\\\"`
    2. Если a = -4 и b = -3.9, результат: `"-Ф_0(3,9)+Ф_0(4)\\\\"`
    """,
    response_description="Форматированный результат по интегральной теореме Муавра-Лапласа.",
)
def api_integral_moivre_laplace(request: IntegralMoivreLaplaceRequest):
    return integral_moivre_laplace_formatter(request.a, request.b)
