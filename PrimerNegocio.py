menu = ["Cafes", "Sandwiches", "Pasteles", "Salir"]
cafes = [
    ["Americano", 1.00],
    ["Capuccino", 1.75],
    ["Mocaccino", 2.00]
]
sandwiches = [
    ["Sandwich de queso", 0.50],
    ["Sandwich de pernil", 1.50],
    ["Sandwich completo", 2.00]
]
pasteles = [
    ["Pastel de chocolate", 1.50],
    ["Pastel de naranja", 1.00],
    ["Pastel de platano", 1.00]
]
def info_clientes():
    print("="*40)
    print("             DATOS CLIENTE            ")
    nombre = str(input("Por favor ingrese su nombre y apellido: "))
    cedula = int(input("Por favor ingrese su numero de cedula: "))
    direccion = str(input("Por favor ingrese su direccion: "))
    return nombre, cedula, direccion
def comprobante(nombre, cedula, direccion, producto, precio, cantidad, subtotal, iva, total):
    print("="*40)
    print("             COMPROBANTE            ")
    print("="*40)
    print("Cliente:", nombre)
    print("Cédula:", cedula)
    print("Dirección:", direccion)
    print("-"*40)
    print("Producto:", producto)
    print("Precio:", precio)
    print("Cantidad:", cantidad)
    print("Subtotal:", subtotal)
    print("IVA (15%):", iva)
    print("TOTAL:", total)
def pedido(lista, nombre):
    numero = 1
    for producto in lista:
        print(numero, ".", producto[0], producto[1])
        numero += 1
    print("0. Regresar")
    opcion = int(input("Por favor seleccione un producto: "))
    if opcion == 0:
        print("Regresando al menú")
    elif opcion >= 1 and opcion <= 3:
        producto = lista[opcion - 1][0]
        precio = lista[opcion - 1][1]
        cantidad = int(input("Por favor ingrese la cantidad: "))
        if cantidad > 0:
            subtotal = cantidad * precio
            iva = subtotal * 0.15
            total = subtotal + iva
            respuesta = input("¿Por favor indique si desea un comprobante? (s/n): ")
            if respuesta == "s":
                nombre, cedula, direccion = info_clientes()
                comprobante(nombre, cedula, direccion, producto, precio, cantidad, subtotal, iva, total)
            else:
                print("Su total es:", total)
        else:
            print("Cantidad incorrecta.")
    else:
        print("Opción incorrecta.")
while True:
    print("="*40)
    print("             DULCE CAFE             ")
    print("="*40)   
    print("            BIENVENIDO/A            ")
    print("-"*40)
    print("                MENU               ")
    numero = 1
    for opcion_menu in menu:
        print(numero, ".", opcion_menu)
        numero += 1
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        pedido(cafes, "Cafés")
    elif opcion == "2":
        pedido(sandwiches, "Sandwiches")
    elif opcion == "3":
        pedido(pasteles, "Pasteles")
    elif opcion == "4":
        print("Gracias por visitar DULCE CAFE")
        break
    else:
        print("Opción incorrecta")
        
