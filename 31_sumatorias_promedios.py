cant_numeros = 5
sumatoria = 0

for cont in range(1,cant_numeros+1):
    print("Ingrese número",cont)
    num = int(input())
    sumatoria = sumatoria + num
    # Otra forma de acumular es usando el operador '+='
    # sumatoria += num
    # El '+=' también sirve para contadores:
    # En lugar de: cont = cont + 1
    # Podés escribir: cont += 1
    # También existen el: '-=', '*=', '/=' y muchos otros...

print("La sumatoria de los valores es",sumatoria)
print("El valor promedio es",(sumatoria/cant_numeros))