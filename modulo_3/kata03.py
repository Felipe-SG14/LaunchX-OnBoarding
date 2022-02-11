
# Módulo 3 - Kata03


# Ejercicio 1
print("\nEjercicio 1 \n")
asteroide_vel = 49
print("Un asteroide se acerca a una velocidad de: "+str(asteroide_vel) + "km/s")
if (asteroide_vel>25):
    print("¡Advertencia!")
else:
    print("No hay de que preocuparse")

# Ejercicio 2
print("\nEjercicio 2 \n")
asteroide_vel = 19
print("Un asteroide se acerca a una velocidad de: "+str(asteroide_vel) + "km/s")
if (asteroide_vel>20):
    print("Se produce el rayo de luz")
elif (asteroide_vel==20):
    print("Se produce el rayo de luz")
else:
    print("No se produce el rayo de luz :(")

# Ejercicio 3
asteroide_vel = 20
asteroide_tam = 40
print("\nEjercicio 3 \n")
if ((asteroide_tam>25 and asteroide_tam<1000) and asteroide_vel>25):
    print("¡Advertencia! El asteroide chocara en al tierra")
elif (asteroide_vel>20):
    print("Se produce el rayo de luz")
elif (asteroide_tam<=25):
    print("El asteroide se quemo en la atmosfera")
else:
    print("Sin novedades")
