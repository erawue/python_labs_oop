from model import Student

def main():
    s1 = Student("Иван Петров", "21041234", 2, 4.5, 3500)
    print("Сценарий 1 — создание объекта:")
    print(s1)
    print()

    s2 = Student("Петр Иванов", "21045678", 2, 4.3, 3000)
    s3 = Student("Иван Петров", "21041234", 2, 4.5, 3500)
    print("Сценарий 2 — сравнение объектов:")
    print(f"s1 == s2? {s1 == s2}")
    print(f"s1 == s3? {s1 == s3}")
    print()

    s1.gpa = 4.8
    print("Сценарий 3 — изменение через setter:")
    print(f"GPA = {s1.gpa:.2f}")
    print(f"Статус стипендии: {'Получает' if s1.has_scholarship else 'Не получает'}")
    print()

    print("Сценарий 4 — проверка бизнес-метода:")
    print("Студент является отличником?", s1.is_honors())
    print("Может получать повышенную стипендию?", s1.can_get_increased_scholarship())
    print()

    print("Сценарий 5 — повышение стипендии:")
    s1.increase_stipend(10)
    print(f"Стипендия после повышения +10%: {s1.stipend:.2f} руб.")
    print()

    print("Сценарий 6 — отчисление студента:")
    s1.expel()
    print(s1)
    print()

    try:
        s1.promote()
    except ValueError as e:
        print(f"Ошибка при попытке перевести на следующий курс: {e}")
    print()

    print("Зачисления студента обратно:")
    s1.reinstate()
    print(s1)
    print()

    try:
        s1.reinstate()
    except ValueError as e:
        print(f"Ошибка при повторном зачислении: {e}")
    print() 

    print("Сценарий 7 — демонстрация валидации:")
    try:
        bad = Student("", "abc", 7, 6.0, -100)
    except ValueError as e:
        print(f"Ошибка создания: {e}")
    
    try:
        s1.gpa = 5.5
    except ValueError as e:
        print(f"Ошибка при попытке установить некорректный балл: {e}")
    print()

    try:
        s1.course = 7
    except ValueError as e:
        print("Ошибка при попытке установить некорректный курс:", e)
    print()

    print("Сценарий 8 — атрибут класса:")
    print(f"Всего студентов: {Student.total_students}")
    print(f"Доступ через экземпляр: {s1.total_students}")
    print()

    print("Сценарий 9 — __repr__:")
    print(repr(s1))
    print()

    print("Сценарий 10 — Перевод на курс:")
    s4 = Student("Анна Смирнова", "22049876", 5, 4.9, 4000)
    print(f"Был курс: {s4.course}")
    s4.promote()
    print(f"Стал курс: {s4.course}")

if __name__ == "__main__":
    main()