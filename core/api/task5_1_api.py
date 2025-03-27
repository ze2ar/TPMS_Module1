from fastapi import APIRouter
import math

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
    Применяется на небольших данных

    📝 Формула: `P(m) ≈ a^m / m! * e^(-a)`

    ℹ️ Где:
     - a - математическое ожидание (n*p)

    Параметры:
    - n — Общее количество испытаний
    - p — Вероятность успеха в одном испытании
    - m — Число наступлений события

    
    📚 Примеры:
    1. Если n = 900, p = 0.005, m = 3, результат: `"2,57^3/3!e^-2,57"`
    """,
    response_description="Форматированный результат по формуле Пуассона.",
)
def api_poisson_formula(request: PoissonRequest):
    return poisson_formatter(n=request.n, p=request.p, m=request.m)


@router.post(
    "/local-moivre-laplace",
    response_model=str,
    summary="Локальная теорема Муавра-Лапласа",
    description="""
    📌 **Описание**:

    Вычисляет вероятность по локальной теореме Муавра-Лапласа.
    Применяется на значительных данных.

    📝 Формула: `P(m) ≈ 1 / (σ√(2π)) * e^(-x_m²/2)`

    ℹ️ Где:
    - σ — стандартное отклонение (sqrt(n * p * (1 - p)))
    - x_m — нормированное значение ((x_target - n * p) / σ)
    - Функция φ(-x) = φ(x)

    ℹ️ Параметры:
    - n — Общее количество испытаний
    - p — Вероятность успеха в одном испытании
    - m — Целевое количество успехов
    
    📚 Примеры:
    1. Если n = 170, p = 0.55, x_target = 90, результат: `"1/6,49fi(0,54)""`
    """,
    response_description="Форматированный результат по локальной теореме Муавра-Лапласа.",
)
def api_local_moivre_laplace(request: LocalMoivreLaplaceRequest):
    return local_moivre_laplace_formatter(
        n=request.n, p=request.p, x_target=request.x_target
    )


@router.post(
    "/integral-moivre-laplace",
    response_model=str,
    summary="Интегральная теорема Муавра-Лапласа",
    description="""
    📌 **Описание**:

    Вычисляет вероятность того, что случайная величина попадёт в интервал [x1, x2] по интегральной теореме Муавра-Лапласа.

    📝 **Формула:**  
    `P(x1 < X < x2) ≈ Φ(b) - Φ(a)`

    ℹ️ **Где:**  
    - `σ = sqrt(n * p * (1 - p))` — стандартное отклонение  
    - `a = (x1 - n * p) / σ` — нормированное значение для `x1`  
    - `b = (x2 - n * p) / σ` — нормированное значение для `x2`  
    - `Φ(x)` — функция Лапласа, где `Φ(-x) = -Φ(x)`
    
    Параметры:
    - `n` — общее количество испытаний  
    - `p` — вероятность успеха в одном испытании  
    - `x1` — левая граница числа успехов  
    - `x2` — правая граница числа успехов  

    📚 **Пример:**  
    1. Если n = 400, p = 0.1, x1 = 30, x2 = 50, результат: `"Ф_0(3,48)+Ф_0(3,48)"`
    """,
    response_description="Форматированный результат по интегральной теореме Муавра-Лапласа.",
)
def api_integral_moivre_laplace(request: IntegralMoivreLaplaceRequest):
    return integral_moivre_laplace_formatter(
        n=request.n, p=request.p, x1=request.x1, x2=request.x2
    )
