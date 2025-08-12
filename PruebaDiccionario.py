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
        if clave == "vidas":
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
