class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_course(self, course):
        if course in self.finished_courses:
            print(f'Course "{course}" have been added earlier.')
        else:
            self.finished_courses.append(course)

    def grade_lecturers(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached\
                and course in self.courses_in_progress and 0 <= grade <= 10:
            if course in lector.grade_book:
                lector.grade_book[course] += [grade]
            else:
                lector.grade_book[course] = [grade]
        else:
            print('Access denied')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия:{self.surname}\n' \
              f'Средняя оценка: {average_grade(self.grades)}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __gt__(self, classmate):
        if isinstance(classmate, Student):
            return average_grade(self.grades) > average_grade(classmate.grades)
        else:
            return f"{classmate.name} {classmate.surname} isn't found among students"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


def average_grade(journal):
    total = 0
    counter = 0
    for grades in journal.values():
        for grade in grades:
            total += grade
            counter += 1
    return round(total/counter, 2)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_book = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя ' \
              f'оценка за лекцию: {average_grade(self.grade_book)}'
        return res

    def __gt__(self, colleague):
        if isinstance(colleague, Lecturer):
            return average_grade(self.grade_book) > average_grade(colleague.grade_book)
        else:
            return f"{colleague.name} {colleague.surname} isn't found among lecturers"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Access denied'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


def avg_grade_students_in_course(students, course):
    total = 0
    counter = 0
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            for grade in student.grades[course]:
                total += grade
                counter += 1
        else:
            return 'Check the passed arguments'
    return f'The average grade for students in the "{course}" ' \
           f'course is {round(total / counter, 2)}'


def avg_rating_course_lecturers(lecturers, course):
    total = 0
    counter = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grade_book:
            for grade in lecturer.grade_book[course]:
                total += grade
                counter += 1
        else:
            return 'Check the passed arguments'
    return f'The average grade of the lecturers of the "{course}" ' \
           f'course is {round(total / counter, 2)}'


student_1 = Student('Dmitry', 'Fuchko', 'Male')
student_2 = Student('Denis', 'Okan', 'Male')

student_1.courses_in_progress += ['Django']
student_2.courses_in_progress += ['Django']
student_1.courses_in_progress.append('Python-Web')
student_2.courses_in_progress.append('Python-Web')
student_1.courses_in_progress.append('Python')
student_2.courses_in_progress.append('Python')

student_1.finished_courses.append('Git')
student_2.add_finished_course('Git')
student_1.add_finished_course('Git')

lector_1 = Lecturer('Johny', 'Bamboni')
lector_2 = Lecturer('Magic', 'Johnson')
mentor_1 = Mentor('Oleg', 'Bulygin')
reviewer_1 = Reviewer('Oleg', 'Bulygin')
lector_1.courses_attached.append('Python-Web')
lector_2.courses_attached.append('Python-Web')
lector_1.courses_attached.append('Python')
lector_2.courses_attached.append('Python')
reviewer_1.courses_attached.append('Python')
reviewer_1.courses_attached.append('Python-Web')
reviewer_1.courses_attached.append('Django')
reviewer_1.rate_hw(student_2, 'Python', 2)
reviewer_1.rate_hw(student_2, 'Django', 9)
reviewer_1.rate_hw(student_1, 'Django', 5)
reviewer_1.rate_hw(student_1, 'Django', 8)

student_2.grade_lecturers(lector_2, 'Python', 7)
student_2.grade_lecturers(lector_1, 'Python-Web', 8)
student_2.grade_lecturers(lector_1, 'Python-Web', 7)
student_1.grade_lecturers(lector_2, 'Python-Web', 7)
student_1.grade_lecturers(lector_2, 'Python', 6)
student_2.grade_lecturers(lector_1, 'Python', 6)

student_2.grade_lecturers(lector_1, 'Python', 11)
student_1.grade_lecturers(lector_2, 'Django', 5)
student_1.grade_lecturers(mentor_1, 'Python', 5)
print(lector_1.grade_book)
print(lector_2.grade_book)




# print(best_student.__dict__)





student_1.grades['Python'] = [9, 9, 9, 9, 5, 6, 4]
student_2.grades['Python'] = [8, 7, 8, 9, 5, 7, 3]

reviewer_1.courses_attached.append('Python')
reviewer_1.courses_attached.append('Python-Web')
reviewer_1.courses_attached.append('Django')

print(avg_grade_students_in_course([student_2, student_1], 'Django'))
print(avg_rating_course_lecturers([lector_1, lector_2], 'Python-Web'))
print(reviewer_1)
print(lector_1)
print(student_1)
print(student_2)
print(student_1 > student_2)
print(lector_1)
print(lector_2)
print(lector_1 > lector_2)

