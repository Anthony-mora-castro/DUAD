import csv
from actions.get_names_and_grades import students

def import_csv():
    try:
        with open("estudiantes.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            students.clear()  # Limpia la lista actual de estudiantes
            for fila in reader:
                try:
                    # Convierte los valores a float
                    fila["spanish"] = float(fila["spanish"])
                    fila["english"] = float(fila["english"])
                    fila["social_studies"] = float(fila["social_studies"])
                    fila["science"] = float(fila["science"])
                    fila["average"] = float(fila["average"])
                    
                    # Agrega el estudiante a la lista
                    students.append(fila)
                except ValueError as e:
                    print(f"Error al convertir los datos de la fila {fila}: {e}")
                
            print("Datos importados correctamente de 'estudiantes.csv'.")
    except FileNotFoundError:
        print("No hay un archivo CSV previamente exportado.")
    except KeyError as e:
        print(f"Error: El archivo CSV no tiene la columna esperada: {e}")
    except ValueError as e:
        print(f"Error: Los datos en el archivo CSV no tienen el formato correcto: {e}")


