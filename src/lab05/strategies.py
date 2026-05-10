import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def sort_by_name(student):
    """Ключ сортировки по имени."""
    return student.name

def sort_by_gpa(student):
    """Ключ сортировки по среднему баллу (по убыванию)."""
    return -student.gpa

def sort_by_course_then_name(student):
    """Ключ сортировки: сначала курс, затем имя."""
    return (student.course, student.name)


# ==================== ФУНКЦИИ-ФИЛЬТРЫ ====================

def filter_honors(student):
    """Фильтр: отличники (GPA >= 4.8)."""
    return student.gpa >= 4.8

def filter_masters(student):
    """Фильтр: только магистры."""
    from lab04.models import MasterStudent
    return isinstance(student, MasterStudent)

def filter_by_course(course):
    """Фабрика функций: создаёт фильтр для заданного курса."""
    def filter_fn(student):
        return student.course == course
    return filter_fn


# ==================== ФУНКЦИИ ДЛЯ MAP ====================

def apply_discount(percent):
    """Фабрика: создаёт функцию для применения скидки к стипендии."""
    def discount_fn(student):
        new_stipend = student.stipend * (1 - percent / 100)
        return (student.name, new_stipend)
    return discount_fn

def increase_stipend(percent):
    """Фабрика: создаёт функцию для увеличения стипендии."""
    def increase_fn(student):
        student.stipend = student.stipend * (1 + percent / 100)
        return student
    return increase_fn


# ==================== CALLABLE-ОБЪЕКТЫ (СТРАТЕГИИ) ====================

class DiscountStrategy:
    """Стратегия применения скидки к стипендии (callable-объект)."""
    
    def __init__(self, percent: float):
        """
        Args:
            percent: Процент скидки (0-100)
        """
        self.percent = percent
    
    def __call__(self, student):
        """Применить скидку к студенту."""
        new_stipend = student.stipend * (1 - self.percent / 100)
        return (student.name, new_stipend, self.percent)


class HonorsBonusStrategy:
    """Стратегия начисления бонуса отличникам (callable-объект)."""
    
    def __init__(self, bonus: float, threshold: float = 4.8):
        """
        Args:
            bonus: Размер бонуса
            threshold: Пороговый GPA для получения бонуса
        """
        self.bonus = bonus
        self.threshold = threshold
    
    def __call__(self, student):
        """Начислить бонус, если студент отличник."""
        if student.gpa >= self.threshold:
            new_stipend = student.stipend + self.bonus
            return (student.name, student.stipend, new_stipend, self.bonus)
        return (student.name, student.stipend, student.stipend, 0)