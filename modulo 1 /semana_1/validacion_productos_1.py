#Sistema de validación de productos

nombre_producto = str(input("Escribe el nombre del producto: ")) # Pedimos al usuario el nombre del producto

#Se verifica que el nombre solo tenga letras con un isalpha 
if not nombre_producto.replace(" ", "").isalpha():
    print("El nombre del producto solo debe contener letras y espacios.")
    exit("vuelva a intentarlo") #si los datos son incorrectos le pedimos al usuario volver a intentarlo

#hacemos un ciclo para que el usuario pueda poner las datos de nuevo desde este punto si se equivoca
while True:
    try:
        # Pedimos el precio, la cantidad y el porcentaje de descuento.
        # Usamos float para precios (pueden tener decimales) y int para cantidades.
        precio_unitario = float(input("Escribe el precio unitario: "))
        cantidad_producto = int(input("Escribe la cantidad que desea: "))
        cantidad_porcentaje = int(input("Escribe el porcentaje de descuento (0 a 100): "))
    except ValueError: #se evalua si esta correctos los enunciados (que corresponda al tipo de variable)
        print("Por favor, ingresa datos válidos: no se debe poner texto, solo numeros.") #si los datos no son validos se vuelve preguntar al usuario

    if precio_unitario < 0 or cantidad_producto < 0 or cantidad_porcentaje < 0 or cantidad_porcentaje > 100: #procedemos a verificar que los datos sean correctos teniendo en cuenta los porcentajes y no tengan numeros negativos
        print("\n")
        print("=" * 35)
        print("        ¡Error en los datos!")
        print("=" * 35)
        print("- El precio no puede ser negativo.")
        print("- La cantidad no puede ser negativa.")
        print("- El porcentaje debe estar entre 0% y 100%.")
        print("________vuelve a intentarlo________")
        print("\n\n") #vuelve al ciclo para preguntar de nuevo los datos al estar mal
    else:
        cantidad_total = precio_unitario * cantidad_producto  # Calculamos el total sin descuento
        total_con_descuento = cantidad_total - (cantidad_total * cantidad_porcentaje / 100) # Calculamos el total con el descuento aplicado

        #cuando tenemos todos los datos pocedemos a imprimirlos

        print("\n") #salto de linea
        print("=" * 35)
        print("            RESULTADOS")
        print("=" * 35)
        print(f"Producto: {nombre_producto}")
        print(f"Precio unitario: ${precio_unitario:.2f}")
        print(f"Cantidad: {cantidad_producto}")
        print(f"Total sin descuento: ${cantidad_total:.2f}")
        print(f"Descuento aplicado: {cantidad_porcentaje}%")
        print(f"Total con descuento: ${total_con_descuento:.2f}")
        print("=" * 35)
        break #este break es para que el ciclo termine si va todo bien

# Fin del programa
