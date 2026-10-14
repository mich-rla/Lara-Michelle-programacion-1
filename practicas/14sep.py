
dato= input("Escribe un numero: ")
print(dato.isdigit())

dato = input("Tu nombre: ")
print(len(dato)> 0)

print("7".isdigit())
print("siete".isdigit())
print("-7".isdigit())

num=input("Ingresa numero del 1-100:")
print("Numero validado como:", (((len(num)>0) & (len(num)<3) & (num.isdigit()))))


#Si es par
num2 = int(input("Ingresa un numero par:"))
print(num2 % 2 == 0)

#Si la edad es valida
edad=input("Escribe tu edad:")
print(len(edad) > 0 and edad.isdigit())

edad = input("Edad: ")
es_valida = edad.isdigit() and (0 < int(edad) < 120)
print(f"¿Edad valida? {es_valida}")
