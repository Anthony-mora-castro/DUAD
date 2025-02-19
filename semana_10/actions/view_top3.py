from actions.get_names_and_grades import students  

def ver_top3():
    if len(students) < 3:
        print("No hay suficientes estudiantes para mostrar el top 3.")
        return
    
    def get_average(student):
        return student["average"]
    
    students_in_order = sorted(students, key=get_average, reverse=True)[:3]
    
    for i, student in enumerate(students_in_order, 1):
        print(f"{i}. {student['name']} - average: {student['average']}")

