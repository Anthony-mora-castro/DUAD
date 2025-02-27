from actions.general_average import ver_promedio_general
from actions.get_names_and_grades import enter_student
from actions.view_students import view_students
from actions.view_top3 import ver_top3
import data
import data.export_csv
import data.import_csv 

def show_menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar información de estudiantes")
        print("2. Ver información de todos los estudiantes")
        print("3. Ver top 3 estudiantes con mejor promedio")
        print("4. Ver nota promedio de todos los estudiantes")
        print("5. Exportar datos a CSV")
        print("6. Importar datos desde CSV")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            enter_student()  # Usa la función importada
        elif opcion == '2':
            view_students()  # Usa la función importada
        elif opcion == '3':
            ver_top3()  
        elif opcion == '4':
            ver_promedio_general()  # Usa la función importada
        elif opcion == '5':
            data.export_csv.export_csv()  # Usa la función importada
        elif opcion == '6':
            data.import_csv.import_csv()  # Usa la función importada
        elif opcion == '7':
            print(f'Saliendo del sistema...')
            break
        else:
            print('Ingrese una opcion valida')

                    