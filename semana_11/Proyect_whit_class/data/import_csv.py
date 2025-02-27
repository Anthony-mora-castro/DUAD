import csv
from actions.class_Student import Student

def import_csv():
    try:
        with open("estudiantes.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  
            Student.students.clear()  
            for fila in reader:
                
                student = Student(
                    name=fila[0],
                    group=fila[1],
                    spanish=float(fila[2]),
                    science=float(fila[3]),
                    social_studies=float(fila[4]),
                    english=float(fila[5])
                )
            print("Datos importados correctamente de 'estudiantes.csv'.")
    except FileNotFoundError:
        print("No hay un archivo CSV previamente exportado.")
    except ValueError as e:
        print(f"Error: Los datos en el archivo CSV no tienen el formato correcto: {e}")


