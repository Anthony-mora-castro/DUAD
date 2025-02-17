numeros = []

for index in range(10):
    numero = int(input(f"Ingrese el numero {index + 1}: "))  
    numeros.append(numero)

numero_mas_alto = numeros[0]

for numero in numeros:
    if numero > numero_mas_alto:
        numero_mas_alto = numero

print(f"Numeros ingresados: {numeros}")
print(f"El mas alto fue: {numero_mas_alto}")