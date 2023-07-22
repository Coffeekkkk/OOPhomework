def person_average(person):
    count = 0
    count_len = 0
    for value in person.grades.values():
        count += sum(value)
        count_len += len(value)
    average = count / count_len
    return average


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, teacher, course, grade):
        if isinstance(teacher, Lecturer) and course in teacher.courses_attached and course in self.courses_in_progress:
            if course in teacher.grades:
                teacher.grades[course] += [grade]
            else:
                teacher.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        return person_average(self) < person_average(other)

    def __eq__(self, other):
        return person_average(self) == person_average(other)

    def __le__(self, other):
        return person_average(self) <= person_average(other)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {person_average(self)}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {person_average(self)}'

    def __lt__(self, other):
        return person_average(self) < person_average(other)

    def __eq__(self, other):
        return person_average(self) == person_average(other)

    def __le__(self, other):
        return person_average(self) <= person_average(other)


class Reviewer(Mentor):
    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


lecture_list = []
student_list = []

student1 = Student('Денис', 'Кравченко', 'мужской')
student1.courses_in_progress += ['Python', 'Git', 'SQL', 'Django']
student1.finished_courses += ['Введение в программирование']
student_list.append(student1)

student2 = Student('Станислав', 'Дятловский', 'мужской')
student2.courses_in_progress += ['Python', 'Git', 'SQL', 'Django']
student2.finished_courses += ['Основы Java']
student_list.append(student2)

lecture1 = Lecturer('Олег', 'Булыгин')
lecture1.courses_attached += ['Python', 'Git']
lecture_list.append(lecture1)

lecture2 = Lecturer('Федор', 'Пупкин')
lecture2.courses_attached += ['Python', 'SQL']
lecture_list.append(lecture2)

reviewer1 = Reviewer('Сергей', 'Южаков')
reviewer1.courses_attached += ['Python', 'Git', 'SQL', 'Django']

reviewer2 = Reviewer('Денис', 'Волков')
reviewer2.courses_attached += ['Python', 'Git', 'SQL', 'Django']

student1.rate_lector(lecture1, 'Python', 10)
student2.rate_lector(lecture1, 'Python', 6)
student1.rate_lector(lecture2, 'Python', 6)
student2.rate_lector(lecture2, 'Python', 10)

reviewer1.rate_st(student1, 'Python', 1)
reviewer1.rate_st(student2, 'Python', 3)
reviewer2.rate_st(student1, 'Python', 1)
reviewer2.rate_st(student2, 'Python', 5)


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
    all_lector_average = all_grades / grade_count
    return print(all_lector_average)




