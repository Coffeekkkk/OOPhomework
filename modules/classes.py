from modules.funtions import person_average


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