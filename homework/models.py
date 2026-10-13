from database import Base
from sqlalchemy import Column, Integer, String, Text


class RecipeModel(Base):
    """Рецепт в базе данных"""

    __tablename__ = "Recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    cooking_time = Column(Integer, nullable=False)
    ingredients = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    views = Column(Integer, default=0, nullable=False)
