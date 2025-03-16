from fastapi import APIRouter

from core.services import hypergeometric_probability, exam_pass_probability
from core.models import ExamProbabilityRequest, HypergeometricRequest

router = APIRouter(prefix="/task2_1", tags=["Task2_1"])


@router.post(
    "/exam-pass-probability",
    response_model=float,
    summary="Вероятность сдать экзамен",
    description="""
    Рассчитывает вероятность сдать экзамен по гипергеометрическому распределению.
    
    📝 Формула: P(X = k) = (C(m, k) * C(N - m, n - k)) / C(N, n)
    - **N** — общее количество вопросов.
    - **K** — количество вопросов, которые знает студент.
    - **n** — количество билетов.
    - **k** — количество билетов, на которые нужно ответить.
    
    📚 Пример: студент знает 25 из 60 вопросов. В билете 3 вопроса, нужно ответить как минимум на 2.
    """,
    response_description="Вероятность сдать экзамен (от 0 до 1).",
)
def api_exam_pass_probability(request: ExamProbabilityRequest):
    return exam_pass_probability(
        total_questions=request.total_questions,
        known_questions=request.known_questions,
        questions_in_ticket=request.questions_in_ticket,
        min_correct_answers=request.min_correct_answers,
    )


@router.post(
    "/hypergeometric",
    response_model=float,
    summary="Вероятность гипергеометрического распределения",
    description="""
    Рассчитывает вероятность гипергеометрического распределения.
    
    📝 Формула: P(X = k) = (C(m, k) * C(N - m, n - k)) / C(N, n)
    - **N** — общее количество объектов (например, всего шаров).
    - **K** — количество объектов с нужным признаком (например, белых шаров).
    - **n** — размер выборки (например, сколько достаем шаров).
    - **k** — количество объектов с нужным признаком в выборке (например, сколько белых шаров достали).

    #### Пример:
    В урне 30 шаров, из них 15 белых и 15 черных. Извлекаем 14 шаров.
    Какова вероятность того, что среди них окажется ровно 5 белых?
    """,
    response_description="Вероятность события (от 0 до 1)",
)
def api_hypergeometric_probability(request: HypergeometricRequest):
    result = hypergeometric_probability(
        total_population=request.total_population,
        success_population=request.success_population,
        sample_size=request.sample_size,
        successes_in_sample=request.successes_in_sample,
    )
    return round(result, 3)
