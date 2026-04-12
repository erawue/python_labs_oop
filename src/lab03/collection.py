from base import Student

class StudentGroup:
    def __init__(self):
        self._items = []
    
    def add(self, student):
        if not isinstance(student, Student):
            raise TypeError("Можно добавлять только объекты Student")
        if student in self._items:
            raise ValueError(f"Студент с ID {student.student_id} уже есть в группе")
        self._items.append(student)
    
    def remove(self, student):
        if student not in self._items:
            raise ValueError("Такого студента нет в группе")
        self._items.remove(student)
    
    def remove_at(self, index):
        if not 0 <= index < len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)
    
    def get_all(self):
        return self._items.copy()
    
    def find_by_name(self, name_part):
        result = []
        for student in self._items:
            if name_part.lower() in student.name.lower():
                result.append(student)
        return result
    
    def find_by_id(self, student_id):
        for student in self._items:
            if student.student_id == student_id:
                return student
        return None
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            new_group = StudentGroup()
            for student in self._items[index]:
                new_group.add(student)
            return new_group
        return self._items[index]
    
    def __contains__(self, student):
        return student in self._items
    
    def __str__(self):
        if not self._items:
            return "Группа пуста"
        result = f"Группа студентов (всего: {len(self._items)}):\n"
        result += "-" * 40 + "\n"
        for i, student in enumerate(self._items, 1):
            result += f"{i}. {student.name} (ID: {student.student_id}, курс: {student.course})\n"
        return result
    
    def sort_by_name(self, reverse=False):
        self._items.sort(key=lambda s: s.name, reverse=reverse)
    
    def sort_by_gpa(self, reverse=False):
        self._items.sort(key=lambda s: s.gpa, reverse=reverse)
    
    def get_active(self):
        new_group = StudentGroup()
        for student in self._items:
            if student.is_studying:
                new_group.add(student)
        return new_group