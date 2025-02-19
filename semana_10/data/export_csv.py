import csv
from actions.get_names_and_grades import students

def export_csv():
    if not students:
        print("No hay datos para exportar.")
        return
    with open("estudiantes.csv", "w",encoding= 'utf-8', newline="") as file:
        headers = ["name", "group", "spanish", "english", "social_studies", "science", "average"]
        csv_writer = csv.DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(students)
    print("Datos exportados correctamente a 'estudiantes.csv'.")

