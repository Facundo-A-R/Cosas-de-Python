# CONSIGNA 1: Inventario básico (Listas + Funciones)
# Objetivo: Crear un sistema de inventario usando listas y funciones.
# Instrucciones:
#     ● Crear una lista que represente el inventario del jugador.
#     ● Escribir funciones para:
#         ○ Agregar un elemento.
#         ○ Eliminar un elemento.
#         ○ Mostrar el inventario
#         ○ Verificar si un objeto está en el inventario

def inventario_inicial():
    inventario = ["poción", 50, "espada", "escudo"]
    return inventario

def agregar_item(inventario, item):
    inventario.append(item)

def eliminar_item(inventario, item):
    if item in inventario:
        inventario.remove(item)
        print("Item eliminado correctamente")
    else:
        print("Este item no existe")

def mostrar_inventario(inventario):
    if inventario:
        print("Inventario:")
        for item in inventario:
            print(f" - {tuple(item)}")
    else:
        print("El inventario está vacío.")

def verificar_objeto_en_inventario(inventario, objeto):
    if objeto in inventario:
        print(f"El objeto '{objeto}' está en el inventario.")
    else:
        print(f"El objeto '{objeto}' no está en el inventario.")


# CONSIGNA 2: Control de enemigos (Diccionarios + Iteración)
# Objetivo: Gestionar enemigos mediante un diccionario y recorrerlos con un bucle.
# Instrucciones:
#     ● Crear un diccionario donde la clave sea el nombre del enemigo y el valor un sub diccionario con su vida y daño.
#     ● Hacer funciones para:
#         ○ Mostrar todos los enemigos
#         ○ Restar la vida a un enemigo específico, pasando por parámetro el daño a impactar.
#         ○ Eliminar al enemigo si su vida llega a 0

def monstruos_iniciales():
    return {
        "goblin": {"vida": 30, "daño": 5},
        "esqueleto": {"vida": 25, "daño": 7},
        "orco": {"vida": 40, "daño": 10}
    }

def mostrar_enemigos(enemigos):
    if enemigos:
        print("Enemigos:")
        for nombre, valores in enemigos.items():
            print(f" - {nombre}: Vida = {valores['vida']}, Daño = {valores['daño']}")
    
def restar_vida_enemigo(enemigos, nombre_enemigo, daño):
    if nombre_enemigo in enemigos:
        enemigos[nombre_enemigo]['vida'] -= daño
        print(f"Se ha restado {daño} de vida a {nombre_enemigo}. Vida restante: {enemigos[nombre_enemigo]['vida']}.")
        actualizar_enemigo(enemigos, nombre_enemigo, enemigos[nombre_enemigo]['vida'])
        if enemigos[nombre_enemigo]['vida'] <= 0:
            eliminar_enemigo(enemigos, nombre_enemigo)
    else:
        print(f"El enemigo {nombre_enemigo} no existe.")

def eliminar_enemigo(enemigos, nombre_enemigo):
    if nombre_enemigo in enemigos:
        del enemigos[nombre_enemigo]
        print(f"El enemigo {nombre_enemigo} ha sido eliminado.")
    else:
        print(f"El enemigo {nombre_enemigo} no existe.")

def actualizar_enemigo(enemigos, nombre_enemigo, nueva_vida):
    if nombre_enemigo in enemigos:
        enemigos[nombre_enemigo]['vida'] = nueva_vida
        #print(f"El enemigo {nombre_enemigo} ha sido actualizado.")

def eliminar_enemigo_de_diccionario(enemigos, nombre_enemigo):
    if nombre_enemigo in enemigos:
        del enemigos[nombre_enemigo]
        print(f"El enemigo {nombre_enemigo} ha sido eliminado.")
    else:
        print(f"El enemigo {nombre_enemigo} no existe.")


# Funciones de los menus
def menu_principal():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Consigna 1")
    print("2. Consigna 2")
    print("3. Salir")
    print("=======================================================\n")

def menu_consigna_1():
    #Menu Consigna 1.
    print("\n===== MENÚ CONSIGNA 1 =====")
    print("1. Lista basica del jugador.")
    print("2. Agregar un elemento.")
    print("3. Eliminar un elemento.")
    print("4. Mostrar el inventario")
    print("5. Verificar si un objeto está en el inventario")
    print("6. Menu Anterior")
    print("=======================================================\n")

def menu_consigna_2():
    #Menu Consigna 2.
    print("\n===== MENÚ CONSIGNA 2 =====")
    print("1. Lista basica del enemigos.")
    print("2. Mostrar todos los enemigos.")
    print("3. Restar la vida a un enemigo específico,\n   pasando por parámetro el daño a impactar.")
    print("4. Eliminar el enemigo del diccionario.")
    print("5. Menu Anterior")
    print("=======================================================\n")


menu_principal()

while True:
    print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
    opcion = input("Selecciona una opción (1-3): ")
    print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios

    match opcion:

        case "1":
            menu_consigna_1()

            while True:
                print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
                opcion = input("Selecciona una opción (1-6): ")
                print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios

                match opcion:

                    case "1":
                        print("Esta es la lista inicial del jugador: \n", inventario_inicial())
                        
                    case "2":
                       
                        elemento = input("Agragar elemento: ")
                        try:
                            agregar_item(inventario, elemento)
                            print("El elemento agregado a la lista con exito: \n", inventario)
                            
                        except NameError:
                            inventario = inventario_inicial()
                            agregar_item(inventario, elemento)
                            print("El elemento agregado a la lista con exito: \n", inventario)

                    case "3":
                        try:
                            print("El inventario es \n", inventario)
                            
                        except NameError:
                            inventario = inventario_inicial()
                            print("El inventario es \n", inventario)

                        item = input("Cual es el item que queres eliminar: ")
                        eliminar_item(inventario, item)
                        print("El inventario es \n", inventario)

                    case "4":
                        try:
                            print("El inventario es \n", inventario)
                            
                        except NameError:
                            inventario = inventario_inicial()
                            print("El inventario es \n", inventario)

                    case "5":
                        try:
                            if inventario == True:
                                item = input("Cual es el objeto que queres buscar: ")
                                verificar_objeto_en_inventario(inventario, item)
                                
                        except NameError:
                            inventario = inventario_inicial()
                            item = input("Cual es el objeto que queres buscar: ")
                            verificar_objeto_en_inventario(inventario, item)
                             
                    case "6":
                        print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
                        print("\nMenu Anterior\n")
                        print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
                        
                        #Menu para los ejercicios de funciones.
                        menu_principal()

                        break
                    
                    case _:
                        print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
                        print("\nOpción inválida. Intenta de nuevo.\n")
                        print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
            
        case "2":
            menu_consigna_2()

            while True:
                print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
                opcion = input("Selecciona una opción (1-5): ")
                print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios

                match opcion:

                    case "1":
                        print("Esta es la lista inicial de los enemigos: \n", monstruos_iniciales())
                        
                    case "2":
                        enemigos = monstruos_iniciales()
                        mostrar_enemigos(enemigos)
                        actualizar_enemigo(enemigos, monstruo, enemigos[monstruo]['vida'])

                    case "3":
                        enemigos = mostrar_enemigos(monstruos_iniciales())
                        monstruo = input("Ingrese el nombre del monstruo: ")
                        dano = int(input("Ingrese el daño a aplicar: "))
                        restar_vida_enemigo(monstruos_iniciales(), monstruo, dano)
                        
                    case "4":
                        mostrar_enemigos(monstruos_iniciales())
                        monstruo = input("Ingrese el nombre del monstruo a eliminar: ")
                        eliminar_enemigo_de_diccionario(monstruos_iniciales(), monstruo)

                    case "5":
                        print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
                        print("\nMenu Anterior\n")
                        print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
                        
                        #Menu para los ejercicios de funciones.
                        menu_principal()

                        break
                    
                    case _:
                        print("_________________________________________________")  # Línea en blanco para separar las salidas de los ejercicios
                        print("\nOpción inválida. Intenta de nuevo.\n")
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

