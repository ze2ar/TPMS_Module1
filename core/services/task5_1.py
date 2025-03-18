import math

# TODO Check all functions
# TODO Refactor formatters, right amount of \ or just delete it (outer func)


def poisson_formula(a: float, m: int) -> float:
    """
    Вычисляет вероятность по формуле распределения Пуассона.

    📝 Формула: P(m) = (a^m / m!) * e^(-a)

    :param a: Среднее количество событий за интервал (математическое ожидание)
    :param m: Количество наступивших событий
    :return: Вероятность появления m событий при параметре a

    Пример:
    a = 2.57
    m = 2

    Вычисление:
    P(2) = (2.57^2 / 2!) * e^(-2.57)
         ≈ (6.6049 / 2) * e^(-2.57)
         ≈ 3.30245 * 0.0767
         ≈ 0.2532

    Ответ: 0.2532
    """
    return (a**m) / math.factorial(m) * math.exp(-a)


def local_moivre_laplace(sigma: float, x_m: float) -> float:
    """
    Вычисляет вероятность по локальной теореме Муавра-Лапласа.

    📝 Формула: P(m) ≈ (1 / σ) * φ(x_m)

    Где φ(x) = (1 / √(2π)) * e^(-x² / 2)

    :param sigma: Стандартное отклонение (σ)
    :param x_m: Нормированное значение отклонения (x_m)
    :return: Приближённая вероятность по локальной теореме Муавра-Лапласа

    Пример:
    sigma = 2.57
    x_m = -3.48

    Вычисление:
    φ(3.48) = (1 / √(2π)) * e^(-(3.48)² / 2)
            ≈ (1 / 2.5066) * e^(-6.0552)
            ≈ 0.3989 * 0.00234
            ≈ 0.0009337

    P ≈ (1 / 2.57) * 0.0009337
      ≈ 0.0003633

    Ответ: 0.0003633
    """
    phi = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x_m**2)
    return (1 / sigma) * phi


def integral_moivre_laplace(a: float, b: float) -> float:
    """
    Вычисляет вероятность по интегральной теореме Муавра-Лапласа.

    📝 Формула: P(a < x < b) ≈ Φ(b) - Φ(a)

    Где Φ(x) — функция Лапласа (интегральная функция распределения стандартного нормального распределения),
    обладающая свойством чётности:
    Φ(-x) = -Φ(x)

    При отрицательных границах используется это свойство:
    - Если обе границы отрицательные (a < 0 и b < 0), то вероятность считается как -Φ(b) + Φ(a)
    - Если одна граница положительная, применяется стандартное Φ(b) - Φ(a)

    :param a: Левая граница нормированного значения (a)
    :param b: Правая граница нормированного значения (b)
    :return: Вероятность того, что случайная величина попадёт в интервал [a, b]

    Примеры:

    1️⃣ a = -3.48, b = 3.48

    Вычисление:
    Φ(3.48) ≈ 0.99975
    Φ(-3.48) = -0.99975 (по свойству чётности)

    P ≈ Φ(3.48) - Φ(-3.48)
      ≈ 0.99975 - (-0.99975)
      ≈ 1.9995

    Ответ: 1.9995 (погрешность приближённого метода)

    2️⃣ a = -4, b = -3.9

    Вычисление:
    Φ(-4.0) = -Φ(4.0) ≈ -0.99997
    Φ(-3.9) = -Φ(3.9) ≈ -0.99995

    P ≈ Φ(-3.9) - Φ(-4.0)
      ≈ -0.99995 - (-0.99997)
      ≈ 0.00002

    Ответ: 0.00002
    """

    def laplace(x):
        return 0.5 * (1 + math.erf(x / math.sqrt(2)))

    return laplace(b) - laplace(a)


def poisson_formatter(a: float, m: int) -> str:
    """
    Форматирует ответ по теореме Пуассона в виде строки длиной 20 символов.

    📝 Формат: <a>^<m>/<m>!e^-<a>\\\\

    Пример: 2,57^2/2!e^-2,57\\\\

    :param a: Среднее количество событий (a)
    :param m: Количество наступивших событий (m)
    :return: Строка длиной 20 символов
    """
    a_str = f"{a:.2f}".replace(".", ",")
    m_str = str(m)

    result = f"{a_str}^{m_str}/{m_str}!e^-{a_str}"
    result = result.ljust(20, "\\")  # Дополняем до 20 символов символом '\'

    return result


def local_moivre_laplace_formatter(sigma: float, x_m: float) -> str:
    """
    Форматирует ответ по локальной теореме Муавра-Лапласа в виде строки длиной 20 символов.

    📝 Формат: 1/<σ>fi(<|x_m|>)\\\\

    Пример: 1/2,57fi(3,48)\\\\\\\\\

    :param sigma: Стандартное отклонение (σ)
    :param x_m: Нормированное значение отклонения (x_m)
    :return: Строка длиной 20 символов
    """
    sigma_str = f"{sigma:.2f}".replace(".", ",")
    x_m_abs_str = f"{abs(x_m):.2f}".replace(".", ",")

    result = f"1/{sigma_str}fi({x_m_abs_str})"
    result = result.ljust(20, "\\")

    return result


def integral_moivre_laplace_formatter(a: float, b: float) -> str:
    """
    Форматирует ответ по интегральной теореме Муавра-Лапласа в виде строки длиной 20 символов.

    📝 Формат: Ф_0(<|a|>)±Ф_0(<|b|>)\\\\

    Если a и b одного знака:
    - оба положительные: Ф_0(a) - Ф_0(b)
    - оба отрицательные: -Ф_0(|a|) + Ф_0(|b|)

    Примеры результата:
    Ф_0(3,48)+Ф_0(3,48)\\\\\\
    -Ф_0(3,9)+Ф_0(4)\\\\\\\\\

    :param a: Левая граница нормированного значения (a)
    :param b: Правая граница нормированного значения (b)
    :return: Строка длиной 20 символов
    """

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

    result = result.ljust(20, "\\")

    return result
