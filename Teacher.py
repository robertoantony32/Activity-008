class Teacher:
    def __init__(self, name):
        self.__name = name
        self.__subjects = []

    def add_subjects(self, new_subject):
        self.__subjects.append(new_subject)

    def get_subjects(self):
        return self.__subjects

    def get_name(self):
        return self.__name