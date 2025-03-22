import pytest

from core.services import hypergeometric_probability, exam_pass_probability


@pytest.mark.parametrize(
    "total_population, success_population, sample_size, successes_in_sample, expected",
    [
        (50, 5, 10, 1, 0.431),
        (100, 20, 10, 5, 0.022),
        (10, 5, 5, 3, 0.397),
        (20, 10, 5, 0, 0.016),
        (30, 15, 10, 10, 0),
        # Tests
        (30, 15, 14, 5, 0.103),
        (15, 7, 7, 5, 0.091),
        (21, 15, 9, 3, 0.002),
    ],
)
def test_hypergeometric_probability(
    total_population, success_population, sample_size, successes_in_sample, expected
):
    result = hypergeometric_probability(
        total_population, success_population, sample_size, successes_in_sample
    )

    assert round(result, 3) == expected


@pytest.mark.parametrize(
    "total_questions, known_questions, questions_in_ticket, min_correct_answers, expected",
    [
        (5, 2, 3, 2, 0.3),
        (4, 1, 2, 1, 0.5),
        (10, 10, 5, 3, 1.0),
        (10, 0, 5, 1, 0.0),
        (100, 20, 10, 6, 0.004),
        # Tests
        (60, 25, 3, 2, 0.374),
    ],
)
def test_exam_pass_probability(
    total_questions, known_questions, questions_in_ticket, min_correct_answers, expected
):
    result = exam_pass_probability(
        total_questions, known_questions, questions_in_ticket, min_correct_answers
    )

    assert round(result, 3) == expected
