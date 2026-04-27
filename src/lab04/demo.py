from models import Student, BachelorStudent, MasterStudent
from collection import StudentGroup
from interfaces import StudyManageable, AchievementsInterface

def study_all(items):
    """Универсальная функция для обучения всех студентов"""
    for item in items:
        if isinstance(item, StudyManageable):
            print(f"  {item.study(3)}")
            print(f"  {item.take_exam()}")
            print()

def display_achievements_all(items):
    """Универсальная функция для показа достижений"""
    for item in items:
        if isinstance(item, AchievementsInterface):
            print(f"{item.name}")
            print(f"  Рейтинг: {item.get_rating()}")
            print(f"  Достижения: {', '.join(item.get_achievements())}")
            print()

def main():
    print("Сценарий 1 — Создание объектов и проверка интерфейсов")
    print("=" * 65)
    
    ordinary = Student("Алексей Смирнов", "24041111", 2, 4.0, 3000)
    bachelor = BachelorStudent("Екатерина Волкова", "21041234", 3, 4.5, 3500,
                                "Разработка веб-приложений", True)
    master = MasterStudent("Иван Жуков", "22049876", 1, 4.9, 4000,
                           "Искусственный интеллект", 1)
    
    students = [ordinary, bachelor, master]

    print("Сценарий 1 — Создание объектов и проверка интерфейсов")
    print("Объекты созданы:")
    for s in students:
        print(f"- {s.name}  ({type(s).__name__}), курс: {s.course}, GPA: {s.gpa}")
    
    print("\nПроверка реализации интерфейсов:")
    for s in students:
        is_study = "Да" if isinstance(s, StudyManageable) else "Нет"
        is_achievements = "Да" if isinstance(s, AchievementsInterface) else "Нет"
        print(f"{s.name}: StudyManageable? {is_study}, AchievementsInterface? {is_achievements}")
    print()
    
    print("Сценарий 2 — Полиморфизм (процесс обучения)")
    print("=" * 65)
    print("ОБУЧЕНИЕ:")
    study_all(students)
    
    print("Сценарий 3 — Достижения и рейтинг")
    print("=" * 78)
    print("ДОСТИЖЕНИЯ СТУДЕНТОВ:\n")
    display_achievements_all(students)
    
    print("Сценарий 4 — Фильтрация коллекции по интерфейсу")
    print("=" * 65)
    
    group = StudentGroup()
    for s in students:
        group.add(s)
    
    print(f"Все объекты в коллекции ({len(group)}):")
    for s in group:
        print(f"- {s.name} ({type(s).__name__})")
    
    study_items = group.get_study_manageable()
    print(f"\nОбъекты, реализующие StudyManageable ({len(study_items)}):")
    for s in study_items:
        print(f"- {s.name}")
    
    achievements_items = group.get_achievements_interface()
    print(f"\nОбъекты, реализующие AchievementsInterface ({len(achievements_items)}):")
    for s in achievements_items:
        print(f"- {s.name}")

if __name__ == "__main__":
    main()