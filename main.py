
def average_grades(self):

    """Внешний метод для подсчета среднего балла (чтобы не повторять его много раз)"""

    total_gr = []
    try:
        for i in self.grades.values():
            total_gr += i
        avr_gr = round(sum(total_gr) / len(total_gr), 1)
    except ZeroDivisionError:
        avr_gr = "Ошибка"

    return avr_gr


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    median = average_grades

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {Student.median(self)}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            warn = f'{other.name} is not a student\n'
            return warn
        elif Student.median(self) < Student.median(other):
            warn = f'{self.name} более ленивый(ая), чем {other.name}\n'
            return warn
        else:
            warn = f'{self.name} НЕ более ленивый(ая), чем {other.name}\n'
            return warn


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    median = average_grades

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Lecturer.median(self)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            warn = f'{other.name} is not a lecturer\n'
            return warn
        elif Lecturer.median(self) < Lecturer.median(other):
            warn = f'{self.name} больший(ая) экстроверт, чем {other.name}\n'
            return warn
        else:
            warn = f'{self.name} НЕ больший(ая) экстроверт, чем {other.name}\n'
            return warn


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res

# Создаем списки для подсчета средних баллов по всем экземплярам классов


students = []
lecturers = []

# Создаем по 2 экземпляра каждого класса


student_1 = Student('Roy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Introduction']
student_1.finished_courses += ['Basics of Python']
students.append(student_1)

student_2 = Student('Marie', 'Curie', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Introduction']
student_2.finished_courses += ['Basics of Python']
students.append(student_2)

reviewer_1 = Reviewer('Jonn', 'Smith')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Jonn', 'Nash')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['OOP']


lecturer1 = Lecturer('Some', 'Body')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']
lecturers.append(lecturer1)

lecturer2 = Lecturer('Guido', 'van Rossum')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']
lecturers.append(lecturer2)

student_1.rate_lc(lecturer1, 'Python', 10)
student_1.rate_lc(lecturer1, 'Git', 9)

student_2.rate_lc(lecturer1, 'Python', 9.9)
student_2.rate_lc(lecturer1, 'Git', 9.5)

student_1.rate_lc(lecturer2, 'Python', 10)
student_1.rate_lc(lecturer2, 'Git', 10)

student_2.rate_lc(lecturer2, 'Python', 10)
student_2.rate_lc(lecturer2, 'Git', 10)

# cool_mentor = Mentor('Kip', 'Thorne')
# cool_mentor.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Git', 9.6)

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Git', 9.9)
reviewer_1.rate_hw(student_2, 'Git', 10)

reviewer_2.rate_hw(student_1, 'Python', 9.9)
reviewer_2.rate_hw(student_1, 'Python', 9.6)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 9.8)

reviewer_2.rate_hw(student_2, 'Python', 9.9)
reviewer_2.rate_hw(student_2, 'Python', 9.6)
reviewer_2.rate_hw(student_2, 'Git', 9.6)
reviewer_2.rate_hw(student_2, 'Git', 9.9)


# Функции подсчета средних оценок лекторов и студентов:


def total_gr_avr(persons):

    """ Одна функция для подсчета среднего балла, как для Lecturer, так и для Student (в зависимости от того,
    что передать на вход)"""

    try:
        avr = 0
        class_ = persons[0].__class__
        for i in persons:
            avr += i.median()
        ans = f'Средняя оценка {(str(class_.__name__)).lower()+"s"} = {round(avr/len(persons), 1)}'
    except TypeError:
        ans = 'Ошибка'
    return ans

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)


print(student_1)
print(student_2)

print(student_1 > student_2)
print(student_1 < student_2)

print(lecturer1)
print(lecturer2)

print(lecturer1 > lecturer2)
print(lecturer1 < lecturer2)

print(reviewer_1)
print(reviewer_2)

print(total_gr_avr(students))
print(total_gr_avr(lecturers))
