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
def info_clientes(nombre = "", cedula=0, direccion = ""):
    print("="*40)
    print("             DATOS CLIENTE            ")
    nombre = str(input("Por favor ingrese su nombre y apellido: "))
    cedula = int(input("Por favor ingrese su numero de cedula: "))
    direccion = str(input("Por favor ingrese su direccion: "))
    return nombre, cedula, direccion
def comprobante(*compra, **cliente):
    print("="*40)
    print("             COMPROBANTE            ")
    print("="*40)
    print("Cliente:", cliente["nombre"])
    print("Cédula:", cliente["cedula"])
    print("Dirección:", cliente["direccion"])
    print("-"*40)
    print("Producto:", compra[0])
    print("Precio:", compra[1])
    print("Cantidad:", compra[2])
    print("Subtotal:", compra[3])
    print("IVA (15%):", compra[4])
    print("TOTAL:", compra[5])
def pedido(lista, producto = "Producto"):
    print(producto)
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
            respuesta = input("¿Por favor indique si desea un comprobante? (s/n): ").lower()
            if respuesta == "s":
                nombre, cedula, direccion = info_clientes()
                comprobante(producto, precio, cantidad, subtotal, iva, total, nombre = nombre, cedula = cedula, direccion = direccion)
                return True
            else:
                print("Su total es:", total)
                return True
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
    opcion = input("Por favor seleccione una opción: ")
    if opcion == "1":
        pedido(cafes, "     Cafés       ")
    elif opcion == "2":
        pedido(sandwiches, "       Sandwiches     ")
    elif opcion == "3":
        pedido(pasteles, "     Pasteles    ")
    elif opcion == "4":
        print("Gracias por visitar DULCE CAFE")
        break
    else:
        print("Opción incorrecta")
        
