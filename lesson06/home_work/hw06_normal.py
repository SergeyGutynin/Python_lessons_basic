# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:

    def __init__(self, name, classes=None, teachers=None):
        self.name = name

        self._classes = classes
        self._teachers = teachers

    def get_classes(self):
        return self._classes.copy()

    def get_class_students(self, class_name):
        for el in self._classes:
            if el.name == class_name:
                return el.students

    def print_class_students(self, class_name):
        result = self.get_class_students(class_name)
        print(f'Class name {class_name}')
        for ind, st in enumerate(result):
            print(f'{ind+1}. {st.name}')

    def get_student_subjects(self, student_name):
        for cl in self._classes:
            for st in cl.students:
                if st.name == student_name:
                    tc_names = [t.name for t in self._teachers if t.subjects in cl.subjects]
                    return student_name, cl.name, tc_names, cl.subjects

    def print_student_subjects(self, student_name):
        result = self.get_student_subjects(student_name)
        print(f'Student {result[0]} in class {result[1]} has teachers {result[2]} in subjects {result[3]}')

    def get_student_parents(self, student_name):
        for cl in self._classes:
            for st in cl.students:
                if st.name == student_name:
                    return st.father, st.mother

    def print_student_parents(self, student_name):
        result = self.get_student_parents(student_name)
        print(f'Student {student_name} has parents {result}')

    def get_class_teachers(self, class_name):
        for cl in self._classes:
            if cl.name == class_name:
                tc_names = [t.name for t in self._teachers if t.subjects in cl.subjects]
                return tc_names

    def print_class_teachers(self, class_name):
        result = self.get_class_teachers(class_name)
        print(f'Class {class_name} teachers {result}')


class Class_:

    def __init__(self, name, students=None, subjects=None):
        self.name = name
        self.students = students
        self.subjects = subjects

    def __repr__(self):
        return f"{self.name}"


class Person:

    def __init__(self, lastname, firstname, middlename):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.name = f'{lastname} {firstname[0]}.{middlename[0]}.'

    def __repr__(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"


class Teacher(Person):
    def __init__(self, lastname, firstname, middlename, subjects):
        super().__init__(lastname, firstname, middlename)
        self.subjects = subjects

    def __repr__(self):
        return f"{self.firstname} {self.middlename} {self.lastname} ({self.subjects})"


class Student(Person):
    def __init__(self, lastname, firstname, middlename, father=None, mother=None):
        super().__init__(lastname, firstname, middlename)
        self.father = father
        self.mother = mother

    def __repr__(self):
        return f"{self.firstname} {self.middlename} {self.lastname} ({self.father}, {self.mother})"


# Generate parents and students
parents = []
students = []

start = 65
number = 12

for ind in range(start, start+number, 3):
    pr1 = Person(chr(ind),chr(ind),chr(ind))
    pr2 = Person(chr(ind+1), chr(ind+1), chr(ind+1))
    students.append(Student(chr(ind+2), chr(ind+2), chr(ind+2), pr1, pr2))
    parents.extend([pr1, pr2])

print(f'Parents {parents}')
print(f'Students {students}')

# Generate teachers

subjects = ['math', 'phy', 'bio']

teachers = []

start += number
number = len(subjects)

for ind in range(start, start+number):
    teachers.append(Teacher(chr(ind), chr(ind), chr(ind), subjects[ind-start]))

print(f'Teachers {teachers}')

# Generate classes
stcl1 = students[int(len(students)/2):]
sbjcl1 = ['math', 'phy']

stcl2 = students[:int(len(students)/2)]
sbjcl2 = ['math', 'bio']

classes = [Class_('1A', stcl1, sbjcl1), Class_('1B', stcl2, sbjcl2)]

school = School('sch1', classes, teachers)

print(f'School classes {school.get_classes()}')
school.print_class_students('1A')
school.print_student_subjects('L L.L.')
school.print_student_parents('L L.L.')
school.print_class_teachers('1A')
