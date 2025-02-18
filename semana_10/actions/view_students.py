from actions.get_names_and_grades import students

def view_students():
    if not students:
        print(f'No hay estudiantes registrados')
        return
    for student in students:
        print (student)

