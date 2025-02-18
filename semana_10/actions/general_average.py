from actions.get_names_and_grades import students  

def ver_promedio_general():
    if not students:
        print("No hay estudiantes registrados.")
        return None  
    
    promedio_general = sum(student["average"] for student in students) / len(students)
    print(f"Promedio general de notas: {promedio_general}")
    return promedio_general  