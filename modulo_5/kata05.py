
# Modulo 5 - Kata05

# Ejercicio 1
print("\nEjercicio 1\n")

distanciaTierra  = 149597870
distanciaJupiter = 778547200

distancia_entre_planetas = abs(distanciaTierra-distanciaJupiter)
print("Distancias:")
print(distancia_entre_planetas)
print(int(round(distancia_entre_planetas*0.621,0)))

# Ejercicio 2
print("\nEjercicio 2\n")

distance1 = int(input("Dame la primer distancia: "))
distance2 = int(input("Dame la segunda distancia: "))

diff = abs(distance1-distance2)
print("Distancia en KM: ",diff)
print("Distancia en millas",int(round(diff*0.621,0)))