def person_average(person):
    count = 0
    count_len = 0
    for value in person.grades.values():
        count += sum(value)
        count_len += len(value)
    average = count / count_len
    return average


def average_lectors(lec_list, course):
    lec_course = []
    all_grades = 0
    grade_count = 0
    for lec in lec_list:
        if course in lec.courses_attached:
            lec_course.append(lec)
    for obj in lec_course:
        for grade in obj.grades.values():
            summa = sum(grade)
            all_grades += summa
            grade_count += len(grade)
    all_lector_average = all_grades / grade_count
    return all_lector_average


def average_students(stud_list, course):
    lec_course = []
    all_grades = 0
    grade_count = 0
    for stud in stud_list:
        if course in stud.courses_in_progress:
            lec_course.append(stud)
    for obj in lec_course:
        for grade in obj.grades.values():
            summa = sum(grade)
            all_grades += summa
            grade_count += len(grade)
    all_student_average = all_grades / grade_count
    return all_student_average