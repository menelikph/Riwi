# Inventario inicial con un producto de ejemplo
inventario = {}

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total")
    print("6. Salir")

# Función para validar que el usuario ingrese un número entero válido
def validar_entrada_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("Por favor ingrese un número válido.")

# Función para añadir un nuevo producto al inventario
def agregar_producto():
    nombre = input("Nombre del producto: ").strip()

    if nombre in inventario:
        print("Este producto ya está en el inventario.")
        return

    precio = validar_entrada_numero("Precio del producto: ")
    cantidad = validar_entrada_numero("Cantidad disponible: ")

    inventario[nombre] = {"precio": precio, "cantidad": cantidad}
    print(f"Producto '{nombre}' añadido con éxito.")

# Función para consultar los datos de un producto existente
def consultar_producto():
    nombre = input("Ingresa el nombre del producto: ").strip()

    if nombre in inventario:
        precio = inventario[nombre]["precio"]
        cantidad = inventario[nombre]["cantidad"]
        print(f"\nProducto: {nombre}")
        print(f"Precio: {precio}")
        print(f"Cantidad: {cantidad}")
    else:
        print("El producto no está en el inventario.")

# Función para actualizar el precio de un producto
def actualizar_precio():
    nombre = input("Nombre del producto a actualizar: ").strip()

    if nombre not in inventario:
        print("El producto no está en el inventario.")
        return

    nuevo_precio = validar_entrada_numero("Nuevo precio: ")
    inventario[nombre]["precio"] = nuevo_precio
    print(f"Precio de '{nombre}' actualizado a {nuevo_precio}.")

# Función para eliminar un producto del inventario
def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ").strip()

    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print("El producto no se encuentra en el inventario.")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    total = 0
    for producto in inventario:
        precio = inventario[producto]["precio"]
        cantidad = inventario[producto]["cantidad"]
        total += precio * cantidad

    print(f"El valor total del inventario es: {total}")

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = validar_entrada_numero("Selecciona una opción: ")

    match opcion:
        case 1:
            agregar_producto()
        case 2:
            consultar_producto()
        case 3:
            actualizar_precio()
        case 4:
            eliminar_producto()
        case 5:
            calcular_valor_total()
        case 6:
            print("Saliendo del programa. ¡Vuelva pronto!")
            break
        case _:
            print("Opción no válida, intente nuevamente.")