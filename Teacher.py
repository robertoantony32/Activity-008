class Teacher:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subjects(self, new_subject):
        self.subjects.append(new_subject)