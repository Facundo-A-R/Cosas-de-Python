import random

#Ejercicio 1
print("Ejercicio 1")
for pasos in range(1, 11):
    print(f"Paso {pasos}")
     
#Ejercicio 2
print("\nEjercicio 2")
for pasos in range(5, 0, -1):
    print(f"Paso {pasos}")

#Ejercicio 3
print("\nEjercicio 3")
posicion = 0
while posicion <= 5:
    print(f"Posición actual {posicion}")
    posicion += 1

#ejercicio 4
print("\nEjercicio 4")
vidas = 3

while vidas > 0:
    print(f"Te quedan {vidas}")
    vidas -=1

if vidas == 0:
    print("Game Over")

"""    
#Ejercicio 5
print("\nEjercicio 5")
#contrasenia = input("Ingresa tu contraseña: ")
intentos = 3

while intentos > 0:
    contrasenia = input("Ingresa tu contraseña: ")

    if contrasenia == "rompepepe":
        print("Hola Pepe podes romper tranquilo")
        break
    else:
        print("La contraseña es incorrecta")
    
    intentos -=1

if intentos == 0:
    print("No dispones de más intentos.")
""" 
""" #Ejercicio 6
print("\nEjercicio 6")
numero_aleatorio = random.randint(1,20)
print(f"Numeero aleatorio {numero_aleatorio}")
intentos_de_juego = 5
es_correcto = False


while intentos_de_juego > 0  and not es_correcto:

    print("-------------------------------------------------")
    numero = int(input("ingresa un numero entre 1 y 20: "))
    
    #Validamos que el numero este dentro del rango 1 a 20
    if numero < 1 or numero > 20:
        print("El número debe estar entre 1 y 20")
        numero = int(input("ingresa un numero entre 1 y 20: "))
        continue
    
    if numero == numero_aleatorio:
        print("-----------------------------------------------")
        print(f"Ganaste el numero era el -> {numero_aleatorio}")
        print("-----------------------------------------------")
        es_correcto = True
        break
    else:
        if intentos_de_juego != 0:
            
            if numero < numero_aleatorio:
                print("-------------------------------------------------")
                print(f"\nEl número es mayor de {numero} y menor de 20")
            else:
                print("-------------------------------------------------")
                print(f"\nEl número es menor de {numero} y mayor de 1")

            print(f"Te quedan {intentos_de_juego - 1} intentos\n")
            print("-------------------------------------------------")

    intentos_de_juego -= 1
    

if not es_correcto:
    print("-----------------------------------------------")
    print(f"Perdiste, el número era -> {numero_aleatorio}")
    print("-----------------------------------------------")
 """
 
#Ejercicio extra
print("\nEjeercicio Extra")
contador = 1
limite = int(input("Ingrese la cantidad de veces que se ejecuta: "))
print(f"\nPasada {contador}")
nombre = input("Ingresa un nombre o ingresa 'fin' para terminar: ")

while (nombre.lower() != "fin") and (contador < limite):
    contador += 1
    print(f"Tu nombre es {nombre}")
    print(f"\nPasada {contador}")
    nombre = input("Ingresa un nombre o ingresa 'fin' para terminar: ")

print(f"\nGracias por todo, pasadas {contador}")