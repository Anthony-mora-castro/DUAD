contador_nota = 1
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobada = 0
promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0

total_de_notas = int(input("Ingrese la cantidad de notas: "))

while (contador_nota <= total_de_notas):
    print("Ingrese la nota numero ",contador_nota)
    
    nota_actual = int(input("Ingrese la nota: "))
    if (nota_actual < 70 ):
        cantidad_de_notas_desaprobada += 1

        promedio_de_notas_desaprobadas += 1
        contador_nota +=1
    else:
        cantidad_de_notas_aprobadas += 1
        
        promedio_de_notas_aprobadas +=1
        contador_nota +=1 
    promedio_de_notas_total = promedio_de_notas_total + (nota_actual/ total_de_notas)

promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobada

promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas

print("El estudiante teiene esta cantidad de notas aprobadas: ", cantidad_de_notas_aprobadas)
print("")
print("Este es el promedio de notas aprobadas ", promedio_de_notas_aprobadas)
print("")
print("El estudiante tiene esta cantidad de notas desapporbadas: ",cantidad_de_notas_desaprobada)
print("")
print("Este el es promedio de notas desaprobadas: ", promedio_de_notas_desaprobadas)
print("")
print("Este es el promedio total de notas: ", promedio_de_notas_total)