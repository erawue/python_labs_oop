from base import Student
class BachelorStudent(Student):
    def __init__(self, name, student_id, course, gpa, stipend=3000, 
                 thesis_topic="", has_practice=False):
        super().__init__(name, student_id, course, gpa, stipend)
        self._thesis_topic = thesis_topic
        self._has_practice = has_practice
    
    @property
    def thesis_topic(self): return self._thesis_topic
    
    @property
    def has_practice(self): return self._has_practice
    
    def defend_thesis(self):
        return f"{self._name} защитила курсовую на тему '{self._thesis_topic}'"
    
    def calculate_scholarship(self): # Базовая стипендия + 500 руб. если есть практика
        base = super().calculate_scholarship()
        if self._has_practice:
            return base + 500
        return base
    
    def __str__(self):
        base_str = super().__str__()
        practice = "есть" if self._has_practice else "нет"
        return (base_str + f"\nТип: Бакалавр\nТема курсовой: {self._thesis_topic}\n"
                f"Практика: {practice}")

class MasterStudent(Student):
    def __init__(self, name, student_id, course, gpa, stipend=4000,
                 research_topic="", publications_count=0):
        super().__init__(name, student_id, course, gpa, stipend)
        self._research_topic = research_topic
        self._publications_count = publications_count
    
    @property
    def research_topic(self): return self._research_topic
    
    @property
    def publications_count(self): return self._publications_count
    
    def publish_article(self):
        self._publications_count += 1
        return f"{self._name} опубликовал статью в '{self._research_topic}' (всего: {self._publications_count})"
    
    def calculate_scholarship(self): # Базовая стипендия + 300 руб. за каждую публикацию
        base = super().calculate_scholarship()
        bonus = min(self._publications_count * 300, 1500)
        return base + bonus
    
    def __str__(self):
        base_str = super().__str__()
        return (base_str + f"\nТип: Магистр\nТема исследования: {self._research_topic}\n"
                f"Публикаций: {self._publications_count}")