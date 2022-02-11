
# Ejercicio 1 - Transformar cadenas

text = "Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."

# Diviendo el texto en sus oraciones
oraciones = text.split(". ")

print("\nEjercicio 1 - Transformar cadenas\n")
print("\nLista con las oraciones")
print(oraciones)

key_words = ["average","temperature","distance"]
print("\nLista de palabras clave")
print(key_words)

print("\nOraciones que incluyen las palabras claves que hablan acerca de la Luna")
for i in range(0,len(oraciones)):
    for j in range(0,len(key_words)):
        if ((key_words[j] in oraciones[i]) and ('Moon' in oraciones[i])):
            print(oraciones[i])

print("\nOraciones que incluyen las palabras claves que hablan acerca de la Luna y cambiando C a Celsius")
for i in range(0,len(oraciones)):
    for j in range(0,len(key_words)):
        if ((key_words[j] in oraciones[i]) and ('Moon' in oraciones[i])):
            print(oraciones[i].replace("C","Celsius"))

print("\nEjercicio 2 - Formateando cadenas\n")
# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

#Creación del titulo
titulo = f"gravity facts about {name}"

#Creacion de plantilla
plantilla = """---------------------------------------------
Planet Name: {1}
Gravity on {0}: {2} m/s
""".format(name,planet,gravity*1000)

#Union de cadenas
plantilla_final = """{0}
{1}""".format(titulo.title(),plantilla)

print("Plantilla final\n")
print(plantilla_final)

print("\nUtilizando informacion diferente\n")

name = "Ganimedes"
gravity = 0.00143 # in kms
planet = "Marte"

#Nueva Plantilla
new_plantilla = """
Gravity Facts About {0}
-----------------------------------------------------------
Planet Name: {1}
Gravity on {0}: {2} m/s
""".format(name,planet,gravity*1000)

print(new_plantilla)


