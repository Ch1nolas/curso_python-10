EDAD_MINIMA = 18
cant_personas_mayores = 0
cant_personas = int(input("Ingrese una cantidad de personas: "))

while cant_personas <= 0:
	cant_personas = int(input("ERROR. Ingrese una cantidad de personas: "))

for cont in range(cant_personas):
	print("Ingrese la edad nº",(cont+1))
	edad = int(input())
	while not (edad >= 1 and edad <= 122):
		print("ERROR. Ingrese la edad nº",(cont+1))
		edad = int(input())
	if edad >= EDAD_MINIMA:
		cant_personas_mayores += 1 # Incrementar en 1

porc = (cant_personas_mayores / cant_personas) * 100
print("El porcentaje de personas mayores de edad es",porc,"%")