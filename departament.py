class Departament:
    def __init__(self, name, first_teacher):
        self.__name = name
        self.__teachers = [first_teacher]

    def add_teacher(self, new_teacher):
        self.__teachers.append(new_teacher)
        set(self.__teachers)

    def get_teachers(self):
        return self.__teachers
