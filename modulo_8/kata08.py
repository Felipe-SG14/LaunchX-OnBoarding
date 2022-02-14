#Modulo 8 - Kata08

#Ejercicio 1
print("\nEjercicio 1\n")

#Creacion del diccionario
planet = {
    "name"  : "Mars" ,
    "moons" : 2
}

#Mostrando la informacion del planeta
print("El nombre del planeta es {0} y tiene {1} lunas".format(planet["name"],planet.get("moons")))

#Creando diccionario y agregandolo al diccionario planeta
planet["circunferencia (km)"] ={
    "polar":6752,
    "equatorial":6792
}

#Imprimiendo datos del diccionario actualizado
print("\nEL nombre del planeta es {0} y tiene una circunferencia polar de {1}".format(planet["name"],planet["circunferencia (km)"]["polar"]))

#Ejercicio 2
print("\nEjercicio 2\n")

#Definicion del diccionario
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

#Almacenando el numero de lunas de los planetas
moons = planet_moons.values()

#Calculando el numero total de lunas y planetas
total_moons = sum(moons)
planets = len(planet_moons.keys())

#Calculando el promedio
promedio = total_moons/planets

#Out
print("Hay {0} planetas, en promedio cada uno tiene {1} lunas".format(planets,promedio))
