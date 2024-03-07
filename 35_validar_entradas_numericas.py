numero = int(input("Ingrese un número entre 1 y 10: "))

# Otra forma de poner la condición...
# while numero < 1 or numero > 10:
while not (numero >= 1 and numero <= 10):
    numero = int(input("ERROR. Ingrese un número entre 1 y 10: "))

for c in range(1,11):
	print(numero,"x",c,"=",(numero * c))

