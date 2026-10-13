from typing import List

from database import AsyncSessionLocal
from fastapi import APIRouter, HTTPException, status
from models import RecipeModel
from schemas import RecipeCreate, RecipeDetailResponse, RecipeListResponse
from sqlalchemy import desc, select

router = APIRouter(prefix="/recipes", tags=["Рецепты"])


@router.get(
    "", response_model=List[RecipeListResponse], summary="Получить список всех рецептов"
)
async def get_recipes():
    async with AsyncSessionLocal() as db:
        stmt = select(RecipeModel).order_by(
            desc(RecipeModel.views), RecipeModel.cooking_time
        )
        result = await db.execute(stmt)
        return result.scalars().all()


@router.get(
    "/{recipe_id}",
    response_model=RecipeDetailResponse,
    summary="Получить детальную информацию",
)
async def get_recipe_detail(recipe_id: int):
    async with AsyncSessionLocal() as db:
        stmt = select(RecipeModel).filter(RecipeModel.id == recipe_id)
        result = await db.execute(stmt)
        recipe = result.scalar_one_or_none()

        if not recipe:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Рецепт не найден"
            )

        recipe.views += 1
        await db.commit()
        await db.refresh(recipe)
        return recipe


@router.post("", status_code=status.HTTP_201_CREATED, summary="Создать новый рецепт")
async def create_recipe(recipe_data: RecipeCreate):
    async with AsyncSessionLocal() as db:
        new_recipe = RecipeModel(
            title=recipe_data.title,
            cooking_time=recipe_data.cooking_time,
            ingredients=recipe_data.ingredients,
            description=recipe_data.description,
        )
        db.add(new_recipe)
        await db.commit()
        await db.refresh(new_recipe)
        return {"status": "success", "recipe_id": new_recipe.id}
