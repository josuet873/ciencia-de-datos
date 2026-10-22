# clasificación de temperaturas
# Lista de temperaturas
temperaturas = [25.6, 23.2, 24, 32, 15, 14, -12, 46, 31.8, 30, 30.01, 29.99]

# funciones
for temperatura in temperaturas:

     if temperatura <= 15:
        print(temperatura,"Frío")

     if temperatura > 30:
        print(temperatura,"Calor")

     elif temperatura >= 16:
        print(temperatura,"Agradable")

     elif temperatura <= 30:
        print(temperatura,"Agradable")

