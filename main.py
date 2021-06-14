from Departament import Departament
from Subject import Subject
from Teacher import Teacher
from University import University


university_1 = University("Universidade Estadual do Amazonas")

teacher_1 = Teacher("Professor 1")
teacher_2 = Teacher("Professor 2")
teacher_3 = Teacher("Professor 3")

subject_1 = Subject("m1")
subject_2 = Subject("m2")
subject_3 = Subject("m3")
subject_4 = Subject("m4")

teacher_1.add_subjects(subject_1)

teacher_2.add_subjects(subject_2)

teacher_3.add_subjects(subject_4)
teacher_3.add_subjects(subject_3)


departament_1 = Departament("EST", teacher_1)
departament_1.add_teacher(teacher_2)
departament_1.add_teacher(teacher_3)
university_1.add_departament(departament_1)

print(university_1.get_name())

for departament in university_1.get_departaments():
    print(departament.get_name())
    for teacher in departament.get_teachers():
        print(teacher.get_name(), [x.get_name() for x in teacher.get_subjects()])
    print()
