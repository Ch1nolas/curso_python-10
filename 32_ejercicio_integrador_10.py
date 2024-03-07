productoria = 1
numero = int(input("Ingrese un número natural: "))

if numero >= 0:
    for cont in range(1,numero+1):
        productoria = productoria * cont
        # productoria *= cont
    print("El factorial de",numero,"es",productoria)
else:
    print("No existe el factorial de un número negativo")