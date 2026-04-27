def validate_name(v):
    if not isinstance(v, str) or len(v.strip()) < 5 or ' ' not in v:
        raise ValueError("ФИО должно быть строкой из имени и фамилии")
    return v.strip()

def validate_student_id(v):
    if not (isinstance(v, str) and v.isdigit() and len(v) == 8):
        raise ValueError("Номер студенческого должен быть строкой из 8 цифр")
    return v

def validate_course(v, min_course, max_course):
    if not isinstance(v, int) or not min_course <= v <= max_course:
        raise ValueError(f"Курс должен быть от {min_course} до {max_course}")
    return v

def validate_gpa(v, min_gpa, max_gpa):
    if not isinstance(v, (int, float)) or not min_gpa <= v <= max_gpa:
        raise ValueError(f"Средний балл должен быть от {min_gpa} до {max_gpa}")
    return float(v)

def validate_stipend(v):
    if not isinstance(v, (int, float)) or v < 0:
        raise ValueError("Стипендия должна быть >= 0")
    return float(v)