#Objetivo: Usar if/elif/else

nivel = int(input("Ingresa los puntos obtenidos: "))

if nivel >= 100:
    print("\nMaestro")
elif nivel >= 70:
    print("\nExperto")
elif nivel >= 40:
    print("\nIntermedio")
else:
    if nivel < 40:
        print("\nPrincipiante")