from pydantic import BaseModel, Field


class PermutationsRequest(BaseModel):
    """
    Модель для расчета числа перестановок (размещений).
    """

    n: int = Field(ge=0, description="Общее количество элементов", examples=[5])
    k: int = Field(ge=0, description="Количество выбираемых элементов", examples=[3])


class CombinationsRequest(BaseModel):
    """
    Модель для расчета числа сочетаний.
    """

    n: int = Field(ge=0, description="Общее количество элементов", examples=[6])
    k: int = Field(ge=0, description="Количество выбираемых элементов", examples=[4])


class CombinationsWithRepetitionRequest(BaseModel):
    """
    Модель для расчета числа сочетаний с повторениями.
    """

    n: int = Field(
        ge=1, description="Количество сортов (различных элементов)", examples=[4]
    )
    k: int = Field(
        ge=0, description="Количество элементов, которые нужно выбрать", examples=[7]
    )
