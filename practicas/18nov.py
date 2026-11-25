#parametros y retorno

def saludar(nombre):
    print("Hola, ", nombre)

saludar ("Ana")

#return cuando una función regresa ul resulado

def duplicar(numero):
    return numero * 2 #que numero va a duplicar

resultado= duplicar(5) #cuantas veces lo vas a duplicar
print(resultado)


def calcular_iva(precio):
    return precio * 0.16

precio = 345
iva= calcular_iva(precio)
print("IVA:", iva)

def es_mayor_de_edad(edad):
    return edad >= 18

print(es_mayor_de_edad(20))
print(es_mayor_de_edad(15))



board = [[" " for _ in range(3)] for _ in range (3)]
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("--" * 5)

print_board(board)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range (3)) or all (board[i][2 - i] == player for i in range (3)):
        return True
    return False 

import random

numero= random.randint(1, 10)
print(numero)

import math

print(math.sqrt(16))
print(math.pi)


from random import choice

opc= ["piedra", "papel", "tijera"]
print(choice(opc))

import random

numero_secreto = random.randint(1, 100)
print("Adivina el numero del 1 al 100")
print(numero_secreto)


import math

radio = 5
area = math.pi * radio ** 2
print(f"Área del circulo: {area: .2f}")