class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_course(self, course_name):
        self.finished_courses.append(course_name)

    def grade_lecturers(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached\
                and course in self.courses_in_progress and 0 <= grade <= 10:
            if course in lector.grade_book:
                lector.grade_book[course] += [grade]
            else:
                lector.grade_book[course] = [grade]
        else:
            print('Error')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия:{self.surname}\n' \
              f'Средняя оценка: {overage_grade(self.grades)}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# maybe needs to be inserted into the class Lecturer
def overage_grade(journal):
    num = 0
    counter = 0
    for grades in journal.values():
        for grade in grades:
            counter += grade
            num += 1
    return round(counter/num, 2)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_book = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя ' \
              f'оценка за лекцию: {overage_grade(self.grade_book)}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('access denied')

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


best_student = Student('Dmitry', 'Fuchko', 'Male')
best_mentor = Mentor('Oleg', 'Bulygin')
best_reviewer = Reviewer('Max', 'Payne')
best_lector = Lecturer('Johny', 'Bamboni')
# print(best_student.__dict__)
best_student.finished_courses.append('Git')
best_student.add_finished_course('Flask')

best_student.courses_in_progress += ['Django']
best_student.courses_in_progress.append('Python-Web')
best_student.courses_in_progress.append('Python')

best_student.grades['Python'] = [10, 7, 8, 9]
best_student.grades['Python'] += [10]

# print(best_student.finished_courses)
print(best_student.courses_in_progress)
# print(best_student.grade)
best_reviewer.courses_attached.append('Python')
best_reviewer.courses_attached.append('Python-Web')
best_reviewer.courses_attached.append('Django')
best_lector.courses_attached.append('Python-Web')
best_lector.courses_attached.append('Python')


# print(best_mentor.__dict__)
best_reviewer.rate_hw(best_student, 'Python', 2)
best_reviewer.rate_hw(best_student, 'Django', 5)
best_reviewer.rate_hw(best_student, 'Django', 8)
best_reviewer.rate_hw(best_student, 'Django', 9)

best_student.grade_lecturers(best_lector, 'Python', 8)
best_student.grade_lecturers(best_lector, 'Python-Web', 7)
best_student.grade_lecturers(best_lector, 'Python', 6)
best_student.grade_lecturers(best_lector, 'Python', 5)
# print(best_student.grades)
# print(best_student.courses_in_progress)
# print(best_mentor.courses_attached)
print(best_lector.__dict__)
# print(best_lector.__dir__())
print(best_reviewer)
print(best_lector)
print(best_student)


