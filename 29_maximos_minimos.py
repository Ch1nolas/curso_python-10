cant_numeros = 4

print("Ingrese número 1")
num = int(input())

max_numero = num
min_numero = num
pos_max = 1
pos_min = 1

for cont in range(2,cant_numeros+1):
	print("Ingrese número",cont)
	num = int(input())
	if num > max_numero:
		max_numero = num
		pos_max = cont
	elif num < min_numero:
		min_numero = num
		pos_min = cont

print("El máximo es",max_numero,"y salió en la pos.",pos_max)
print("El mínimo es",min_numero,"y salió en la pos.",pos_min)