from model import Student
class StudentGroup:
    def __init__(self):
        self._items = []
    
    def add(self, student): #Добавить студента в коллекцию
        if not isinstance(student, Student):
            raise TypeError("Можно добавлять только объекты Student")
        if student in self._items:
            raise ValueError(f"Студент с ID {student.student_id} уже есть в группе")
        self._items.append(student)
    
    def remove(self, student): #Удалить студента из коллекции
        if student not in self._items:
            raise ValueError("Такого студента нет в группе")
        self._items.remove(student)
    
    def remove_at(self, index): #Удалить студента по индексу
        if not 0 <= index < len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)
    
    def get_all(self): #Вернуть список всех студентов
        return self._items.copy()
    
    #Поиск
    def find_by_id(self, student_id): #Найти студента по номеру зачетки
        for student in self._items:
            if student.student_id == student_id:
                return student
        return None
    
    def find_by_name(self, name): #Найти студента по имени
        for student in self._items:
            if student.name.lower() == name.lower():
                return student
        return None
    
    def find_by_course(self, course): #Найти всех студентов на заданном курсе
        return [s for s in self._items if s.course == course]
    
    #Магические методы
    def __len__(self): #Возвращает количество студентов в группе
        return len(self._items)
    
    def __iter__(self): #Позволяет итерироваться по коллекции
        return iter(self._items)
    
    def __getitem__(self, index): #Позволяет обращаться по индексу collection[i]
        if isinstance(index, slice):
            new_group = StudentGroup()
            for student in self._items[index]:
                new_group.add(student)
            return new_group
        return self._items[index]
    
    def __contains__(self, student):
        return student in self._items
    
    def __str__(self): #Строковое представление коллекции
        if not self._items:
            return "Группа пуста"
        result = f"Группа студентов (всего: {len(self._items)}):\n"
        result += "-" * 40 + "\n"
        for i, student in enumerate(self._items, 1):
            result += f"{i}. {student.name} (ID: {student.student_id}, курс: {student.course})\n"
        return result
    
    #Сортировка
    def sort_by_name(self, reverse=False): #Сортировка по имени
        self._items.sort(key=lambda s: s.name, reverse=reverse)
    
    def sort_by_course(self, reverse=False): #Сортировка по курсу
        self._items.sort(key=lambda s: s.course, reverse=reverse)
    
    def sort_by_gpa(self, reverse=False): #Сортировка по среднему баллу
        self._items.sort(key=lambda s: s.gpa, reverse=reverse)
    
    def sort(self, key, reverse=False): #Универсальная сортировка
        self._items.sort(key=key, reverse=reverse)
    
    #Фильтрация
    def get_active(self): #Получить коллекцию только из учащихся студентов
        new_group = StudentGroup()
        for student in self._items:
            if student.is_studying:
                new_group.add(student)
        return new_group
    
    def get_honors(self): #Получить коллекцию отличников
        new_group = StudentGroup()
        for student in self._items:
            if student.is_honors():
                new_group.add(student)
        return new_group
    
    def get_by_course(self, course): #Получить студентов заданного курса
        new_group = StudentGroup()
        for student in self._items:
            if student.course == course:
                new_group.add(student)
        return new_group