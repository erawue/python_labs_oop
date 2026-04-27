from interfaces import StudyManageable, AchievementsInterface

class StudentGroup:
    def __init__(self):
        self._items = []
    
    def add(self, student):
        self._items.append(student)
    
    def get_all(self):
        return self._items.copy()
    
    def get_study_manageable(self): #Вернуть только объекты, реализующие StudyManageable
        return [item for item in self._items if isinstance(item, StudyManageable)]
    
    def get_achievements_interface(self): #Вернуть только объекты, реализующие AchievementsInterface
        return [item for item in self._items if isinstance(item, AchievementsInterface)]
    
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
        result += "-" * 40 + "\n"
        for i, student in enumerate(self._items, 1):
            result += f"{i}. {student.name} ({type(student).__name__})\n"
        return result