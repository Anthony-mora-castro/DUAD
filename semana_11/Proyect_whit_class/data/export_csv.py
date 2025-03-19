import csv
from actions.class_Student import Student  

def export_csv():
    if not Student.students:
        print("No hay datos para exportar.")
        return
    with open("estudiantes.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "group", "spanish", "science", "social_studies", "english", "average"])

        for student in Student.students:
            writer.writerow([
                student.name,
                student.group,
                student.spanish,
                student.science,
                student.social_studies,
                student.english,
                student.average
            ])
        print("Datos exportados correctamente a 'estudiantes.csv'.")

