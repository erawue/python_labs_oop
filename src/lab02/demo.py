from model import Student
from collection import StudentGroup

def main():
    group = StudentGroup()
    
    s1 = Student("Иван Петров", "21041234", 2, 4.5, 3500)
    s2 = Student("Анна Смирнова", "22049876", 3, 4.9, 4000)
    s3 = Student("Петр Иванов", "21045678", 1, 3.8, 2500)
    s4 = Student("Елена Волкова", "23041123", 2, 4.2, 3000)
    
    group.add(s1)
    group.add(s2)
    group.add(s3)
    group.add(s4)
    
    print("Сценарий 1 — создание коллекции:")
    print(group)
    print()

    print("Сценарий 2 — защита от дубликатов:")
    try:
        s5 = Student("Дубликат", "21041234", 1, 3.0, 2000)
        group.add(s5)
    except ValueError as e:
        print(f"Ошибка: {e}")
    print()

    print("Сценарий 3 — поиск студентов:")
    found = group.find_by_id("22049876")
    print(f"Поиск по ID '22049876': {found.name}")
    
    found = group.find_by_name("Иван Петров")
    print(f"Поиск по имени 'Иван Петров': {found.name}")
    
    course_students = group.find_by_course(2)
    print(f"Студенты 2 курса: {[s.name for s in course_students]}")
    print()

    print("Сценарий 4 — магические методы:")
    print(f"Количество студентов: {len(group)}")
    
    print("Перебор через for:")
    for student in group:
        print(f"  - {student.name} (курс {student.course})")
    
    print(f"Первый студент: {group[0].name}")
    print()

    print("Сценарий 5 — сортировка:")
    group.sort_by_name()
    print("По имени:")
    for s in group:
        print(f"  - {s.name}")
    
    group.sort_by_gpa(reverse=True)
    print("\nПо GPA (по убыванию):")
    for s in group:
        print(f"  - {s.name}: {s.gpa}")
    print()

    print("Сценарий 6 — фильтрация:")
    active_group = group.get_active()
    print(f"Учатся: {len(active_group)} студента")
    
    honors_group = group.get_honors()
    print(f"Отличники: {[s.name for s in honors_group]}")
    print()

    print("Сценарий 7 — удаление студентов:")
    group.remove(s3)
    print(f"После удаления Петра Иванова: {len(group)} студента")
    
    removed = group.remove_at(0)
    print(f"Удален по индексу 0: {removed.name}")
    print(f"Осталось: {len(group)} студентов")
    print()

    print("Сценарий 8 — обработка ошибок:")
    try:
        group.add("не студент")
    except TypeError as e:
        print(f"Ошибка: {e}")
    
    try:
        group.remove(s3)
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    try:
        group.remove_at(100)
    except IndexError as e:
        print(f"Ошибка: {e}")
    print()

    print("Сценарий 9 — итоговое состояние коллекции:")
    print(group)

if __name__ == "__main__":
    main()