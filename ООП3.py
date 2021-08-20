class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        sum_hw = 0
        count = 0
        for course in self.grades.values():
            sum_hw += sum(course)
            count += len(course)
        return round(sum_hw / count, 2)

    def __str__(self):
        res = f'Имя: {self.name} \n '               f'Фамилия: {self.surname} \n'               f'Средняя оценка за домашние задания: {self.get_avg_grade()} \n'              f'Курсы в процессе обучения: {" ".join(self.courses_in_progress)} \n'              f'Завершенные курсы: {" ".join(self.finished_courses)}'
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет!')
            return
        else:
            compare = self.get_avg_grade() < other_student.get_avg_grade()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{self.name} {self.surname} учится лучше, чем {other_student.name} {other_student.surname}')
            return compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n '               f'Фамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_grade(self):
        sum_lect = 0
        count = 0
        for course in self.grades.values():
            sum_lect += sum(course)
            count += len(course)
        return round(sum_lect / count, 2)

    def __str__(self):
        res = f'Имя: {self.name} \n '               f'Фамилия: {self.surname}'               f'Средняя оценка за лекции: {self.get_avg_grade()}'
        return res

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет!')
            return
        else:
            compare = self.get_avg_grade() < other_lecturer.get_avg_grade()
            if compare:
                print(f'{self.name} {self.surname} ведет хуже, чем {other_lecturer.name} {other_lecturer.surname}')
            else:
                print(f'{self.name} {self.surname} ведет лучше, чем {other_lecturer.name} {other_lecturer.surname}')
            return compare





best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

next_student = Student('Some', 'Name', 'm')
next_student.courses_in_progress += ['Python']
next_student.courses_in_progress += ['Git']

cool_reviwer = Reviewer('Some', 'Name')
cool_reviwer.courses_attached += ['Python']
cool_reviwer.courses_attached += ['Git']
cool_reviwer.rate_hw(best_student, 'Python', 6)
cool_reviwer.rate_hw(best_student, 'Python', 9)
cool_reviwer.rate_hw(best_student, 'Python', 8)
cool_reviwer.rate_hw(best_student, 'Git', 10)
cool_reviwer.rate_hw(best_student, 'Git', 20)

cool_reviwer.rate_hw(next_student, 'Python', 10)
cool_reviwer.rate_hw(next_student, 'Python', 8)
cool_reviwer.rate_hw(next_student, 'Python', 3)
cool_reviwer.rate_hw(next_student, 'Git', 5)
cool_reviwer.rate_hw(next_student, 'Git', 2)

cool_lecturer = Lecturer('Some', 'Name')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

next_lecturer = Lecturer('Some', 'Name')
next_lecturer.courses_attached += ['Python']
next_lecturer.courses_attached += ['Git']

best_student.rate_lecturer(cool_lecturer, 'Python', 4)
best_student.rate_lecturer(cool_lecturer, 'Git', 10)

next_student.rate_lecturer(next_lecturer, 'Python', 10)
next_student.rate_lecturer(next_lecturer, 'Git', 10)

print(best_student.grades)
print(next_student.grades)

print(best_student)
print(next_student)

print(best_student < next_student)

print(cool_lecturer < next_lecturer)

print(cool_lecturer)
print(cool_reviwer)




def get_avg_hw_grade(student_list, course):
    total_sum = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)


print(get_avg_hw_grade([best_student, next_student], 'Python'))





def get_avg_hw_grade(student_list, course):
    #     total_sum = 0
    all_grades = []
    for student in student_list:
        if course in student.courses_in_progress and student.grades.get(course) is not None:
            all_grades += student.grades.get(course)

    if sum(all_grades) != 0:
        print(round(sum(all_grades) / len(all_grades), 1))
    else:
        print('Оценки отсутствуют!')


get_avg_hw_grade([best_student, next_student], 'Python')
