nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = int(input("Ingrese la edad: "))

if (edad >= 0 and edad < 5 ):
    print(f'{nombre} {apellido} es un bebe')

elif (edad >= 5 and edad < 8 ):
    print(f'{nombre} {apellido} es un niÃ±o')

elif (edad >= 8 and edad < 12 ):
    print(f'{nombre} {apellido} es un preadelocente')

elif (edad >= 12 and edad < 18 ):
    print(f'{nombre} {apellido} es un adelocente')

elif (edad >= 18 and edad < 35 ):
    print(f'{nombre} {apellido} es un adulto joven')

elif (edad >= 35 and edad < 64 ):
    print(f'{nombre} {apellido} es un adulto')

elif (edad >= 65 ):
    print(f'{nombre} {apellido} es un adulto mayor')

# Esas son las edades generalaes de cada etapa que encontre