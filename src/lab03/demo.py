from base import Student
from models import BachelorStudent, MasterStudent
from collection import StudentGroup

def main():
    print("Сценарий 1 — Создание объектов разных типов")
    print("=" * 50)
    
    ordinary = Student("Алексей Смирнов", "24041111", 2, 4.0, 3000)
    bachelor = BachelorStudent("Екатерина Волкова", "21041234", 3, 4.5, 3500,
                                "Разработка веб-приложений", True)
    master = MasterStudent("Иван Жуков", "22049876", 1, 4.9, 4000,
                           "Искусственный интеллект", 1)
    
    print(ordinary)
    print()
    print(bachelor)
    print()
    print(master)
    print()
    
    print("Сценарий 2 — Работа коллекции с разными типами")
    print("=" * 50)
    
    group = StudentGroup()
    group.add(ordinary)
    group.add(bachelor)
    group.add(master)
    
    print("Все объекты в коллекции:")
    for s in group:
        print(f"- {s.name} ({type(s).__name__})")
    
    print("\nПроверка типов через isinstance():")
    for s in group:
        if isinstance(s, MasterStudent):
            print(f"{s.name} — магистр")
        elif isinstance(s, BachelorStudent):
            print(f"{s.name} — бакалавр")
        else:
            print(f"{s.name} — обычный студент")
    print()
    
    print("Сценарий 3 — Полиморфизм (расчёт стипендии)")
    print("=" * 50)
    
    for s in group:
        print(f"{s.name:30} → {s.calculate_scholarship():.0f} руб.")
    print()
    
    print("Сценарий 4 — Фильтрация по типу")
    print("=" * 50)
    
    bachelors = [s for s in group.get_all() if isinstance(s, BachelorStudent)]
    print(f"Бакалавров: {len(bachelors)}")
    for b in bachelors:
        print(f"  - {b.name}")
    
    masters = [s for s in group.get_all() if isinstance(s, MasterStudent)]
    print(f"\nМагистров: {len(masters)}")
    for m in masters:
        print(f"  - {m.name}")
    print()

    print("Сценарий 5 — Специфичные методы")
    print("=" * 70)
    
    print(bachelor.defend_thesis())
    print(master.publish_article())

if __name__ == "__main__":
    main()