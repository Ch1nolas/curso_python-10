categoria = input("Ingrese categoría: A, B, C: ")

# # Otra forma de poner la condición...
# while categoria != "A" and categoria != "B" and categoria != "C":
while not (categoria == "A" or categoria == "B" or categoria == "C"):
    categoria = input("ERROR. Ingrese categoría: A, B, C: ")

print("Continuamos con una categoría válida ;)")