def saludar(nombre):
    print("Hola,",nombre)

def calcular_edad(anio_nacimiento):
    edad = 2026 - anio_nacimiento
    return edad

saludar("Josué")
mi_edad = calcular_edad(1994)
print("Tengo", mi_edad, "años")
