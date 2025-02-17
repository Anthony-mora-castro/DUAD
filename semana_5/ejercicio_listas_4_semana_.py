my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_pares = []

for numero in my_list:
    if numero % 2 == 0:
        lista_pares.append(numero)

my_list = lista_pares
print(my_list) 
