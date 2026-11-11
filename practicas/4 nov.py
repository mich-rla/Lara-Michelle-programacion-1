for _ in range (5):
    print("holi")

#while, se repite mientras sea verdadero

contador = 0
while contador <10:
    print(contador)
    contador = contador + 2

#se va a repetir hasta que le des la contraseña correcta porque while es un bucle
clave = ""
while clave != "mich":
    clave = input("Contraseña:")

print ("acceso concedido :) ")

while True:
    print("se ejecuta al menos una vez")
    user_input = input("¿Continuar? (y/n): ")
    if user_input.lower() != 'y': #upper()
        break


contador = 0
for _ in range (5):
    contador = contador + 1
print (contador)

precios = [50, 120, 30]
total = 0
for precio in precios:
    total = total + precio
print(total)

precios =[30, 10, 9, 50, 29, 10]
total = 0
for precio in precios: 
    print(precio)

matriz =[[1,2,3], [4,5,6]]
print(matriz[0][1])   

frutas = ["manzana", "pera"]
frutas.append("uva")  #agrega la cosa al final
frutas.insert(2, "kiwi") #agrega en la posicion que le des
print(frutas)

