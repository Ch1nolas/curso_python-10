CARACTER = "*"
ESPACIO = " "
base = int(input("Ingrese la base (impar y mayor a 1): "))
while not (base > 1 and base % 2 != 0):
    base = int(input("ERROR. Ingrese la base (impar y mayor a 1): "))

espacios_iniciales = base // 2 # División entera

for cont_caracteres in range(1,base+1,2):
    # Imprimir los espacios
    for cont_espacios in range(espacios_iniciales):
        print(ESPACIO,end="") # Imprime y deja el cursor en el mismo renglón
    espacios_iniciales -= 1 # En el próximo renglón habrá un espacio menos
    # Imprimir los caracteres
    for col in range(cont_caracteres):
        print(CARACTER,end="") # Imprime y deja el cursor en el mismo renglón
    print() # Para saltar una línea