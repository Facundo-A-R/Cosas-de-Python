# Mapa del juego
# Representar un mapa como una matriz (lista de listas) y permitir que el jugador interactúe con este mapa, moviéndose y
# detectando enemigos y metas. El mapa estará representado por una lista de listas. En cada celda, se utilizará:
#   ● "P": Posición del jugador.
#   ● "M": Meta (donde el jugador debe llegar).
#   ● "E": Enemigo (el jugador pierde si pisa esta celda).
#   ● " ": Espacio vacío.
# Se pide crear un mapa que esté representado por una lista 2D, donde cada elemento de la lista interna representará una
# celda del mapa. El jugador (P) se moverá a través del mapa, que tendrá ciertos obstáculos o metas representadas por
# caracteres como M (meta) o E (enemigo).
#   ● Crear una función mostrar_mapa(mapa) que imprima el mapa.
#   ● Agregar funciones para:
#       ○ Mover al jugador (P) en la matriz
#       ○ Detectar si llega a una meta (M)
#       ○ o pisa un enemigo (E)

def crear_mapa(filas, columnas):
    mapa = [[" " for _ in range(columnas)] for _ in range(filas)]
    return mapa

def mostrar_mapa(mapa):
    for fila in mapa:
        print(" | ".join(fila))
        print("-" * (len(fila) * 4 - 1))

def mover_jugador(mapa, pos_jugador, nueva_pos):
    x, y = pos_jugador
    nueva_x, nueva_y = nueva_pos
    if (0 <= nueva_x) and (nueva_x < len(mapa)) and (0 <= nueva_y) and (nueva_y < len(mapa[0])):
        mapa[x][y] = " "
        mapa[nueva_x][nueva_y] = "P"
        return (nueva_x, nueva_y)
    return pos_jugador

def detectar_meta(mapa, pos_jugador):
    x, y = pos_jugador
    if mapa[x][y] == "M":
        print("¡Has llegado a la meta!")
        return True
    return False

def pisar_enemigo(mapa, pos_jugador):
    x, y = pos_jugador
    if mapa[x][y] == "E":
        print("¡Has pisado un enemigo!")
        return True
    return False

# Ejemplo de uso
mapa = crear_mapa(5, 5)
mapa[0][0] = "P"
mapa[1][3] = "E"
mapa[2][2] = "E"
mapa[3][4] = "E"
mapa[4][4] = "M"
mostrar_mapa(mapa)

print("\n")

# Posición inicial del jugador
pos_jugador = (0, 0)
# Mover al jugador
nueva_pos = (1, 3)
pos_jugador = mover_jugador(mapa, pos_jugador, nueva_pos)

mostrar_mapa(mapa)

pos_jugador = nueva_pos  # Actualizar la posición del jugador después de moverlo

# Pisar enemigo
if pisar_enemigo(mapa, pos_jugador):
    mostrar_mapa(mapa)
    print("¡Has perdido!")

print("\n")

# Detectar meta
if detectar_meta(mapa, pos_jugador):
    print("¡Has ganado!")
    mostrar_mapa(mapa)


