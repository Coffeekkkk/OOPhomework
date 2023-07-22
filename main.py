from modules.classes import Student, Lecturer, Reviewer
from modules.funtions import average_students, average_lectors


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

reviewer1.rate_st(student1, 'Python', 10)
reviewer1.rate_st(student2, 'Python', 3)
reviewer2.rate_st(student1, 'Python', 1)
reviewer2.rate_st(student2, 'Python', 5)

print(student1)
print(student2)
print(lecture1)
print(lecture2)
print(reviewer1)
print(reviewer2)

print(f'Средняя оценка по всем студентам курса Python: {average_students(student_list, "Python")}')
print(f'Средняя оценка по всем лекторам курса Python: {average_lectors(lecture_list, "Python")}')
