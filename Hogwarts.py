# Contexto:
# Estás programando un sistema para administrar estudiantes, hechizos y exámenes en una escuela mágica (como
# Hogwarts). Los estudiantes aprenden hechizos, rinden pruebas y acumulan puntos.

import array

#Menu para los dos ejercicios.
print("\n===== MENÚ PRINCIPAL (HOGWARTS) =====")
print("1. 1ERA PARTE: Hechizos y Listas")
print("2. 2DA PARTE: Alumnos y Puntajes")
print("3. 3ERA PARTE: Exámenes y Notas")
print("4. 4TA PARTE: Sistema de Calificaciones")
print("5. Salir")
print("=======================================\n")

while True:
    print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
    opcion = input("Selecciona una opción (1-5): ")
    print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios

    match opcion:

        case "1":
            # 1ERA PARTE:
            # 1. Crear una lista llamada hechizos_basicos con: "Lumos", "Alohomora", "Wingardium Leviosa"
            # 2. Simular que un estudiante intenta usar un hechizo (ejemplo: hechizo = "Expelliarmus")
            # 3. Si el hechizo está en la lista, mostrar "Hechizo lanzado con éxito"
            # 4. Si no, mostrar "Ese hechizo no está aprendido aún”

            hechizos_basicos = ["Lumos", "Alohomora", "Wingardium Leviosa"]
            # hechizo = "Expelliarmus"
            hechizo = input("Ingresa el hechizo que deseas lanzar: ")

            # Normalizar la entrada del usuario metodo title()
            if hechizo.title() in hechizos_basicos:
                print("\nHechizo lanzado con éxito")
            else:
                print("\nEse hechizo no está aprendido aún")
            
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios

        case "2":
            # 2DA PARTE:
            # Crear un diccionario alumnos con los nombres como claves y su puntaje en hechizos como valores:
            # alumnos = {
            # "Harry": 80,
            # "Hermione": 95,
            # "Ron": 60
            # }
            # Recorrer el diccionario y:
            # 1. Si el puntaje es mayor a 90, mostrar "Excelente".
            # 2. Si está entre 70 y 90, mostrar "Muy bien".
            # 3. Si es menor a 70, mostrar "Debe practicar más".

            alumnos = {
                "Facundo": 100,
                "Harry": 80,
                "Hermione": 95,
                "Ron": 60
            }
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            print("Alumnos y sus puntajes:\n")
            
            for nombre, puntaje in alumnos.items():
                if puntaje > 90:
                    print(f"{nombre}: Excelente")
                elif 70 <= puntaje <= 90:
                    print(f"{nombre}: Muy bien")
                else:
                    print(f"{nombre}: Debe practicar más")
            
            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios

        case "3":           
            # 3ERA PARTE
            # Consigna:
            # Crear un array con los puntajes obtenidos por un alumno en sus 5 exámenes mágicos: [70, 85, 60, 90, 75]
            # Calcular:
            # 1. El puntaje total
            # 2. El promedio
            # 3. Cuántas veces obtuvo más de 80 puntos

            puntajes_examenes = array.array('i', [70, 85, 60, 90, 75])  # Puntajes de los exámenes
            puntaje_total = sum(puntajes_examenes)  # Sumar todos los puntajes
            promedio = puntaje_total / len(puntajes_examenes)  # Calcular el promedio
            cant_veces_mas_80 = 0  # Contador de veces con más de 80 puntos

            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            print(f"Puntajes obtenidos en los exámenes: {tuple(puntajes_examenes)}") # Mostrar los puntajes en una tupla con el metodo tuple()
            # Contar cuántas veces se obtuvo más de 80 puntos
            for puntaje in puntajes_examenes:
                if puntaje > 80:
                    cant_veces_mas_80 += 1

            print(f"\nEl promedio de los exámenes es: {promedio:.2f}")
            print(f"Cantidad de veces con más de 80 puntos: {cant_veces_mas_80}")

            print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios

        case "4":
            # 4TA PARTE
            # Simular un sistema de calificaciones mágicas:
            # Crear un diccionario estudiantes donde cada valor sea otro diccionario con:
            # "hechizos_aprendidos": lista
            # "puntos": entero
            # "examenes": array de notas
            # Calcular y mostrar:
            # 1. El promedio de exámenes
            # 2. Si aprendió más de 3 hechizos
            # 3. Si tiene más de 250 puntos → mostrar "¡Graduado!”

            # Diccionario de estudiantes de Hogwarts
            estudiantes = {
                "Facundo": {
                    "hechizos_aprendidos": ["Expelliarmus", "Incendio", "Expecto Patronum", "Lumos", "Alohomora"],
                    "puntos": 290,
                    "examenes": array.array('i', [95, 90, 100])
                },
                "Harry": {
                    "hechizos_aprendidos": ["Expelliarmus", "Lumos", "Alohomora", "Expecto Patronum"],
                    "puntos": 300,
                    "examenes": array.array('i', [95, 90, 85])
                },
                "Hermione": {
                    "hechizos_aprendidos": ["Aguamenti", "Incendio", "Stupefy", "Expecto Patronum"],
                    "puntos": 350,
                    "examenes": array.array('i', [95, 100, 90])
                },
                "Ron": {
                    "hechizos_aprendidos": ["Riddikulus", "Wingardium Leviosa"],
                    "puntos": 200,
                    "examenes": array.array('i', [70, 75, 80])
                }
            }

            # Mostrar información de los estudiantes
            for nombre, info in estudiantes.items():
                print(f"\nEstudiante: {nombre}")
                for clave, valor in info.items():
                    # Mostrar información de cada clave y valor usando el metodo isinstance(objeto, tipo)
                    if isinstance(valor, list):
                        print(f"  {clave}: {tuple(valor)}")
                    elif isinstance(valor, array.array):
                        print(f"  {clave}: {tuple(valor)}")
                    else:
                        print(f"  {clave}: {valor}")

            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios

            for nombre, info in estudiantes.items():
                promedio_examenes = sum(info["examenes"]) / len(info["examenes"])  # Calcular promedio de exámenes
                aprendio_hechizos = len(info["hechizos_aprendidos"]) > 3  # Verificar si aprendió más de 3 hechizos
                tiene_puntos = info["puntos"] > 250  # Verificar si tiene más de 250 puntos

                # Mostrar información del estudiante
                print(f"Estudiante: {nombre}")
                print(f"Promedio de exámenes: {promedio_examenes:.2f}")

                if aprendio_hechizos:
                    print(f"Hechizos aprendidos: {len(info['hechizos_aprendidos'])} hechizos")
                else:
                    print("No aprendió más de 3 hechizos.")

                print(f"Puntos: {info['puntos']}")
                if tiene_puntos:
                    print("¡Graduado!\n")
                else:
                    print("No graduado.\n")

            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios

        case "5":
            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios
            print("\n¡Hasta luego!\n")
            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios
            break
        
        case _:
            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios
            print("\nOpción inválida. Intenta de nuevo.\n")
            print("_________________________________________________\n")  # Línea en blanco para separar las salidas de los ejercicios

            pass