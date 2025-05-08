#Gestion de inventario de productos

#inventario inicial con un producto de ejemplo
inventory = { #diccionario con los productos, este diccionario es una estructura de datos mutable por lo que se puede modificar
    "leche": (1200, 10)#tupla con el precio y la cantidad, la tupla es una estructura de datos inmutable por lo que no se puede modificar pero se puede acceder a sus elementos
} #se debe modificar la tupla para cambiar el precio o la cantidad, se puede hacer creando una nueva tupla con los nuevos valores y asignandola a la clave del diccionario

#Funcion para mostrar el menu de opciones al usuario
def show_menu():
    print("\n--- Show the Invetory ---")
    print("1. Add product")
    print("2. Consult product")
    print("3. Update price")
    print("4. Delete product")
    print("5. Calculate total value")
    print("6. Exit")
    print("-------------------------")

#Funcion para validar que el usuario ingrese un numero entero valido
def validate_input_numbrer(message):
    while True:
        val = input(message)
        if val.isdigit(): #verifica si el valor es un numero entero con .isdigit() (True si es un numero) y devuelve con un return
            return int(val)
        else:
            print("Please enter a valid number.")

#Funcion para añadir un nuevo producto al inventario
def add_product():
    product = input("Product name: ").lower().strip() #.strip() elimina los espacios en blanco al inicio y al final de la cadena
    if product in inventory: #verifica si el producto ya existe en el inventario
        #si el producto ya existe, imprime un mensaje y no lo añade
        print("this product is already in the inventory.")
    else:
        price = validate_input_numbrer("product price: ")
        quantity = validate_input_numbrer("Available quantity: ")
        inventory[product] = (price, quantity)
        print(f"product {product} added successfully.")


#Funcion para consultar los datos de un producto existente
def consult_product():
    product = input("enter the oroduct name: ").lower().strip() #strip() elimina los espacios en blanco al inicio y al final de la cadena
    if product in inventory: #se verifica si el producto esta en el inventerio
        price, quantity = inventory[product] #se asigna el precio y la cantidad a las variables
        #se imprime el producto, precio y cantidad
        print(f"\nProduct: {product}")
        print(f"Price: {price}")
        print(f"Quantity: {quantity}")
    else:
        print("The product is not in the inventory.")

#Funcion para actualizar el precio de un producto
def update_price():
    product = input("name of the product to update: ").lower().strip() #strip() elimina los espacios en blanco al inicio y al final de la cadena
    if product in inventory:
        new_price = validate_input_numbrer("new price: ") #se valida el nuevo precio con la funcion validate_input_numbrer
        inventory[product] = (new_price, inventory[product][1]) #se actualiza el precio del producto con el nuevo precio y se mantiene la cantidad
        #se imprime el nuevo precio del producto
        print(f"Price of {product} updated to {new_price}.")
    else:
        print("The product is not in the inventory.") #si el producto no esta en el inventario, se imprime un mensaje
    
#Funcion para eliminar un producto del inventario
def delete_product():
    product = input("which product do yoy want to delete? ").lower().strip() #strip() elimina los espacios en blanco al inicio y al final de la cadena
    if product in inventory: #se verifica si el producto esta en el inventerio
        del inventory[product] #se elimina el producto del inventario
        print(f"Product {product} deleted successfully.")
    else:
        print("The product is not in the inventory.")

#Funcion para calcular el valor total del inventario
def calculate_total():
    total = 0
    for product in inventory: #se itera sobre el inventario
        price, quantity = inventory[product] #se asigna el precio y la cantidad a las variables
        total += price * quantity #se calcula el total
    print(f"Total value of the inventory: {total}")

#Funcion principal
while True:
    show_menu()
    opcion = validate_input_numbrer("Select an option: ")
    #se valida la opcion con la funcion validate_input_numbrer
    match opcion: #se utiliza el match case para validar la opcion
        case 1:
            add_product()
        case 2:
            consult_product()
        case 3:
            update_price()
        case 4:
            delete_product()
        case 5:
            calculate_total()
        case 6:
            print("Exiting the program.")
            break #salir del bucle
        case _:
            print("Invalid option. Please try again.")
