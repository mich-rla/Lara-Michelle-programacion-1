#control de bucle break/continue

for numero in range(1,10):
    if numero ==5:
        break
print (numero)  #si está alineado al for, imprime solo el numero,, si está identado con if, imprime 1, 2, 3,4

for numero in range(1,6):
    if numero ==2:
        continue
    print(numero) #solo estamos quitando el valor que le dijimos qu eno queremos
    #si lo idento con for, solo me imprime el ultimo numero

numeros = [4, 9, -2, 7, -5]
for n in numeros:
    if n <0:
        print("encontrado: ", n)
        break #solo va a imprimir la primera respuesta porque le pusimos break, si lo quitamos nos imprime todas las respuestas

for n in range (1, 11):
    if n % 3 == 0:
        continue
    print(n)

#DICCIONARIOS

alumno= {"nombre": "Ana", "edad": 20, "carrera": "Creatividad"}
print(alumno ["nombre"]) #claves
alumno["edad"] = 21 #modifica
alumno ["promedio"] = 9.5 #inserta
print(alumno)
del alumno ["carrera"] #elimina
print(alumno)
for clave, valor in alumno.items():
    print(clave, ":", valor)

d1 = {"Nombre": "Sara", "Edad": 27, "Documento": 1003882} #usando llaves
d2 = dict(Nombre="Sara", Edad=27, Documento=1003882) #usando dict()

print(d1.keys()) # dict_keys (['Nombre', 'Edad', 'Documento'])
print(d1.values()) #dict_values(['Laura', 27, 1003882])
d1.pop("Edad")
del d1["Documento"]
d2.clear()
print(d1,d2)
nombre= d1.get("Nombre")
nombre_seguro= d1.get("Nombre", "No especificado")
d1.update ({"País": "España"})
print(d1)

cuentas=[
{"tarjeta": "123456789", "nip", "4321", "saldo": 5000.0}
{"tarjeta": "555555555", "nip", "1111", "saldo": 2500.0}
{"tarjeta": "987654321", "nip", "9999", "saldo": 10000.0}
]

for cuenta in cuentas:
    print(f"Tarjeta: {cuenta['tarjeta']} | NIP: {cuenta['nip']} Saldo: ${cuenta['saldo']:.2f")