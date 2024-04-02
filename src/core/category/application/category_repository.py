from abc import ABC, abstractmethod
from uuid import UUID

from src.core.category.domain.category import Category #ABSTRACT base class


#interface para CategoryRepository
class CategoryRepository(ABC):
    @abstractmethod
    def save(self, category: Category):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id: UUID) -> Category | None :
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id: UUID) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, category: Category) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def list(self) -> list[Category]:
        raise NotImplementedError