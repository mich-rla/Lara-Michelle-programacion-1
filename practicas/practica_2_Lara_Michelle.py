#EJERCICO 1 ES PAR O IMPAR

numero=17
es_par = numero % 2 == 0
print(es_par)

#EJERCICIO 2 CONCATENAR VS SUMAR

num1="5"
num2="3"
print(num1 + num2)

num1=int(num1) 
num2=int(num2)
print(num1 + num2)

#EJERCICIO 3 MINI REPORTE DE UN PERFIL

nombre="Isis"
edad=22
estatura=1.52
es_estudiante=True
print(type(nombre))
print(type(edad))
print(type(estatura))
print(type(es_estudiante))

#EJERCICIO 3 OPERADORES ARITMETICOS BÁSICOS

num1=10
num2=2

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

#EJERCICO 4 DIVISION ENTERA Y MODULO

num1=10
num2=2

print(num1//num2)
print(num1%num2)
#si usamos / nos da decimales y si usamos // no nos da decimales

#EJERCICIO 5 OPERADORES RELACIONALES

num3= 6
num4= 3

res1=num3<num4
res2=num3>num4
res3=num3==num4
res4=num3!=num4

print(res1)
print(res2)
print(res3)
print(res4)

#EJERCICIO 6 OPERADORES LOGICOS 

BOL1 = 3<6
BOL2 = 4<3

print( BOL1 and BOL2)
print( BOL1 or BOL2)
print (not BOL2)

#EJERCICIO 7 PROMEDIO Y APROBACION

cal1= 10 
cal2=5
cal3=7

promedio=( cal1+cal2+cal3)/3
aprobado = promedio>= 6

print(promedio)
print (aprobado)

#EJERCICIO 8 VALIDACION DE ELEGIBILIDAD

edad= 18
nacionalidad= "mexicana"

es_elegible= edad>=18 and nacionalidad=="mexicana"
print(es_elegible)

edad= 6
nacionalidad= "mexicana"


es_elegible= edad>=18 and nacionalidad=="mexicana"
print(es_elegible)

edad= 18
nacionalidad= "americano"


es_elegible= edad>=18 and nacionalidad=="mexicana"
print(es_elegible)