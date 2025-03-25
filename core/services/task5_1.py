import math


def poisson_formula(n: int, p: float, m: int) -> float:
    """
    Вычисляет вероятность по формуле распределения Пуассона.

    📝 Формула: P(m) = (a^m / m!) * e^(-a), где a = n * p

    :param n: Общее количество испытаний
    :param p: Вероятность успеха в одном испытании
    :param m: Число наступивших событий
    :return: Вероятность появления m событий при параметре a = n * p
    """
    a = round(n * p, 2)
    return (a**m) / math.factorial(m) * math.exp(-a)


def local_moivre_laplace(n: int, p: float, x_target: int) -> float:
    """
    Вычисляет вероятность по локальной теореме Муавра-Лапласа для задачи о количестве успешных событий.

    📝 Формула: P(m) ≈ (1 / σ) * φ(x_m), φ(x) = (1 / √(2π)) * e^(-x² / 2)

    :param n: Общее количество испытаний
    :param p: Вероятность успеха в одном испытании
    :param x_target: Целевое количество успешных событий
    :return: Приближённая вероятность того, что количество успешных событий будет равно x_target
    """
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))

    x_m = (x_target - mu) / sigma
    phi = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x_m**2)

    return (1 / sigma) * phi


def integral_moivre_laplace(n: int, p: float, a: int, b: int) -> float:
    """
    Вычисляет вероятность по интегральной теореме Муавра-Лапласа.

    :param n: Общее количество испытаний (например, количество вызовов)
    :param p: Вероятность успеха в одном испытании (например, вероятность сбоя вызова)
    :param a: Левая граница количества успехов (например, минимальное количество сбойных вызовов)
    :param b: Правая граница количества успехов (например, максимальное количество сбойных вызовов)
    :return: Приближённая вероятность того, что количество успехов окажется в интервале [a, b]
    """

    def laplace(x):
        """Функция Лапласа через функцию ошибок"""
        return 0.5 * (1 + math.erf(x / math.sqrt(2)))

    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))

    x_a = (a - mu) / sigma
    x_b = (b - mu) / sigma

    return laplace(x_b) - laplace(x_a)


# TODO Округление по правилам
# TODO Автотесты


def poisson_formatter(n: int, p: float, m: int) -> str:
    """
    Форматирует ответ по теореме Пуассона

    📝 Формат: <a>^<m>/<m>!e^-<a>

    Пример: 2,57^2/2!e^-2,57

    :param n: Общее количество испытаний
    :param p: Вероятность успеха в одном испытании
    :param m: Количество наступивших событий
    :return: Формула Пуассона с параметрами
    """
    a = n * p

    a_str = f"{a:.2f}".replace(".", ",")
    m_str = str(m)

    result = f"{a_str}^{m_str}/{m_str}!e^-{a_str}"
    return result


def local_moivre_laplace_formatter(n: int, p: float, x_target: int) -> str:
    """
    Форматирует ответ по локальной теореме Муавра-Лапласа в виде строки длиной 20 символов.

    📝 Формат: 1/<σ>fi(<|x_m|>)
    Пример: 1/2,57fi(3,48)

    :param n: Общее количество испытаний
    :param p: Вероятность успеха в одном испытании
    :param x_target: Целевое количество успехов
    :return: Формула локальной теоремы Муавра-Лапласа с параметрами
    """
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    x_m = (x_target - mu) / sigma

    sigma_str = f"{sigma:.2f}".replace(".", ",")
    x_m_abs_str = f"{abs(x_m):.2f}".replace(".", ",")

    result = f"1/{sigma_str}fi({x_m_abs_str})"
    return result


def integral_moivre_laplace_formatter(n: int, p: float, x1: int, x2: int) -> str:
    """
    Форматирует ответ по интегральной теореме Муавра-Лапласа в виде строки.

    📝 Формат: Ф_0(<|a|>)±Ф_0(<|b|>)\\\\
    Если a и b одного знака:
    - оба положительные: Ф_0(a) - Ф_0(b)
    - оба отрицательные: -Ф_0(|a|) + Ф_0(|b|)

    Примеры результата:
    Ф_0(3,48)+Ф_0(3,48)
    -Ф_0(3,9)+Ф_0(4)

    :param n: Общее количество испытаний
    :param p: Вероятность успеха в одном испытании
    :param x1: Левая граница количества успехов
    :param x2: Правая граница количества успехов
    :return: Формула интегральной теоремы Муавра-Лапласа с параметрами
    """

    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    a = (x1 - mu) / sigma
    b = (x2 - mu) / sigma

    def format_number(x: float) -> str:
        num_str = f"{abs(x):.2f}".replace(".", ",")
        num_str = num_str.rstrip(",00").rstrip(",0")
        return num_str

    a_str = format_number(a)
    b_str = format_number(b)

    if a < 0 and b < 0:
        result = f"-Ф_0({b_str})+Ф_0({a_str})"
    else:
        result = f"Ф_0({b_str})+Ф_0({a_str})"

    return result
