import random

numero_secreto = random.randint(1, 10)

numero = 0

while numero != numero_secreto:
    numero = int(input("Adivina el nÃºmero secreto (entre 1 y 10): "))
    
    if numero < numero_secreto:
        print("Muy bajo, intenta nuevamente.")
    elif numero > numero_secreto:
        print("muy alto, intenta nuevamente.")
    else:
        print("Felicidades, Adivino el nÃºmero.")
        print("La respuesta correcta era: ",numero)

# Lo hice usando la libreria Random, yo se como usar de forma basica el Random para cosas como esta.
