#Alexa Michelle Rodriguez Lara 
#219428753
#Construir un programa de consola que registre varios productos de una compra, valide los datos capturados y muestre un recibo final claramente formateado.

#Recibir y validar datos 
#Para evitar que las personas pongan datos que no pedimos, quise que apareciera en pantalla un mensaje de error

while True:
    numero_productos = input("¿Cuántos productos quieres registrar? ")

    if numero_productos.isdigit() and int(numero_productos) > 0:
        numero_productos = int(numero_productos)
        break
    else:
        print("Error: ingresa un número entero mayor que cero.")

productos = []
subtotal_general = 0

# Pedir cada producto y validar cada dato

for i in range(numero_productos):
    print(f"\nProducto {i + 1}")

    nombre_producto = input("Nombre del producto: ")

    # Valida el precio del producto
    while True:
        precio_texto = input("Precio del producto: $")

        try:
            precio_producto = float(precio_texto)

            if precio_producto >= 0:
                break
            else:
                print("Error: el precio no puede ser negativo.")
        except ValueError:
            print("Error: ingresa un precio válido.")

    # Valida la cantidad 

    while True:
        cantidad_texto = input("Cantidad: ")

        if cantidad_texto.isdigit() and int(cantidad_texto) > 0:
            cantidad_producto = int(cantidad_texto)
            break
        else:
            print("Error: ingresa una cantidad entera mayor que cero.")


# Valida los productos 

    subtotal_producto = precio_producto * cantidad_producto
    subtotal_general += subtotal_producto

    productos.append({
        "nombre": nombre_producto,
        "precio": precio_producto,
        "cantidad": cantidad_producto,
        "subtotal": subtotal_producto
    })

# IVA

iva = subtotal_general * 0.16
total_pagar = subtotal_general + iva

# Imprimir el recibo de compra

print("\n========================================")
print("             TICKET")
print("========================================")

for producto in productos:
    print(f"\nProducto: {producto['nombre']}")
    print(f"Precio: ${producto['precio']:.2f}")
    print(f"Cantidad: {producto['cantidad']}")
    print(f"Subtotal: ${producto['subtotal']:.2f}")

print("\n----------------------------------------")
print(f"Subtotal general: ${subtotal_general:.2f}")
print(f"IVA (16%):        ${iva:.2f}")
print("----------------------------------------")
print(f"TOTAL A PAGAR:    ${total_pagar:.2f}")
print("========================================")
print("        ¡Gracias por tu compra, tqm! ")