from actions.class_Student import Student  # Importa la clase Student

def ver_promedio_general():
    if not Student.students:
        print("No hay estudiantes registrados.")
        return
    
    # Calcular el promedio general
    promedio_general = sum(student.average for student in Student.students) / len(Student.students)
    print(f"Promedio general de notas: {promedio_general}")