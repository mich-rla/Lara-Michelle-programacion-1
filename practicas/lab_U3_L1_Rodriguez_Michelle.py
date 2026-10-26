#Ejercicio 1 CLASIFICACIÓN POR EDAD 

edad = int(input("ingresa tu edad porifs:"))

if edad <13:
    print("niño")

elif edad <= 17:
    print("adolescente")

else:
    print("adulto")


#Ejercicio 2 VALIDAR ACCESO

usuario = input("Ingresa tu usuario: ")
contraseña = input("Ingresa tu contraseña: ")


if usuario == "michita" and contraseña == "nodal0113":
    print("acceso concedido")

elif usuario == "michita" and contraseña != "nodal0113":
    print("contraseña incorrecta")

elif usuario != "michita" and contraseña == "nodal0113":
    print("usuario no encontrado")

else:
    print("usuario y contraseña incorrectos")

#Ejercicio 3 CALCULADORA DE ENVIO

peso = float(input("ingresa el peso de tu paquete en kg:"))

if peso <= 1:
    print("el costo de envío es de $50")
elif peso <= 5:
    print("el costo de tu envío es de $90")
else:
    print("el costo de tu envío es de $150")
    descuento = 150 * 0.10
    print("tienes un descuento del 10% por lo que tu envío costará:", 150 - descuento)

#Ejercicio 4 CLASIFICAR POR TEMPERATURA

temperatura = float (input("ingresa la temperatura en C°:"))

if temperatura <10:
    print("hoy hace frio")
elif temperatura <= 25:
    print("hoy hace templado")
else:
    print("hoy hace calor")

#Ejercicio 5 CALIFICACION CON LETRAS

calificacion = float (input("ingresa la calificación: "))

if calificacion >=90:
    print("A")
elif calificacion >=80:
    print("B")
elif  calificacion >=70:
    print("C")
elif calificacion >=60:
    print("D")
else:
    print("F")

#Ejercicio 6 DESCUENTO POR MONTO DE COMPRA

monto_compra=float(input("ingresa el monto de tu compra:"))

if monto_compra <500:
    descuento = monto_compra * .20
    print("tu descuento es de :", descuento)
    print("total: ", monto_compra - descuento)

elif monto_compra <=200:
    descuento = monto_compra * .10
    print("tu descuento es de :", descuento)
    print("total: ", monto_compra - descuento)

else:
    print("no hay descuento")

#Ejercicio 7 VALIDAR UN RANGO CON COMPARACION ENCADENADA

numero = int(input("Ingresa un número: "))

if 1 <= numero <= 100:
    print("El número está en el rango")
else:
    print("El número no está en el rango")

#Ejercicio 8 CLASIFICAR EL IMC

peso = float(input("ingresa el peso en kg: "))
estatura = float(input("ingresa la altura en metros: "))

imc = peso / (estatura ** 2)

if imc < 18.5:
    print("Estás bajo peso")
elif 18.5 <= imc < 25:
    print("Estás en un peso saludable")
else:
    print("Estás con sobrepeso")

#Ejercicio 9 TARIFAS DE ELECTRICIDAD


consumo = int(input("Ingresa tu consumo mensual en kWh: "))

if consumo <= 150:
    costo = consumo * 1.20

elif consumo <= 300:
    costo = (150 * 1.20) + ((consumo - 150) * 1.80)

else:
    costo = (150 * 1.20) + (150 * 1.80) + ((consumo - 300) * 2.50)

print("Consumo:", consumo, "kWh")
print("Costo total: $", costo)






