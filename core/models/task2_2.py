from pydantic import BaseModel, Field


class MeetingProbabilityRequest(BaseModel):
    """
    Модель для расчета вероятности встречи во временной промежуток (от/до, ч.)
    с максимальным временем ожидания.
    """

    start_time: int = Field(
        ge=0,
        le=24,
        description="Время начала встречи (в часах, от 0 до 24)",
        examples=[13],
    )
    end_time: int = Field(
        ge=0,
        le=24,
        description="Время окончания встречи (в часах, от 0 до 24)",
        examples=[20],
    )
    wait_time: int = Field(
        ge=0, description="Максимальное время ожидания (в минутах)", examples=[22]
    )


class ProbabilityRequest(BaseModel):
    """
    Модель для расчета вероятности в диапазоне чисел по условию.
    """

    start: int = Field(description="Начало диапазона чисел", examples=[0])
    end: int = Field(description="Конец диапазона чисел", examples=[9])
    condition: str = Field(
        description="Условие вида f(x), например '7/x'", examples=["7/x"]
    )
    sign: str = Field(description="Знак", examples=["<"])
