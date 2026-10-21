# if, es el rombo de si y no 
#if es una palabra reservada y else tambien

x = 12
if x > 0:
    print("x es positivo.") 

#sino, esto se usa para decir que sino pasa una cosa, pase la otra

x=2
y=5

if x > y:
    print("x es mayor que y")
else:
    print("x no es mayor que y")

#elif, es resrvada y es otra evaluación, ahora no solo es si, sino, agregamos otra

x=2
y=2

if x > y:
    print("x es mayor que y") 
elif x < y:
    print("y es mayor")
else:
    print("son igualitos")


 #así es en un caso real

cal= 12
if cal > 90:
    print("Sobresaliente")
elif cal > 70:
    print("Bien")
else:
    print("Dibujar no te gusta?")


temp = 30

if temp <10:
    print("frio")

elif temp <25:
    print("templado")
else:
    print("calor")  


cantidad=100

if cantidad >100:
    print("20% de descuento")
elif cantidad >50:
    print("10% de descuento")   
else:
    print("sin descuento")




cantidad=input("Ingresa la cantidad: ")
cantidad=int(cantidad)

if cantidad > 100:
    descuento = cantidad * .20
    total = cantidad - descuento
    print("20% de descuento:", descuento)
    print("Total a pagar:", total)

elif cantidad > 50:
    descuento = cantidad * .10
    total = cantidad - descuento
    print("10% de descuento:", descuento)
    print("Total a pagar:", total)

else:
    print("Sin descuento")