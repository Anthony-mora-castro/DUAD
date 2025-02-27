from actions.class_Student import Student

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
        spanish = get_grades('Español')
        science = get_grades('Ciencias')
        social_studies = get_grades('Estudios Sociales')
        english = get_grades('Inglés')

        student = Student(name, group, spanish, science, social_studies, english)

        continuar = input("¿Desea ingresar otro estudiante? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("Estudiantes ingresados correctamente.")
    return Student.students


