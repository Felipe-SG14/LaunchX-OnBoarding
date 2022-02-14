#Modulo 9 - Kata09

#Ejercicio 1

#Funcion que lee 3 niveles de tanques y regresa un informe
from operator import concat


def informe(tanque1,tanque2,tanque3):
    promedio = (tanque1+tanque2+tanque3)/3
    inform = f"""
    Primer tanque:  {tanque1}%
    Segundo tanque: {tanque2}%
    Tercer tanque:  {tanque3}%
    Promedio:       {int(promedio)}%
    """
    return inform

#Probando la funcion

print("\nEjercicio 1\n")
print("Informe: ",informe(60,40,80))

#Funcion que calcula el promedio
def promedio(valores):
    return sum(valores)/len(valores)

#Probando la funcion de promedio
print(f"Probando la funcion de promedio: {promedio([60,40,80])}")

#Uniendo las dos funciones utilizadas
def informe_actualizado(tanque1,tanque2,tanque3):
    lista = [tanque1,tanque2,tanque3]
    inform = f"""
    Primer tanque:  {tanque1}%
    Segundo tanque: {tanque2}%
    Tercer tanque:  {tanque3}%
    Promedio:       {int(promedio(lista))}%
    """
    return inform

#Utilizando función actualizada
print("\nInforme actualizado: ",informe_actualizado(60,40,80))

#Ejercicio 2
print("\nEjercicio 2\n")

#Creando funcion para primer informe
def informe_mision(prelaunch_hour,tiempo_de_vuelo,destino,t_interno,t_externo):
    cadena = f"""
    Tiempo de viaje:        {prelaunch_hour+tiempo_de_vuelo}
    Destino:                {destino}
    Combustible disponible: {t_interno+t_externo}
    """
    return cadena

#Probando primera funcion
print("Primer informe: ",informe_mision(10,400,"Marte",30,40))

#Creando nueva funcion para el informe
def informe_mision_v2(destino,*minutes,**fuel_reservoirs):
    cadena = f"""
    Tiempo de viaje:        {sum(minutes)}
    Destino:                {destino}
    Combustible disponible: {sum(fuel_reservoirs.values())}
    """
    return cadena

#Probando la version 2 del informe
print("\nSegundo informe: ",informe_mision_v2("Marte",10,400,tanque1=30,tanque2=40))

#Creando nueva funcion para el informe
def informe_mision_v3(destino,*minutes,**fuel_reservoirs):
    cadena = f"""
    Tiempo de viaje:        {sum(minutes)}
    Destino:                {destino}
    Combustible disponible: {sum(fuel_reservoirs.values())}

    Informacion de tanques:
    """
    cadena2=""
    nombres = list(fuel_reservoirs.keys())
    valores = list(fuel_reservoirs.values())
    for i in range(0,len(fuel_reservoirs)):
        cadena2+= str(nombres[i])+": "+str(valores[i])+"\n"

    return concat(cadena,cadena2)

#Probando version 3 del informe
print("\nTercer informe: ",informe_mision_v3("Marte",10,400,tanque1=30,tanque2=40,tanque3=70))
