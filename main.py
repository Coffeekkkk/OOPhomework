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

    # def __str__(self):
    #     return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
    #            f"Средняя оценка за домашние задания :  {self.grades['average']}\n" \
    #            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
    #            f"Завершенные курсы: {', '.join(self.finished_courses)}"


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
stud_list = []

student1 = Student('Денис', 'Кравченко', 'мужской')
student1.courses_in_progress += ['Python', 'Git', 'SQL', 'Django']
stud_list.append(student1)

student2 = Student('Станислав', 'Дятловский', 'мужской')
student2.courses_in_progress += ['Python', 'Git', 'SQL', 'Django']
stud_list.append(student2)

lecture1 = Lecturer('Олег', 'Булыгин')
lecture1.courses_attached += ['Python', 'Git']
lecture_list.append(lecture1)

lecture2 = Lecturer('Федор', 'Пупкин')
lecture2.courses_attached += ['Python', 'Git']
lecture_list.append(lecture2)

reviewer1 = Reviewer('Сергей', 'Южаков')
reviewer1.courses_attached += ['Python', 'Git', 'SQL', 'Django']

reviewer2 = Reviewer('Денис', 'Волков')
reviewer2.courses_attached += ['Python', 'Git', 'SQL', 'Django']

student1.rate_lector(lecture1, 'Python', 10)
student2.rate_lector(lecture1, 'Python', 10)

student1.rate_lector(lecture2, 'Python', 10)
student2.rate_lector(lecture2, 'Python', 10)

reviewer1.rate_st(student1, 'Python', 2)
reviewer1.rate_st(student2, 'Python', 4)
reviewer2.rate_st(student1, 'Python', 5)
reviewer2.rate_st(student2, 'Python', 6)


def average_lector(lec_list, course):
    count_rate = 0
    count_volume = 0
    for obj in lec_list:
        if course in obj.grades.keys():
            count_rate += sum(obj.grades[course])
            count_volume += len(obj.grades[course])
    average = count_rate / count_volume
    return average


def average_student(student_list, course):
    count_rate = 0
    count_volume = 0
    for obj in student_list:
        if course in obj.grades.keys():
            count_rate += sum(obj.grades[course])
            count_volume += len(obj.grades[course])
    average = count_rate / count_volume
    return average


print(average_student(stud_list, 'Python'))


