
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

def mover_jugador(fila, columna, movimiento): #solo para mover al jugador con las teclas wsad

    if movimiento == "w":
        fila = fila - 1 #arriba

    elif movimiento == "s":
        fila = fila + 1 #abajo

    elif movimiento == "a":
        columna = columna - 1 #izq

    elif movimiento == "d":
        columna = columna + 1 #der

    return fila, columna

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

        while True: #repetimos el movimiento varias veces (mientras esto pase)

            movimiento = input("\n¿Para donde le damos?: ") #pedimos una instruccion
            movimiento = movimiento.lower().strip() # convierte a minusculas

            if movimiento not in ["w", "a", "s", "d"]:
                print("Usa las teclas correctas -_-")
                continue #por si presionan otra tecla

            nueva_fila, nueva_columna = mover_jugador(
                fila_jugador, columna_jugador, movimiento
            )

            if laberinto[nueva_fila][nueva_columna] == "#": #es un tope, para que no
                print("Ups, chocaste con la pared!")        #atraviese la pared

            else:
                laberinto[fila_jugador][columna_jugador] = "." #borra la posicion

                fila_jugador = nueva_fila
                columna_jugador = nueva_columna

                laberinto[fila_jugador][columna_jugador] = "P" #la nueva posición

            mostrar_mapa(laberinto)

    else:
        print("\nHasta pronto :) ")


main()
