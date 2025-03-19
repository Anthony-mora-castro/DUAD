from actions.class_Student import Student  # Importa la clase Student

def ver_top3():
    if len(Student.students) < 3:
        print("No hay suficientes estudiantes para mostrar el top 3.")
        return
    
    # Ordenar por promedio de mayor a menor
    estudiantes_ordenados = sorted(Student.students, key=lambda student: student.average, reverse=True)[:3]
   
    for i, student in enumerate(estudiantes_ordenados, 1):
        print(f"{i}. {student.name} - Promedio: {student.average}")

