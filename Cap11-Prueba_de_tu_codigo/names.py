from name_function import get_formatted_name

print("Ingresa 'q' en cualquier momento para salir.")
while True:
    first = input("\nPor favor, dame un nombre: ")
    if first == 'q':
        break
    last = input("Por favor, dame un apellido: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNombre con formto adecuado: {formatted_name}.")