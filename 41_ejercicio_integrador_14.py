NOMBRE_ESPERADO = "Pepe"
CLAVE_ESPERADA = "1234"
INTENTOS_MAX = 3

nombre = input("Nombre: ")
clave = input("Clave: ")
intento = 1

while not (nombre == NOMBRE_ESPERADO and clave == CLAVE_ESPERADA) and intento < INTENTOS_MAX:
    print("ERROR: CREDENCIALES INVÁLIDAS")
    nombre = input("Nombre: ")
    clave = input("Clave: ")
    intento += 1

if nombre == NOMBRE_ESPERADO and clave == CLAVE_ESPERADA:
    print("¡Acceso concedido!")
else:
    print("¡Cuenta bloqueada!")