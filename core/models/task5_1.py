from pydantic import BaseModel, Field


class PoissonRequest(BaseModel):
    """
    Модель для расчета вероятности по формуле Пуассона.
    """

    a: float = Field(
        description="Среднее число событий за интервал времени (λ)", examples=[2.57]
    )
    m: int = Field(ge=0, description="Число наступлений события (m)", examples=[2])


class LocalMoivreLaplaceRequest(BaseModel):
    """
    Модель для расчета вероятности по локальной теореме Муавра-Лапласа.
    """

    sigma: float = Field(
        description="Среднеквадратическое отклонение (σ)", examples=[2.57]
    )
    x_m: float = Field(description="Стандартизированное значение x_m", examples=[-3.48])


class IntegralMoivreLaplaceRequest(BaseModel):
    """
    Модель для расчета вероятности по интегральной теореме Муавра-Лапласа.
    """

    a: float = Field(
        description="Левая граница нормированного значения", examples=[-3.48]
    )
    b: float = Field(
        description="Правая граница нормированного значения", examples=[3.48]
    )
