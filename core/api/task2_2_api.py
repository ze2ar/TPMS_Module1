from fastapi import APIRouter
import numpy as np

from core.models import MeetingProbabilityRequest, ProbabilityRequest
from core.services import meeting_probability, probability_of_condition

router = APIRouter(prefix="/task2_2", tags=["Task2_2"])


@router.post(
    "/meeting-probability",
    response_model=float,
    summary="Вероятность встречи",
    description="""
    Вычисляет вероятность того, что встреча состоится,
    если два человека приходят случайным образом в пределах указанного времени
    и соглашаются ждать друг друга не более заданного времени.
    
    📚 Пример:Двое условились встретиться между 13 и 20 часами, причем договорились ждать
    друг друга не более 22 минут. Считая, что момент прихода на встречу выбирается
    каждым «наудачу» в пределах указанного времени, найдите вероятность того, что
    встреча состоится. (Ответ округлите до 3 знаков после запятой)
    """,
    response_description="Вероятность встречи (от 0 до 1)",
)
def api_meeting_probability(request: MeetingProbabilityRequest):
    probability = meeting_probability(
        start_time=request.start_time,
        end_time=request.end_time,
        wait_time=request.wait_time,
    )

    return round(probability, 3)


@router.post(
    "/probability",
    response_model=float,
    summary="Вероятность для произвольного условия y ? f(x)",
    description="""
    Рассчитывает вероятность того, что для случайных чисел x и y,
    y ? f(x), где x — случайное число из диапазона от start до end. 
    Условие f(x) передается как строка. ? - знак.
    
    📚 Пример: Загадываются два числа x и y в промежутке от 0 до 9. Какова вероятность, что y < \frac{7}{x}? 
    (Ответ округлите до 3 знаков после запятой)
    """,
    response_description="Вероятность того, что y < f(x) (от 0 до 1).",
)
def api_probability(request: ProbabilityRequest):
    probability = probability_of_condition(
        start=request.start,
        end=request.end,
        condition_func=eval(f"lambda x: {request.condition}", {"x": 0, "np": np}),
        sign=request.sign,
    )

    return round(probability, 3)
