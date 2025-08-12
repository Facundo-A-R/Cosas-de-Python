#Objetivo: Uso de operadores y variables.

#Variables
vida_enemigo = int(input("Definir la vida: "))
ataque = int(input("Definir el ataque: "))
vida_Restante = 0

#Operación
vida_Restante = vida_enemigo - ataque

#Mostrar en pantalla
print(f"\nLa vida restante es {vida_Restante}")

#Calcular daño total

vida_Restante = 0 #Reinicio la variable.
ataque = int(input("Definir el ataque: "))
multiplicador_decimal = float(input("Definir el multiplicador del ataque: "))

#operación
danio = ataque * multiplicador_decimal
vida_Restante = vida_enemigo - danio

#Mostrar en pantalla
print(f"\nLa vida restante es {vida_Restante}")
