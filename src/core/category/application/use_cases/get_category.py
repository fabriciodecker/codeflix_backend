

from dataclasses import dataclass
from uuid import UUID

import pytest

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.exceptions import CategoryNotFound
from src.core.category.domain.category import Category


@dataclass
class GetCategoryRequest:
    id: UUID
    
@dataclass
class GetCategoryResponse:
    id: UUID
    name: str
    description: str = ""
    is_active: bool = True



class GetCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self, request: GetCategoryRequest) -> GetCategoryResponse: 
        category = self.repository.get_by_id(id=request.id)
        if category is None:
            raise CategoryNotFound(f"Category with {request.id} not found")
        
        return GetCategoryResponse(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active,
        )
        
        # try:
        #     category = Category(
        #         name=request.name,
        #         description=request.description,
        #         is_active=request.is_active
        #     )
        # except ValueError as err:
        #     raise InvalidCategoryData(err)
        # self.repository.save(category)
        # return CreateCategoryResponse(id=category.id)

