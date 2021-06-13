class Departament:
    def __init__(self, name, first_teacher):
        self.__name = name
        self.__teachers = [first_teacher]

    def add_teacher(self, new_teacher):
        self.__teachers.append(new_teacher)

    def get_teachers(self):
        return self.__teachers


dep1 = Departament("EST", "juju")
dep1.add_teacher("juju")
