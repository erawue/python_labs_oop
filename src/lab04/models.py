from interfaces import StudyManageable, AchievementsInterface
from validations import (
    validate_name, validate_student_id, validate_course, validate_gpa, validate_stipend
)

class Student(StudyManageable, AchievementsInterface):
    total_students = 0
    MIN_GPA, MAX_GPA = 2.0, 5.0
    MIN_COURSE, MAX_COURSE = 1, 6

    def __init__(self, name, student_id, course, gpa, stipend=3000):
        self._name = validate_name(name)
        self._student_id = validate_student_id(student_id)
        self._course = validate_course(course, self.MIN_COURSE, self.MAX_COURSE)
        self._gpa = validate_gpa(gpa, self.MIN_GPA, self.MAX_GPA)
        self._stipend = validate_stipend(stipend)
        self._is_studying = True
        Student.total_students += 1

    @property
    def name(self): return self._name
    @property
    def student_id(self): return self._student_id
    @property
    def course(self): return self._course
    @property
    def gpa(self): return self._gpa
    @property
    def stipend(self): return self._stipend
    @property
    def is_studying(self): return self._is_studying

    # Реализация StudyManageable
    def study(self, hours: int) -> str:
        return f"{self._name} занимался {hours} часа, подтянул знания"

    def take_exam(self) -> str:
        gpa_int = int(self._gpa)
        grade = "5" if gpa_int >= 5 else "4" if gpa_int >= 3 else "3"
        return f"{self._name} сдал экзамен на {grade}"

    # Реализация AchievementsInterface
    def get_achievements(self) -> list:
        return [f"Посещаемость {int(self._gpa * 20)}%"]

    def get_rating(self) -> str:
        if self._gpa >= 4.5:
            return "отлично"
        elif self._gpa >= 3.5:
            return "хорошо"
        else:
            return "удовлетворительно"

    def __str__(self):
        status = "Учится" if self._is_studying else "Отчислен"
        return (f"Студент: {self._name}\nНомер зачетки: {self._student_id}\n"
                f"Курс: {self._course}\nСредний балл: {self._gpa:.2f}\n"
                f"Стипендия: {self._stipend:.2f} руб.\nСтатус: {status}")


class BachelorStudent(Student):
    def __init__(self, name, student_id, course, gpa, stipend=3500, 
                 thesis_topic="", has_practice=False):
        super().__init__(name, student_id, course, gpa, stipend)
        self._thesis_topic = thesis_topic
        self._has_practice = has_practice

    # Переопределение StudyManageable
    def study(self, hours: int) -> str:
        return f"{self._name} готовится к защите, позанималась часа {hours}"

    def take_exam(self) -> str:
        return f"{self._name} сдала экзамен на отлично! + балл к диплому"

    # Переопределение AchievementsInterface
    def get_achievements(self) -> list:
        achievements = []
        if self._has_practice:
            achievements.append("Практика в компании «Яндекс»")
        achievements.append("Участие в конференции")
        return achievements

    def get_rating(self) -> str:
        return "отлично"

    def defend_thesis(self):
        return f"{self._name} защитила курсовую на тему '{self._thesis_topic}'"

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

    # Переопределение StudyManageable
    def study(self, hours: int) -> str:
        return f"{self._name} написал часть научной статьи за {hours} часов"

    def take_exam(self) -> str:
        return f"{self._name} сдал кандидатский минимум"

    # Переопределение AchievementsInterface
    def get_achievements(self) -> list:
        achievements = []
        if self._publications_count > 0:
            achievements.append(f"Публикация в журнале RSCI ({self._publications_count} статья)")
        achievements.append("Выступление на конференции")
        return achievements

    def get_rating(self) -> str:
        return "отлично" if self._publications_count >= 1 else "хорошо (нужны публикации)"

    def publish_article(self):
        self._publications_count += 1
        return f"{self._name} опубликовал статью (всего: {self._publications_count})"

    def __str__(self):
        base_str = super().__str__()
        return (base_str + f"\nТип: Магистр\nТема исследования: {self._research_topic}\n"
                f"Публикаций: {self._publications_count}")