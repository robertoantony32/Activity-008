class University:
    def __init__(self, name):
        self.__name = name
        self.__departaments = []
    
    def add_departament(self, new_departament):
        self.__departaments.append(new_departament)
    
    def get_departaments(self):
        return self.__departaments

    def get_name(self):
        return self.__name
