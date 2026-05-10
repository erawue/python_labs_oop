import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.models import Student, BachelorStudent, MasterStudent
from lab05.collection import StudentGroup
from lab05.strategies import (
    sort_by_name, sort_by_gpa, sort_by_course_then_name,
    filter_honors, filter_masters, filter_by_course,
    apply_discount, increase_stipend,
    DiscountStrategy, HonorsBonusStrategy
)

def main():
    group = StudentGroup()
    students = [
        Student("Алексей Смирнов", "24041111", 2, 4.0, 3000),
        BachelorStudent("Арина Волкова", "21041234", 3, 4.5, 3500,
                        "Разработка веб-приложений", True),
        MasterStudent("Иван Жуков", "22049876", 1, 4.9, 4000,
                      "Искусственный интеллект", 1),
        BachelorStudent("Артем Воробьев", "23045567", 2, 4.7, 3500,
                        "Базы данных", False),
        MasterStudent("Соня Морозова", "25047890", 2, 4.8, 4000,
                      "Машинное обучение", 1),
        Student("Денис Новиков", "26043321", 1, 3.8, 3000)
    ]
    
    for s in students:
        group.add(s)
    
    print("Сценарий 1 — Сортировка разными стратегиями")
    print("=" * 80)
    
    print("\nСортировка по имени:")
    group.sort_by(sort_by_name)
    for i, s in enumerate(group, 1):
        print(f"{i}. {s.name} (GPA {s.gpa})")
    
    print("\nСортировка по GPA:")
    group.sort_by(sort_by_gpa)
    for i, s in enumerate(group, 1):
        print(f"{i}. {s.name} (GPA {s.gpa})")
    
    print("\nСортировка по курсу:")
    group.sort_by(sort_by_course_then_name)
    for i, s in enumerate(group, 1):
        print(f"{i}. {s.name} (курс {s.course})")

    print("")
    print("Сценарий 2 — Фильтрация разными фильтрами")
    print("=" * 80)
    
    honors_group = group.filter_by(filter_honors)
    print("\nФильтр 'отличники' (GPA >= 4.8):")
    for s in honors_group:
        print(f"- {s.name} (GPA {s.gpa})")
    
    masters_group = group.filter_by(filter_masters)
    print("\nФильтр 'магистры':")
    for s in masters_group:
        print(f"- {s.name} ({type(s).__name__})")
    
    # Фабрика функций
    second_course_filter = filter_by_course(2)
    course_2_group = group.filter_by(second_course_filter)
    print("\nФабрика функций: фильтр для 2 курса:")
    for s in course_2_group:
        print(f"- {s.name}")
    
    course_2_lambda = group.filter_by(lambda s: s.course == 2)
    print("\nТо же самое через lambda (без фабрики):")
    for s in course_2_lambda:
        print(f"- {s.name}")
    
    print("")   
    print("Сценарий 3 — Применение map() для преобразования данных")
    print("=" * 80)
    
    names = group.apply_map(lambda s: s.name)
    print("\nИмена всех студентов (через map + lambda):")
    for name in names:
        print(f"- {name}")
    
    increased = group.apply_map(lambda s: (s.name, s.stipend * 1.2))
    print("\nУвеличенная стипендия (+20%) через map + lambda:")
    for name, stip in increased:
        print(f"{name}: {stip:.1f} руб.")
    
    discount_10 = apply_discount(10)
    discounted = group.apply_map(discount_10)
    print("\nПрименение именованной функции (скидка 10% к стипендии):")
    for name, new_stip in discounted:
        print(f"{name}: {new_stip:.1f} руб.")

    print("")
    print("Сценарий 4 — Паттерн «Стратегия» и callable-объекты")
    print("=" * 80)
    
    discount_strategy = DiscountStrategy(20)
    print("\nСтратегия 'скидка 20%':")
    results = group.apply(discount_strategy)
    for i, (name, new_stip, percent) in enumerate(results, 1):
        old = students[i-1].stipend
        print(f"{i}. {name}: {old} → {new_stip:.1f} руб. (скидка {percent}%)")
    
    bonus_strategy = HonorsBonusStrategy(500)
    print("\nСтратегия 'бонус отличникам' (+500 руб., если GPA >= 4.8):")
    results = group.apply(bonus_strategy)
    for i, (name, old, new_stip, bonus) in enumerate(results, 1):
        stu = students[i-1]
        print(f"{i}. {name} (GPA {stu.gpa}): {old} → {new_stip:.1f} руб. (бонус {bonus} руб.)")
        
    print("")
    print("Сценарий 5 — Цепочка операций (filter → sort → apply)")
    print("=" * 80)
    
    def add_bonus_to_honors(student):
        if student.gpa >= 4.8:
            new_stipend = student.stipend + 500
            return (student.name, student.gpa, new_stipend)
        return (student.name, student.gpa, student.stipend)
    
    print("\nИсходные стипендии магистров:")
    for s in masters_group:
        print(f"- {s.name}: {s.stipend} руб. (GPA {s.gpa})")

    result = (group
        .filter_by(filter_masters)
        .sort_by(sort_by_gpa)
        .apply(add_bonus_to_honors))
    
    print("\nПосле цепочки (оставить магистров → отсортировать по GPA → применить бонус 500 руб.):")
    for name, gpa, stip in result:
        print(f"- {name} (GPA {gpa}): {stip} руб.")

if __name__ == "__main__":
    main()