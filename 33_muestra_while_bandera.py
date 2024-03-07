umbral = 10
sumatoria = 0
cont = 0

while sumatoria < umbral:
    cont += 1 # cont = cont + 1
    print("Ingrese número",cont)
    num = int(input())
    sumatoria += num # sumatoria = sumatoria + num

print("El promedio de valores es",(sumatoria / cont))


# NO HAGAS LO SIGUIENTE, ES UNA MUY MALA PRÁCTICA:
umbral = 10
sumatoria = 0

for cont in range(10000000): # Valor absurdo en el range
    if sumatoria < umbral:
        cont += 1 # cont = cont + 1
        print("Ingrese número",cont)
        num = int(input())
        sumatoria += num # sumatoria = sumatoria + num
    else:
        break # Corte abrupto del ciclo

print("El promedio de valores es",(sumatoria / cont))