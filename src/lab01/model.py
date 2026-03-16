from validate import (
    validate_name, 
    validate_student_id, 
    validate_course, 
    validate_gpa, 
    validate_stipend
)

class Student:
    total_students = 0
    MIN_GPA, MAX_GPA = 2.0, 5.0
    MIN_COURSE, MAX_COURSE = 1, 6

    def __init__(self, name, student_id, course, gpa, stipend=3000):
        # Валидация через импортированные функции
        self._name = validate_name(name)
        self._student_id = validate_student_id(student_id)
        self._course = validate_course(course, self.MIN_COURSE, self.MAX_COURSE)
        self._gpa = validate_gpa(gpa, self.MIN_GPA, self.MAX_GPA)
        self._stipend = validate_stipend(stipend)
        self._is_studying = True
        
        Student.total_students += 1

    # Свойства
    @property
    def name(self): return self._name
    @name.setter
    def name(self, v): self._name = validate_name(v)

    @property
    def student_id(self): return self._student_id

    @property
    def course(self): return self._course
    @course.setter
    def course(self, v): self._course = validate_course(v, self.MIN_COURSE, self.MAX_COURSE)

    @property
    def gpa(self): return self._gpa
    @gpa.setter
    def gpa(self, v): self._gpa = validate_gpa(v, self.MIN_GPA, self.MAX_GPA)

    @property
    def stipend(self): return self._stipend
    @stipend.setter
    def stipend(self, v): self._stipend = validate_stipend(v)

    @property
    def is_studying(self): return self._is_studying
    
    @property
    def has_scholarship(self):
        return self._gpa >= 4.5 and self._is_studying

    # Методы состояния
    def expel(self):
        if not self._is_studying: raise ValueError("Студент уже отчислен")
        self._is_studying = False

    def reinstate(self):
        if self._is_studying: raise ValueError("Студент ещё учится")
        self._is_studying = True

    # Бизнес-методы
    def promote(self):
        if not self._is_studying: raise ValueError("студент уже отчислен")
        if self._course >= self.MAX_COURSE: raise ValueError("Cтудент уже на последнем курсе")
        self._course += 1

    def is_honors(self):
        return self._gpa >= 4.8

    def increase_stipend(self, percent):
        if not self._is_studying: raise ValueError("Стипендия отчисленному студенту не изменяется")
        if not 0 <= percent <= 50: raise ValueError("Процент должен быть от 0 до 50")
        self._stipend *= (1 + percent / 100)
    
    def can_get_increased_scholarship(self):
        return self._is_studying and self._gpa >= 4.8 and self._course >= 3

    # Магические методы
    def __str__(self):
        status = "Учится" if self._is_studying else "Отчислен"
        scholarship = "Получает" if self._gpa >= 4.5 else "Не получает"
        return (
            f"Студент: {self._name}\n"
            f"Номер зачетки: {self._student_id}\n"
            f"Курс: {self._course}\n"
            f"Средний балл: {self._gpa:.2f}\n"
            f"Стипендия: {self._stipend:.2f} руб.\n"
            f"Статус: {status}\n"
            f"Стипендия: {scholarship}"
        )

    def __repr__(self):
        return (
            f"Student(name='{self._name}', student_id='{self._student_id}', "
            f"course={self._course}, gpa={self._gpa:.2f}, stipend={self._stipend:.2f}, "
            f"is_studying={self._is_studying})"
        )
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self._student_id == other._student_id