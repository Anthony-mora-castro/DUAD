
students = []

def get_grades(materia):
    while True:
        try:
            nota = float(input(f'Ingrese la nota de {materia}: '))
            if 0 <= nota <= 100:
                return nota
            else:
                print('La nota debe estar entre 0 y 100.')
        except ValueError:
            print('Ingrese un número válido.')

def enter_student():
    while True:
        name = input('Nombre completo: ')
        group = input('Ingrese la sección: ')

        spanish = get_grades('Ingrese la nota de Español: ')
        science = get_grades('Ingrese la nota de Ciencias')
        social_studies = get_grades('ingrese la nota de Estudios Sociales')
        english = get_grades('Ingrese la nota de Inglés')

        student = {
            'name': name,
            'group': group,
            'spanish': spanish,
            'science': science,
            'social_studies': social_studies,
            'english': english,
            'average': (spanish + science + social_studies + english) / 4
        }           
        students.append(student) 
    

        continuar = input("¿Desea ingresar otro estudiante? (s/n): ").strip().lower()
        if continuar != 's':
            break
    print("Estudiantes ingresados correctamente.")
    return students


