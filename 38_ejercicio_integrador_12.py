CARACTER = "X"

ancho = int(input("Ingrese el ancho: "))
while ancho <= 0:
    ancho = int(input("ERROR. Ingrese el ancho: "))

alto = int(input("Ingrese el alto: "))
while alto <= 0:
    alto = int(input("ERROR. Ingrese el alto: "))

for fila in range(alto):
    for col in range(ancho):
        print(CARACTER,end="") # Imprime y deja el cursor en el mismo renglón
    print() # Para saltar una línea
