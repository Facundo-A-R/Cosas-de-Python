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
    return ["poción", 50, "espada", "escudo"]

def agregar_item(inventario, item):
    inventario.append(item)

def eliminar_item(inventario, item):
    if item in inventario:
        inventario.remove(item)

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


# TODO: Menu
# Lista inicial
# inventario_principiante = inventario_inicial()


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
    else:
        print("No hay enemigos en la lista.")

def restar_vida_enemigo(enemigos, nombre_enemigo, daño):
    if nombre_enemigo in enemigos:
        enemigos[nombre_enemigo]['vida'] -= daño
        print(f"Se ha restado {daño} de vida a {nombre_enemigo}. Vida restante: {enemigos[nombre_enemigo]['vida']}.")
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


