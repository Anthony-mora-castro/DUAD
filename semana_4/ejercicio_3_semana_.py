numero1 = int(input("Por favor ingrese el primero numero: "))
numero2 = int(input("Por favor ingrese el segundo numero: "))
numero3 = int(input("Por favor ingrese el tercer numero: "))
mayor = 0
if (numero1 > numero2 and numero1 > numero3):
    mayor = numero1
    print("El numero mayor es: ",mayor)

elif (numero2 > numero1 and numero2 > numero3):
    mayor = numero2
    print("El numero mayor es: ",mayor)

elif (numero3 > numero1 and numero3 > numero2):
    mayor = numero3
    print("El numero mayor es: ",mayor)