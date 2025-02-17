my_list= [12,45,65,23,76,34,76,24,98,56]

if len(my_list ) > 1 :
    primer_elemento = my_list[0]
    ultimo_elemento = my_list[-1]
    my_list[0] = ultimo_elemento
    my_list[-1] = primer_elemento

print(my_list)