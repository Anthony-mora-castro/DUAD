def mostrar_menu():
    print("\n--- Calculadora ---")
    print("Numero actual:", numero_actual)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado")
    print("6. Salir")

def obtener_numero():
    while True:
        try:
            numero = float(input("Ingrese un numero: "))
            return numero
        except ValueError:
            print("Error: Por favor ingrese un nÃºmero valido.")

def main():
    global numero_actual
    numero_actual = 0

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Error: Por favor ingrese un nÃºmero valido.")
            continue

        if opcion == 1:
            numero = obtener_numero()
            numero_actual += numero
        elif opcion == 2:
            numero = obtener_numero()
            numero_actual -= numero
        elif opcion == 3:
            numero = obtener_numero()
            numero_actual *= numero
        elif opcion == 4:
            numero = obtener_numero()
            if numero == 0:
                print("Error: No se puede dividir por cero.")
            else:
                numero_actual /= numero
        elif opcion == 5:
            numero_actual = 0
            print("Resultado borrado.")
        elif opcion == 6:
            print("Saliendo de la calculadora...")
            break
        else:
            print("Error: Opcion no valida. Por favor seleccione una opcion del 1 al 6.")

if __name__ == "__main__":
    main()
    def mostrar_menu():
        print("\n--- Calculadora ---")
        print("Numero actual:", numero_actual)
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Borrar resultado")
        print("6. Salir")

def obtener_numero():
    while True:
        try:
            numero = float(input("Ingrese un numero: "))
            return numero
        except ValueError:
            print("Error: Por favor ingrese un numero valido.")

def main():
    global numero_actual
    numero_actual = 0

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Error: Por favor ingrese un numero valido.")
            continue

        if opcion == 1:
            numero = obtener_numero()
            numero_actual += numero
        elif opcion == 2:
            numero = obtener_numero()
            numero_actual -= numero
        elif opcion == 3:
            numero = obtener_numero()
            numero_actual *= numero
        elif opcion == 4:
            numero = obtener_numero()
            if numero == 0:
                print("Error: No se puede dividir por cero.")
            else:
                numero_actual /= numero
        elif opcion == 5:
            numero_actual = 0
            print("Resultado borrado.")
        elif opcion == 6:
            print("Saliendo de la calculadora...")
            break
        else:
            print("Error: Opcion no valida. Por favor seleccione una opcion del 1 al 6.")

if __name__ == "__main__":
    main()