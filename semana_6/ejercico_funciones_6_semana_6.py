def verificar_primos(numero):
    if numero <= 1:
        return False
    for i in range (2, numero):
        if numero % i == 0:
            return False
    return True

def numeros_primos(lista_numeros):
    primos = []
    for numero in lista_numeros:
        if verificar_primos(numero):
            primos.append(numero)
    return primos

numeros = [1, 2, 3, 4, 5, 6, 77, 89, 32, 45, 12]
resultado = numeros_primos(numeros)
print(resultado)