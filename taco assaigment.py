def mostrar_menu():
    print("\nWelcome to Taco Palace! Please view the menu below and make a selection")
    print("Taco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


def obtener_precio(opcion):
    # Precios de ejemplo (puedes ajustarlos según necesites)
    if opcion == 1:
        return 3.50, "Taco"
    elif opcion == 2:
        return 5.00, "Burrito"
    elif opcion == 3:
        return 4.25, "Nachos"
    elif opcion == 4:
        return 2.50, "Drink"
    return 0.0, ""


def main():
    ordenados = []
    total = 0.0

    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

    while True:
        mostrar_menu()
        try:
            opcion = int(input("User entered: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if opcion == 5:
            break
        elif 1 <= opcion <= 4:
            precio, nombre = obtener_precio(opcion)
            total += precio
            ordenados.append(nombre)
            print(f"You selected a {nombre}")
        else:
            print("Opción inválida, por favor selecciona un número entre 1 y 5.")

    # Formatear el resumen de la orden
    if len(ordenados) == 0:
        print("\nNo order was placed.")
    elif len(ordenados) == 1:
        print(f"\nYou ordered a {ordenados[0]}. Your total is ${total:.2f}")
    else:
        # Construye la frase con "and" para el último elemento según el ejemplo
        items_str = ", ".join(ordenados[:-1]) + " and a " + ordenados[-1]
        print(f"\nYou ordered a {items_str}. Your total is ${total:.2f}")


if __name__ == "__main__":
    main()