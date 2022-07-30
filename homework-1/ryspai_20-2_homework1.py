class Person:

    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, ):
        print(f'Полное имя:{self.full_name}, Возраст:{self.age}, Семейное положение:{self.is_married}')


me =Person('Arstanbekova Alia', 22, 'Single')
print(f'{me.full_name},{me.age},{me.is_married}')
me.introduce_myself()


class Student(Person):

    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average(self):
        count = 0
        sum = 0
        for i in self.marks.values():
            count += 1
            sum += i
        print(round(sum / count, 1))


class Teacher(Person):
    salary = 1500

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def cash(self):
        if self.experience > 3:
            new_salary = self.salary + (self.salary / 100 * 5)
            print(new_salary)
        else:
            print(self.salary)


Jasmin = Teacher('Jasmin Faridinova', 50, 'married', 10)
Jasmin.introduce_myself()
Jasmin.cash()
student = []


def create_students():
    student1 = Student('Alymkulov Ryspai', 14, 'Unmarried', marks= {
        'Химия': 5,
        'Алгебра': 4,
        'физика': 5
    })
    student.append(student1)
    student2 = Student('Asanaliev Aman', 17, 'married', marks={
       'Химия': 3,
       'Алгебра': 3,
       'физика': 3
    })
    student.append(student2)
    student3 = Student('Alimbek uulu Tagdyrbek', 15, 'Married', marks={
        'Химия': 2,
        'Алгебра': 4,
        'физика': 5
    })
    student.append(student3)


create_students()
for i in student:
    i.introduce_myself()
    i.average()