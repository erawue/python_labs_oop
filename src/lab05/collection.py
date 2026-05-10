from typing import List, Callable, Any

class StudentGroup:
    def __init__(self):
        self._items = []
    
    def add(self, student): #Добавить студента в коллекцию.
        self._items.append(student)
    
    def get_all(self): #Вернуть копию списка всех студентов.
        return self._items.copy()
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __str__(self):
        if not self._items:
            return "Группа пуста"
        result = f"Группа студентов (всего: {len(self._items)}):\n"
        result += "-" * 50 + "\n"
        for i, student in enumerate(self._items, 1):
            result += f"{i}. {student.name} ({type(student).__name__}, курс {student.course}, GPA {student.gpa})\n"
        return result
    
    
    def sort_by(self, key_func: Callable, reverse: bool = False):
        """
        Сортировка коллекции по переданной функции-ключу.
        
        Args:
            key_func: Функция, возвращающая ключ для сортировки
            reverse: Сортировка в обратном порядке
        """
        self._items.sort(key=key_func, reverse=reverse)
        return self
    
    def filter_by(self, predicate: Callable):
        """
        Фильтрация коллекции по переданному условию.
        Возвращает новую коллекцию с отфильтрованными элементами.
        
        Args:
            predicate: Функция-условие, возвращающая True/False
        """
        new_group = StudentGroup()
        for item in self._items:
            if predicate(item):
                new_group.add(item)
        return new_group
    
    def apply(self, func: Callable):
        """
        Применить произвольную функцию ко всем элементам коллекции.
        
        Args:
            func: Функция, которая принимает студента и что-то с ним делает
        """
        result = []
        for item in self._items:
            result.append(func(item))
        return result
    
    def apply_map(self, func: Callable):
        """
        Преобразовать коллекцию с помощью map().
        
        Args:
            func: Функция преобразования
        """
        return list(map(func, self._items))
    
    def chain_operations(self, filter_func: Callable, sort_key_func: Callable, 
                         apply_func: Callable = None, sort_reverse: bool = False):
        """
        Цепочка операций: фильтрация → сортировка → применение.
        
        Args:
            filter_func: Функция для фильтрации
            sort_key_func: Функция-ключ для сортировки
            apply_func: Функция для применения к каждому элементу (опционально)
            sort_reverse: Сортировка в обратном порядке
        """
        # Фильтрация
        filtered = [item for item in self._items if filter_func(item)]
        
        # Сортировка
        filtered.sort(key=sort_key_func, reverse=sort_reverse)
        
        if apply_func:
            result = []
            for item in filtered:
                result.append(apply_func(item))
            return result
        return filtered