import array

#Menu para los dos ejercicios.
print("\n===== MENÚ PRINCIPAL Arreglos(array,[tipo_dato,]) =====")
print("1. Ejercicio 1")
print("2. Ejercicio 2")
print("3. Salir")
print("=======================================================\n")

while True:
    print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
    opcion = input("Selecciona una opción (1-3): ")
    print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios

    match opcion:

        case "1":
            # EJERCICIO 2 – ARREGLOS (array)
            # Consigna:
            # Usando el módulo array, creá un arreglo de enteros llamado puntos con los valores [10, 20, 30].
            # Se pide:
            # 1. Agregar el número 40 al final.
            # 2. Insertar el número 25 en la posición 2.
            # 3. Mostrar todos los valores con un bucle for

            #Array inicial
            punto = array.array("i", [10, 20, 30])
            print("\n0. Array inicial.")
            for numero in punto:
                print(f"El arreglo es: {numero}")

            print("\n1. Agregar el número 40 al final.")
            punto.append(40)
            for numero in punto:
                print(f"El arreglo es: {numero}")

            print("\n2. Insertar el número 25 en la posición 2.")
            punto.insert(2, 25)
            for numero in punto:
                print(f"El arreglo es: {numero}")

            print("\n3. Mostrar todos los valores con un bucle for")
            for numero in punto:
                print(f"El arreglo es: {numero}")
            
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios

        case "2":
            # EJERCICIO 2 – ARREGLOS (array) (Nivel intermedio)
            # Consigna:
            # Usá el módulo array para simular los puntos de vida recibidos por un personaje en 5 turnos de ataque enemigo.
            # 1. Cargar un arreglo llamado daños con: [10, 5, 15, 0, 20]
            # 2. Restar cada daño al valor de vida del jugador (empieza con 50)
            # 3. Mostrar el valor de vida restante después de cada turno.
                
            #Array inicial
            danio = array.array("i", [10, 5, 15, 0, 20]) # Arreglo de daños
            print("\n0. Array inicial.")
            print(f"El arreglo es: {sorted(danio)}") # Ordenado

            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            #vida = 50
            vida = int(input("\nIngrese la vida inicial del jugador: ")) # Vida inicial
            print("_________________________________________________")

            #Simulación de turnos con el arreglo de daños inicial sin ordenar
            for i in danio:
                print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
                print(f"\nTurno {danio.index(i) + 1} de ataque enemigo: {i}") #Turno
                vida -= i
                print(f"Vida restante: {vida}") #Vida restante
                print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
        
        case "3":
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            print("\n¡Hasta luego!\n")
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            break
        
        case _:
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            print("\nOpción inválida. Intenta de nuevo.\n")
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
