
# mod1_program.py

# Haciendo una suma
suma = 1+2
print(suma)

# Función print()
# Utilizando función print()

print("Hola desde la consola")

# Variables 
sum = 1+2       # Resultado = 3
producto = sum * 3
print("El resultado del producto es:",producto)

# Tipo de datos
planetas_en_el_sistema_solar = 8                     # tipo de dato int 
distancia_a_alfa_centauri = 4.367                    # tipo de dato float
puede_despegar = True                                # tipo de dato booleano
transbordador_que_aterrizo_en_la_luna = "Apollo 11"  # tipo de dato string

# Imprimiendo el tipo de variable 
print("El tipo de variable de distancia es:",type(distancia_a_alfa_centauri))

# Operadores
# Esquema general de una operacion ->  <left-side> <operator> <right-side>
# Aplicando una operación
left_side = 10
right_side = 5
print("Resultado de la operación:",left_side / right_side) # Resultado = 2

#Fechas
from datetime import date
print("Fecha de hoy",date.today())

#Conversion de tipos de datos:
print("Today's date is: " + str(date.today()))

#Entrada de usuario
print("Bienvenido al programa de bienvenida")
name = input("Instroduzca su nombre: ")
print("Saludos " + name)

#Calculadora (suma de dos numeros)
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print("El resultado es",int(first_number) + int(second_number))

