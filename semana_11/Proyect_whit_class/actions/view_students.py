from actions.class_Student import Student


def view_students():
    if not Student.students:
        print("No hay estudiantes registrados.")
        return
    for student in Student.students:
        print(f"Nombre: {student.name}, Grupo: {student.group}, Promedio: {student.average}")
