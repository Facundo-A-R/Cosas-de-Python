#Entrada para activar modo dificil

#Variables
modo_dificil = input("Ingresa Si o No para activar el modo dificil: ")

if modo_dificil == "Si" or modo_dificil == "si":
    print("\nModo dificil activado")
elif modo_dificil == "No" or modo_dificil == "no":
    print("\nModo normal activado")
else:
    print("\nRespuesta invalida")