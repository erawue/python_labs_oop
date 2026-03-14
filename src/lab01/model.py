class Student:
    total_students = 0
    MIN_GPA, MAX_GPA = 2.0, 5.0
    MIN_COURSE, MAX_COURSE = 1, 6

    def __init__(self, name, student_id, course, gpa, stipend=3000):
        self._validate_name(name)
        self._validate_id(student_id)
        self._validate_course(course)
        self._validate_gpa(gpa)
        self._validate_stipend(stipend)

        self._name = name.strip()
        self._student_id = student_id
        self._course = course
        self._gpa = float(gpa)
        self._stipend = float(stipend)
        self._is_studying = True
        
        Student.total_students += 1

    # Валидация
    def _validate_name(self, v):
        if not isinstance(v, str) or len(v.strip()) < 5 or ' ' not in v:
            raise ValueError("ФИО должно быть строкой из имени и фамилии")

    def _validate_id(self, v):
        if not (isinstance(v, str) and v.isdigit() and len(v) == 8):
            raise ValueError("ID должен быть строкой из 8 цифр")

    def _validate_course(self, v):
        if not isinstance(v, int) or not self.MIN_COURSE <= v <= self.MAX_COURSE:
            raise ValueError(f"Курс от {self.MIN_COURSE} до {self.MAX_COURSE}")

    def _validate_gpa(self, v):
        if not isinstance(v, (int, float)) or not self.MIN_GPA <= v <= self.MAX_GPA:
            raise ValueError(f"GPA от {self.MIN_GPA} до {self.MAX_GPA}")

    def _validate_stipend(self, v):
        if not isinstance(v, (int, float)) or v < 0:
            raise ValueError("Стипендия должна быть >= 0")

    # Свойства
    @property
    def name(self): return self._name
    @name.setter
    def name(self, v): self._validate_name(v); self._name = v.strip()

    @property
    def student_id(self): return self._student_id

    @property
    def course(self): return self._course
    @course.setter
    def course(self, v): self._validate_course(v); self._course = v

    @property
    def gpa(self): return self._gpa
    @gpa.setter
    def gpa(self, v): 
        self._validate_gpa(v)
        self._gpa = float(v)

    @property
    def stipend(self): return self._stipend
    @stipend.setter
    def stipend(self, v): self._validate_stipend(v); self._stipend = float(v)

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