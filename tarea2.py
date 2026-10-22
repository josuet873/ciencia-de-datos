# variables de temperatura

temperatures = [25.6, 23.2, 24, 32, 38, 14, -12, 46, 31.8, 44]

for temperature in temperatures:
    if temperature <= 15:
        print(temperature,"It's a good day for drink a coffee")
    elif temperature <=29:
        print(temperature,"Drink a coffee is your choice today, but always I recomended")
    else:
        print("You just need drink cold water")

