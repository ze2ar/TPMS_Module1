from pydantic import BaseModel, Field


class ExamProbabilityRequest(BaseModel):
    """
    Модель для расчета вероятности сдачи экзамена.
    """

    total_questions: int = Field(
        ge=1, description="Общее количество вопросов на экзамене", examples=[60]
    )

    known_questions: int = Field(
        ge=0, description="Количество вопросов, которые знает студент", examples=[25]
    )

    questions_in_ticket: int = Field(
        ge=1, description="Количество вопросов в билете", examples=[3]
    )

    min_correct_answers: int = Field(
        ge=0,
        description="Минимальное количество правильных ответов для сдачи экзамена",
        examples=[2],
    )


class HypergeometricRequest(BaseModel):
    """
    Модель для расчета вероятности гипергеометрического распределения
    """

    total_population: int = Field(
        ge=1,
        description="Общее количество объектов",
        examples=[30],
    )
    success_population: int = Field(
        ge=0,
        description="Количество объектов с нужным признаком",
        examples=[15],
    )
    sample_size: int = Field(
        ge=1,
        description="Размер выборки",
        examples=[14],
    )
    successes_in_sample: int = Field(
        ge=0,
        description="Количество успешных исходов в выборке",
        examples=[5],
    )
