def ordenar_palabras(palabras):
    lista_palabras= palabras.split('-')
    lista_palabras.sort()

    resultado = '-'.join(lista_palabras)

    return resultado

string = "hola-como-estan-me-llamo-hocksan"
resultado = ordenar_palabras(string)
print(resultado)