from typing import Callable
import scipy.integrate as integrate


def meeting_probability(start_time: int, end_time: int, wait_time: int) -> float:
    """
    Рассчитывает вероятность того, что встреча состоится.

    📝 Формула: P = (T - W)² / T²
    - T — общее время (в минутах), в пределах которого двое людей могут прибыть.
    - W — максимальное время ожидания (в минутах).

    :param start_time: Время начала встречи (в часах).
    :param end_time: Время окончания встречи (в часах).
    :param wait_time: Максимальное время ожидания (в минутах).
    :return: Вероятность того, что встреча состоится (от 0 до 1).
    """
    total_time = (end_time - start_time) * 60

    total_area = total_time * total_time
    allowed_area = (total_time - wait_time) * (total_time - wait_time)

    return 1 - allowed_area / total_area


def probability_of_condition(
    start: float, end: float, condition_func: Callable, sign: str
) -> float:
    """
    Вычисляет вероятность выполнения заданного условия в пределах интервала [start, end],
    используя интегрирование для нахождения площади, где условие выполняется.

    Функция рассматривает значения condition_func(x) на интервале [start, end] и определяет
    области, где выполняется заданное условие ('>' или '<'). После этого она вычисляет
    отношение площади этих областей к полной площади интервала.

    📝 Формула нормализации: probability = площадь_под_кривой / (end - start)^2

    :param start: Левая граница интервала интегрирования по оси X.

    :param end: Правая граница интервала интегрирования по оси X.

    :param condition_func:
        Функция условия, принимающая одно значение `x` и возвращающая `y`.
        Определяет зависимость между x и y, по которой будет проверяться выполнение условия.

    :param sign:
        Строка-сравнение, определяющая направление условия:
            - '>' : учитываются случаи, когда condition_func(x) < end.
            - '<' : учитываются случаи, когда condition_func(x) > start.
        Любое другое значение приводит к возбуждению исключения ValueError.

    :return:
        Вероятность выполнения условия на интервале [start, end].
        Рассчитывается как отношение площади, где выполняется условие, к полной площади области.

    :raises ValueError:
        Если передан неизвестный знак сравнения в параметр `sign`.
    """

    def integrand(x):
        condition_y = condition_func(x)

        if sign == ">":
            if condition_y >= end:
                return 0
            if condition_y <= start:
                return end - start
            return end - condition_y

        elif sign == "<":
            if condition_y <= start:
                return 0
            if condition_y >= end:
                return end - start
            return condition_y - start

        else:
            raise ValueError("Неизвестный знак сравнения")

    area_under_curve = integrate.quad(integrand, start, end)
    total_area = (end - start) * (end - start)

    return area_under_curve[0] / total_area
