class Student:
    students = []  # Lista para almacenar todos los estudiantes

    def __init__(self, name, group, spanish, science, social_studies, english):
        self.name = name
        self.group = group
        self.spanish = spanish
        self.science = science
        self.social_studies = social_studies
        self.english = english
        self.average = self.calculate_average()
        Student.students.append(self)  # Agrega el estudiante a la lista

    def calculate_average(self):
        return (self.spanish + self.science + self.social_studies + self.english) / 4