import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from container import TypedCollection, Displayable, Scorable, D, S
from lab04.models import Student, BachelorStudent, MasterStudent

def main():
    print("Сценарий 1: Базовые операции TypedCollection")
    print("=" * 60)
    
    collection: TypedCollection[Student] = TypedCollection()
    
    s1 = Student("Алексей Смирнов", "24041111", 2, 4.0, 3000)
    s2 = BachelorStudent("Арина Волкова", "21041234", 3, 4.5, 3500,
                          "Разработка веб-приложений", True)
    s3 = MasterStudent("Иван Жуков", "22049876", 1, 4.9, 4000,
                       "Искусственный интеллект", 1)
    
    collection.add(s1)
    collection.add(s2)
    collection.add(s3)
    
    print(f"\nДобавлено: {s1.name} {type(s1).__name__} | {s1.course} курс | {s1.gpa} | {s1.stipend} руб.")
    print(f"Добавлено: {s2.name} {type(s2).__name__} | {s2.course} курс | {s2.gpa} | {s2.stipend} руб.")
    print(f"Добавлено: {s3.name} {type(s3).__name__} | {s3.course} курс | {s3.gpa} | {s3.stipend} руб.")
    print(f"\nВсего элементов: {len(collection)}")
    
    print("\nСодержимое коллекции:")
    for item in collection:
        print(f"  - {item.name} ({type(item).__name__})")
    
    print("\nПроверка типов (добавление объекта неправильного типа):")
    try:
        test_collection: TypedCollection[Student] = TypedCollection()
        test_collection.add("не студент")  # type: ignore
    except TypeError as e:
        print(f"Ошибка: {e}")
    print()
    
    print("Сценарий 2: find, filter, map")
    print("=" * 60)
    
    print("\n1. find() — поиск по условию:")
    found = collection.find(lambda s: s.gpa >= 4.5)
    print(f"   Студент с GPA >= 4.5: {found.name if found else 'None'} (GPA {found.gpa if found else '-'})")
    
    found = collection.find(lambda s: s.student_id == "99999999")
    print(f"   Студент с ID '99999999' (не найден): {found}")
    
    print("\n2. filter() — фильтрация по условию:")
    filtered = collection.filter(lambda s: s.course >= 2)
    print(f"   Студенты с курсом >= 2 ({len(filtered)} шт.):")
    for s in filtered:
        print(f"   - {s.name} (курс {s.course})")
    
    print("\n3. map() — преобразование (демонстрация смены типа):")
    names = collection.map(lambda s: s.name)
    print(f"   Имена студентов (list[str]): {names}")
    
    gpas = collection.map(lambda s: s.gpa)
    print(f"   Средние баллы GPA (list[float]): {gpas}")
    
    displays = collection.map(lambda s: s.display())
    print(f"   Display (list[str]):")
    for d in displays:
        print(f"     - {d}")
    print()
    
    print("Сценарий 3: Protocols (структурная типизация)")
    print("=" * 60)
    
    # DisplayableCollection
    display_collection: TypedCollection[D] = TypedCollection()
    display_collection.add(s1)
    display_collection.add(s2)
    display_collection.add(s3)

    print("\nВызов display() для всех объектов:")
    for s in display_collection:
        print(f" {s.display()}")

    # ScorableCollection
    print("\n2. ScorableCollection — коллекция объектов с методом score():")
    score_collection: TypedCollection[S] = TypedCollection()
    score_collection.add(s1)
    score_collection.add(s2)
    score_collection.add(s3)

    print("\nСортировка по score (по убыванию):")
    sorted_by_score = sorted(score_collection.get_all(), key=lambda x: x.score(), reverse=True)
    for i, s in enumerate(sorted_by_score, 1):
        print(f" {i}. {s.name} (score: {s.score():.1f})")

if __name__ == "__main__":
    main()