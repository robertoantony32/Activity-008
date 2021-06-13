class Departament:
    def __init__(self, name, first_teacher):
        self.__name = name
        self.__teachers = [first_teacher]

    def get_name(self):
        return self.__name

    def add_teacher(self, new_teacher):
        self.__teachers.append(new_teacher)

    def remove_teacher(self, teacher):
        self.__teachers.remove(teacher)

    def get_teachers(self):
        return self.__teachers
