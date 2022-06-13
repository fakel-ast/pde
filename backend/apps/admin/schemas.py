from typing import Dict, Optional

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    title: str
    slug: str
    active: bool


class CategoriesGet(BaseModel):
    categories: list[Category]
