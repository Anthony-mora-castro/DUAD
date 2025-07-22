from semana_6.ejercico_funciones_3_semana_6 import cadena_invertida
# Tests para ejercicio 3 de la semana 6
def test_cadena_invertida_normal():
    assert cadena_invertida("Se lee al reves") == "sever la eel eS"

def test_cadena_invertida_empty():
    assert cadena_invertida("") == ""

def test_cadena_invertida_one_char():
    assert cadena_invertida("a")

#------------------------------------------------

# Test para ejercicio 4 de la semana 15
from semana_6.ejercico_funciones_4_semana_6 import cant_mayusculas_y_minusculas

def test_cant_mayusculas_y_minusculas_normal():
    mayus, minus = cant_mayusculas_y_minusculas("Yo me llamo Anthony")
    assert mayus == 2
    assert minus == 14

def test_cant_mayusculas_y_minusculas_all_upper():
    mayus, minus = cant_mayusculas_y_minusculas("HOLA")
    assert mayus == 4
    assert minus == 0

def test_cant_mayusculas_y_minusculas_all_lower():
    mayus, minus = cant_mayusculas_y_minusculas("hola")
    assert mayus == 0
    assert minus == 4

def cant_mayusculas_y_minusculas(oracion):
    mayusculas = 0
    minusculas = 0

    for char in oracion:
        if char.isupper():
            mayusculas += 1
        elif char.islower():
            minusculas += 1

    return mayusculas, minusculas

#-------------------------------------------------
# Test para ejercicio 5 de la semana 15
from semana_6.ejercico_funciones_5_semana_6 import ordenar_palabras

def test_ordenar_palabras_normal():
    entrada = "hola-como-estan-me-llamo-hocksan"
    esperado = "como-estan-hocksan-hola-llamo-me"
    assert ordenar_palabras(entrada) == esperado

def test_ordenar_palabras_unica_palabra():
    entrada = "python"
    esperado = "python"
    assert ordenar_palabras(entrada) == esperado

def test_ordenar_palabras_ya_ordenadas():
    entrada = "a-b-c"
    esperado = "a-b-c"
    assert ordenar_palabras(entrada) == esperado

#-------------------------------------------------
# Test para ejercicio 6 de la semana 15
from semana_6.ejercico_funciones_6_semana_6 import numeros_primos

def test_numeros_primos_mixto():
    entrada = [1, 2, 3, 4, 5, 6, 77, 89, 32, 45, 12]
    esperado = [2, 3, 5, 89]
    assert numeros_primos(entrada) == esperado

def test_numeros_primos_todos_primos():
    entrada = [2, 3, 5, 7, 11]
    esperado = [2, 3, 5, 7, 11]
    assert numeros_primos(entrada) == esperado

def test_numeros_primos_sin_primos():
    entrada = [1, 4, 6, 8, 9, 10]
    esperado = []
    assert numeros_primos(entrada) == esperado