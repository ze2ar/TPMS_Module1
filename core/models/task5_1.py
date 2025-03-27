from pydantic import BaseModel, Field


class PoissonRequest(BaseModel):
    """
    Модель для расчета вероятности по формуле Пуассона.
    """

    n: int = Field(
        ge=0,
        description="Общее количество испытаний",
        examples=[900],
    )
    p: float = Field(
        ge=0, le=1, description="Вероятность успеха в одном испытании", examples=[0.005]
    )
    m: int | None = Field(
        default=None,
        ge=0,
        description="Число наступлений события (опционально, если None, то P(X >= 1))",
        examples=[3],
    )


class LocalMoivreLaplaceRequest(BaseModel):
    """
    Модель для расчета вероятности по локальной теореме Муавра-Лапласа.
    """

    n: int = Field(ge=0, description="Общее количество испытаний", examples=[170])
    p: float = Field(
        ge=0, le=1, description="Вероятность успеха в одном испытании", examples=[0.55]
    )
    x_target: int = Field(
        ge=0, description="Целевое количество успехов (x)", examples=[90]
    )


class IntegralMoivreLaplaceRequest(BaseModel):
    """
    Модель для расчета вероятности по интегральной теореме Муавра-Лапласа.
    """

    n: int = Field(ge=0, description="Общее количество испытаний", examples=[400])
    p: float = Field(
        ge=0, le=1, description="Вероятность успеха в одном испытании", examples=[0.1]
    )
    x1: int = Field(ge=0, description="Левая граница количества успехов", examples=[30])
    x2: int | None = Field(
        default=None,
        ge=0,
        description="Правая граница количества успехов (опционально, если None, то P(X >= x1))",
        examples=[50],
    )
