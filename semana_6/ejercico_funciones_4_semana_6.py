def cant_mayusculas_y_minusculas(oracion):
    mayusculas = 0
    minusculas = 0

    for char in oracion:
        if char.isupper():
            mayusculas += 1
        elif char.islower():    
            minusculas += 1
        
    print(f'La cantidad de mayusculas es de: {mayusculas}')
    print(f'La cantidad de minusculas es de: {minusculas}')

oracion = "Yo me llamo Anthony"
cant_mayusculas_y_minusculas(oracion)