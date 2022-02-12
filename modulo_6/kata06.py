
# Ejercicio 1

print("\nEjercicio 1\n")

# Creacion de lista
planets = ["Mercurio","Venus","Tierra","Marte","Jupiter","Saturno","Urano","Neptuno"]

# Agregando a pluton
planets.append("Pluton")
print("Hay {0} planetas en el sistema solar y el ultimo es {1}".format(len(planets),planets[-1]))

# Ejercicio 2

print("\nEjercicio 2\n")

# Agregando lista de planetas
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

objetivo = input("Dame el nombre del planeta a buscar en la lista: ")

#Buscando el planeta
indice = planets.index(objetivo)
print("El planeta se encuentra en el indice {0} de la lista".format(objetivo))

# Los planetas mas cercanos al sol respecto del que el usario ingreso
print("Los planetas mas cercanos al sol respecto del objetivo son:")
print(planets[0:indice])

# Los planetas mas alejando del sol respecto del objetivo
print("Los planetas mas alejados del sol respecto del objetivo son:")
print(planets[indice+1:])