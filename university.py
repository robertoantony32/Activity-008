from Departament import Departament

class University:
    def __init__(self, name):
        self.__name = name
        self.__departaments = [Departament]

    
    def add_departament(self, new_departament):
        self.__departaments.append(new_departament)
        