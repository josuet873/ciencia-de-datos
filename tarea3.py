# aqui comienza la tarea 3

#Function
def clasif_temp(temperatura):
     if temperatura < 15:
        return "Frío"
     elif temperatura > 30:
        return "Calor"
     else:
        return "Agradable"

def tempf(temperatura):
    temp_f = temperatura * 9 / 5 + 32
    return temp_f
    
#List
temperaturas = [25.6, 23.2, 24, 32, 15, 14, -12, 46, 31.8, 30, 30.01, 29.99]

#Llamando a la función

for temperatura in temperaturas:
    resultado = clasif_temp(temperatura)
    resultemp = tempf(temperatura)
    print(round(resultemp,1), resultado)