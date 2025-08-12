#Menu para los dos ejercicios.
print("\n===== MENÚ PRINCIPAL LISTAS[ ] =====")
print("1. Ejercicio 1")
print("2. Ejercicio 2")
print("3. Salir")

while True:
    opcion = input("Selecciona una opción (1-3): ")

    match opcion:

        case "1":
            # EJERCICIO 1 – LISTAS
            # Consigna 1:
            # Crear una lista llamada enemigos con los siguientes nombres: "zombi", "orco", "dragón".
            # Después se pide:
            # 1. Agregar “fantasma" al final de la lista.
            # 2. Insertar "gólem" en la posición 1.
            # 3. Mostrar todos los enemigos uno por uno usando un for.

            # Crear la lista inicial
            enemigos = ["zombi", "orco", "dragón"]
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            print(f"\nLista inicial de enemigos: {enemigos}")

            # 1. Agregar “fantasma" al final de la lista.
            enemigos.append("fantasma")
            print(f"\nDespués de agregar 'fantasma': {enemigos}")
            
            # 2. Insertar "gólem" en la posición 1.
            enemigos.insert(1, "gólem")
            print(f"\nDespués de insertar 'gólem' en la posición 1: {enemigos}")

            # 3. Mostrar todos los enemigos uno por uno usando un for.
            print("\nLista de enemigos:")
            for enemigo in enemigos:
                print(enemigo)

            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios

        case "2":
            # Consigna 2:
            # Tenés una lista con enemigos que aparecen en pantalla:
            # enemigos = ["zombi", "orco", "zombi", "dragón", "orco", "zombi"]
            # 1. Contar cuántas veces aparece cada tipo de enemigo.
            # 2. Mostrar una lista nueva (enemigos_unicos) sin repeticiones.
            # 3. Mostrar cuántos enemigos hay en total.

            # Crear la lista de enemigos que aparecen en pantalla
            enemigos = ["zombi", "orco", "zombi", "dragón", "orco", "zombi"]
            #enemigos = ["zombi", "orco", "dragón", "orco", "zombi", "fantasma", "gólem"]
            #enemigos = []
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            print(f"\nLista de enemigos en pantalla: {enemigos}")

            # 1. Contar cuántas veces aparece cada tipo de enemigo.
            contador_enemigos = {} #Diccionario
            for enemigo in enemigos:
                if enemigo in contador_enemigos:
                    contador_enemigos[enemigo] += 1
                else:
                    contador_enemigos[enemigo] = 1

            print(f"\nContador de enemigos: {contador_enemigos}")

            # 2.0. Mostrar una lista nueva (enemigos_unicos_1) sin repeticiones.
            enemigos_unicos_1 = list(contador_enemigos.keys())
        
             # 2.1. Mostrar una lista nueva (enemigos_unicos_2) sin repeticiones.
            enemigos_unicos_2 = []
            #Variable enemigo, count recorro los items si se repiten y los cuento
            for enemigo, count in contador_enemigos.items():
                if count == 1:
                    enemigos_unicos_2.append(enemigo)

            # Mostrar el resultado
            print(f"\nEnemigos únicos: {enemigos_unicos_1}")
            print(f"\nEnemigos únicos (sin repeticiones): {enemigos_unicos_2}")
           
            # 3. Mostrar cuántos enemigos hay en total.
            total_enemigos = sum(contador_enemigos.values())
            print(f"\nTotal de enemigos: {total_enemigos}")

            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios

        case "3":
            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios
            print("\n¡Hasta luego!\n")
            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios
            break
        
        case _:
            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios
            print("\nOpción inválida. Intenta de nuevo.\n")
            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios


