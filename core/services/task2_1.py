from core.services import combinations


def hypergeometric_probability(
    total_population: int,  # N
    success_population: int,  # m
    sample_size: int,  # n
    successes_in_sample: int,  # k
) -> float:
    """
    Вычисляет вероятность по формуле гипергеометрического распределения.

    📝 Формула: P(X = k) = (C(m, k) * C(N - m, n - k)) / C(N, n)

    :param total_population: Общее количество элементов в генеральной совокупности (N)
    :param success_population: Количество успешных элементов (m)
    :param sample_size: Размер выборки (n)
    :param successes_in_sample: Число успешных исходов в выборке (k)
    :return: Вероятность получить successes_in_sample успешных исходов
    """
    comb_successes = combinations(success_population, successes_in_sample)
    comb_failures = combinations(
        total_population - success_population, sample_size - successes_in_sample
    )
    comb_total = combinations(total_population, sample_size)

    return (comb_successes * comb_failures) / comb_total


def exam_pass_probability(
    total_questions: int,
    known_questions: int,
    questions_in_ticket: int,
    min_correct_answers: int,
) -> float:
    """
    Вычисляет вероятность сдать экзамен, ответив минимум на min_correct_answers вопросов.

    Используется гипергеометрическое распределение для подсчета вероятностей.

    :param total_questions: Общее количество вопросов на экзамене (N)
    :param known_questions: Количество вопросов, которые студент знает (m)
    :param questions_in_ticket: Количество вопросов в билете (n)
    :param min_correct_answers: Минимальное количество правильных ответов для сдачи экзамена
    :return: Вероятность сдачи экзамена
    """
    probability = 0
    for k in range(min_correct_answers, questions_in_ticket + 1):
        prob_k = hypergeometric_probability(
            total_population=total_questions,
            success_population=known_questions,
            sample_size=questions_in_ticket,
            successes_in_sample=k,
        )
        probability += prob_k

    return round(probability, 3)
