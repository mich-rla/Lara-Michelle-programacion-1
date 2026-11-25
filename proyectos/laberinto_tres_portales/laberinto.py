
# El laberinto de los tres portales
# Alexa Michelle Rodriguez Lara  219428753
# Programacion | 1 CUGDL |

def mostrar_inicio():
    # Aquí solo es el intro, puro print y dar instrucciones claras

    print("===================================")
    print(" EL LABERINTO DE LOS TRES PORTALES")
    print("===================================")

    print("Bienvenidx a nuestra aventura :)")
    print("Tendras que superar tres laberintos")
    print("Encuentra objetos y evita las trampas!")
    print("Consigue puntos para llegar al final, suerte.")

    print("\nCONTROLES:")
    print("W = Arriba")
    print("S = Abajo")
    print("A = Izquierda")
    print("D = Derecha")

    print("\n¿Estas lista para comenzar?")

    while True:   #Mientras pase esto
        respuesta = input("Escribe S para comenzar o N para salir: ")
        respuesta = respuesta.lower().strip() #lower convierte a minusculas
                                            #strip quita los espacios innecesarios
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("Te dije s o n, no otras teclas -_-")

def mostrar_mapa(laberinto): # esta funcion muestra el laberinto
    
    for fila in laberinto: #este recorre las filas
        for casilla in fila: #este las casillas
            print(casilla, end=" ")  #espacio

        print()

def main():
    #Mich del futuro: aquí incia el juego 

    comenzar = mostrar_inicio()

    if comenzar == True:
        print("\n¡Vamos pues!")

        laberinto = [   #esta es la primera matriz, nivel 1
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", "P", ".", "E", ".", "#", "#"],
            ["#", "#", "#", ".", "#", ".", "#"],
            ["#", "M", ".", ".", "#", ".", "#"],
            ["#", ".", "#", ".", ".", ".", "#"],
            ["#", ".", "D", ".", "#", "S", "#"],
            ["#", "#", "#", "#", "#", "#", "#"]
        ]

        fila_jugador = 1
        columna_jugador = 1

        print("\nNIVEL 1")
        mostrar_mapa(laberinto)

    else:
        print("\nHasta pronto :) ")


main()
