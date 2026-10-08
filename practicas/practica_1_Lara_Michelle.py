#Reconocer y utilizar los tipos de datos básicos de Python (int, float, str, bool), identificarlos con type  y distimguir emtre textos y numero al operar con ellos.

#Ejercicio 1 DATOS PERSONALES
nombre = "Michelle"
edad = 25
ciudad = "Guadalajara"
print(nombre, edad, ciudad)

#Ejercicio 2 ACTUALIZAR UN CONTADOR

CONTADOR=0
CONTADOR=CONTADOR+1
print(CONTADOR)
CONTADOR=CONTADOR+1
print(CONTADOR)
CONTADOR=CONTADOR+1
print(CONTADOR)

#Ejercicio 3 CONSTANTE DE CONVERSION
PULGADAS_A_CM=2.54
PULGADAS=22
CM=PULGADAS*PULGADAS_A_CM
print(CM)

#Ejercicio 4 AREA DE UN RECTANGULO

BASE=32
ALTURA=6
PERIMERO=2*(BASE+ALTURA)
print(f"El area del rectagulo es: {BASE*ALTURA}")
print(f"El perimetro del rectangulo es: {PERIMERO}")

#Ejercicio 5 TOTAL CON IVA

IVA=0.16
precio=float(input("Ingrese el precio sin IVA: "))
total=(precio + precio*IVA)
print(f"El total sin IVA es: {precio}")
print(f"El total con IVA es: {total}")
precio=float(input("Ingrese el precio sin IVA: "))
total=(precio + precio*IVA)
print(f"El total sin IVA es: {precio}")
print(f"El total con IVA es: {total}")

#Ejercicio 6 INTERCAMBIO DE VALORES

a=5
b=10

print("Antes del intercambio:")
print("a=", a)
print("b=", b)

temp=a
a=b
b=temp

print("Despuués del intercambio:")
print("a=", a)
print("b=", b)

#Ejercicio 7 IDENTIFICAR CON UN TYPE()

entero=100
decimal=3.5
texto="michita"
boleano=True

print(type(entero))
print(type(decimal))
print(type(texto))
print(type(boleano))

#Ejercicio 8 CONVRTIR TIPOS

texto="25"
numero=int(texto)
print(numero, type(numero))

entero=60
texto2=str(entero)
print(texto2, type(texto2))

#Ejercicio 9 BOOLEANOS Y COMPARACIONES

a=10
b=5
mayor=a>b
print(mayor, type(mayor))