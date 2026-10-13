from pydantic import BaseModel, Field


class RecipeBase(BaseModel):
    title: str = Field(
        ...,
        title="Название блюда",
        description="Тут нужно написать название рецепта",
        examples=["Борщ"]
    )
    cooking_time: int = Field(
        ...,
        title="Время приготовления",
        description="Время, необходимое для приготоввления блюда в минутах",
        gt=0,
        examples=[45]
    )


class RecipeCreate(RecipeBase):
    """Формат тела запроса для создания рецепта (POST /recipes)."""
    ingredients: str = Field(
        ..., 
        title="Список ингредиентов", 
        description="Перечень продуктов строкой",
        examples=["Мясо 500г, Картошка 300г, Свекла 100г, ..."]
    )
    description: str = Field(
        ...,
        title="Текстовое описание", 
        description="Пошаговый процесс приготовления блюда",
        examples=["1. Сварите мясо. 2. Нарежьте картошку. 3. Добавьте свеклу, ..."]
    )


class RecipeListResponse(RecipeBase):
    """Формат ответа для первого экрана (GET /recipes)."""
    id: int = Field(..., title="ID рецепта", description="Идентификатор для перехода на детальный экран")
    views: int = Field(..., title="Количество просмотров", description="Счетчик популярности рецепта")

    class Config:
        from_attributes = True


class RecipeDetailResponse(RecipeBase):
    """Формат ответа для второго экрана (GET /recipes/{recipe_id})."""
    ingredients: str = Field(..., title="Список ингредиентов")
    description: str = Field(..., title="Текстовое описание")

    class Config:
        from_attributes = True #Pydantic v2
