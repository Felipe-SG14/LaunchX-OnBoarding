# Modulo 7 - Kata07 

print("\n Ejercicio 1 \n\n")

#Declaracion de variables

new_planet = ""
planets = []

#Llenando la lista de planetas
while (new_planet.lower()!="done"):
    if new_planet:
        planets.append(new_planet)
    new_planet = input("Ingresa el nombre de un planeta: ")

#Imprimiendo los valores de la lista
print("\n Ejercicio 2 \n\n")
print("Lista de planetas agregados")
for planet in planets:
    print(planet)

