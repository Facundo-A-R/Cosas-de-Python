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
            # EJERCICIO 3 – DICCIONARIO
            # Consigna 1:
            # Crear un diccionario llamado jugador con las siguientes claves y valores:
            # "nombre": "Mario"
            # "vidas": 3
            # Se pide:
            # 1. Agregá una nueva clave "nivel" con valor 1.
            # 2. Usá update() para agregar las claves "puntos": 100 y "arma": "espada".
            # 3. Mostrá todas las claves y valores uno por uno con un for

            # Crear el diccionario
            jugador = {"Nombre":"Mario", "Vidas":3}
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            # Mostrar el diccionario
            print(f"Diccionario inicial: {jugador}")

            # 1. Agregar una nueva clave "nivel" con valor 1.
            jugador["Nivel"] = 1
            # Mostrar el diccionario
            print(f"Diccionario después de agregar la clave 'Nivel' con valor 1: {jugador}")

            # 2. Usar update() para agregar las claves "puntos": 100 y "arma": "espada".
            jugador.update({"Puntos": 100, "Arma": "Espada"})
            # Mostrar el diccionario
            print(f"Diccionario después de agregar las claves 'Puntos' y 'Arma' y sus valores 100 y 'Espada' usando update(): {jugador}")

            # 3. Mostrar todas las claves y valores uno por uno con un for
            print("\nMostrando todas las claves y valores del diccionario jugador:")
            for clave, valor in jugador.items():
                print(f"{clave}: {valor}")

            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios

        case "2":
            # Consigna 2:
            # Simular los datos de tres jugadores, con un diccionario de jugadores donde cada clave es el nombre, y el valor es otro
            # diccionario con sus estadísticas.

            # jugadores = {
            #  "Mario": {"vidas": 3, "puntos": 120},
            #  "Luigi": {"vidas": 2, "puntos": 150},
            #  "Peach": {"vidas": 4, "puntos": 90}
            # }

            # 1. Sumar 50 puntos a cada jugador.
            # 2. Si un jugador tiene menos de 3 vidas, incrementarle 1 vida.
            # 3. Mostrar todos los datos actualizados.

            # Crear el diccionario de jugadores
            jugadores = {
            "Mario": {"vidas": 3, "puntos": 120},
            "Luigi": {"vidas": 2, "puntos": 150},
            "Peach": {"vidas": 4, "puntos": 90}
            }

            # Recorrer los jugadores y mostrar sus estadísticas antes de las actualizaciones
            print("\n_______________________________________________________________")
            print("\nEstadísticas iniciales de los jugadores: \n")
            for jugador, estadisticas in jugadores.items():
                print(f"{jugador}: ")
                
                for clave, valor in estadisticas.items():
                    print(f"  {clave}: {valor}")
                
                print("\n")

            print("_______________________________________________________________\n")

            # Actualizar las estadísticas de cada jugador
            print("*****************************************************************")
            print("Proceso de actualizado de estadísticas de los jugadores...")
            print("*****************************************************************")

            # 1. Sumar 50 puntos a cada jugador.
            print("_______________________________________________________________")
            for jugador, estadisticas in jugadores.items():
                # Mostrar el puntaje inicial del jugador
                print(f"\nActualizando estadísticas del puntaje de {jugador}:")
                print(f"  Puntaje inicial: {estadisticas['puntos']}") # Mostrar el puntaje inicial

                # Mostrar el puntaje actualizado
                for clave, valor in estadisticas.items():
                    # Verificar si la clave es "puntos"
                    if clave == "puntos": 
                        estadisticas["puntos"] += 50 # Sumar 50 puntos
                        print(f"  Puntaje actualizado: {estadisticas['puntos']}") # Mostrar el puntaje actualizado

            print("_______________________________________________________________")

            # 2. Si un jugador tiene menos de 3 vidas, incrementarle 1 vida.
            for jugador, estadisticas in jugadores.items():
                # Verificar las vidas del jugador
                print(f"\nVerificando vidas de {jugador}:")
                print(f"  Vidas iniciales: {estadisticas['vidas']}") # Mostrar las vidas iniciales

                # Incrementar vida si es necesario
                for clave, valor in estadisticas.items():
                    # Verificar si la clave es "vidas"
                    if clave == "vidas":
                        # Verificar si el valor es menor que 3
                        if valor < 3:
                            estadisticas["vidas"] += 1
                            print(f"  Vidas actualizadas: {estadisticas['vidas']}") # Incrementar vida
                        else:
                            print(f"  ¡Vidas no actualizadas!") # No incrementar vida
            print("_______________________________________________________________")

            # 3. Mostrar todos los datos actualizados.
            print("\nResumen de estadísticas de los jugadores actualizadas: \n")
            for jugador, estadisticas in jugadores.items():
                print(f"{jugador}: ")

                for clave, valor in estadisticas.items():
                    print(f"  {clave}: {valor}")
                
                print("\n")

            print("_______________________________________________________________")

        case "3":
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            print("\n¡Hasta luego!\n")
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            break
        
        case _:
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            print("\nOpción inválida. Intenta de nuevo.\n")
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios





