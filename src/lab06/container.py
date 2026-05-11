from typing import TypeVar, Generic, Callable, Optional, Iterator, List, Protocol

# ========== Protocol ==========

class Displayable(Protocol):
    def display(self) -> str:
        ...

class Scorable(Protocol):
    def score(self) -> float:
        ...

# ========== TypeVar ==========

T = TypeVar('T')
R = TypeVar('R')
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

# ========== TypedCollection ==========

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError("Элемент не найден")
        self._items.remove(item)
    
    def remove_at(self, index: int) -> T:
        if not 0 <= index < len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)
    
    def get_all(self) -> List[T]:
        return self._items.copy()
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self) -> Iterator[T]:
        return iter(self._items)
    
    def __getitem__(self, index: int) -> T:
        return self._items[index]
    
    def __str__(self) -> str:
        if not self._items:
            return "Коллекция пуста"
        result = f"Коллекция ({len(self._items)} элементов):\n"
        for i, item in enumerate(self._items, 1):
            result += f"  {i}. {item}\n"
        return result