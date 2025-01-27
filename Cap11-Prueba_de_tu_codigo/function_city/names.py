from city_functions import formatted_country

print("Ingresa 'q' en cualquier momento para salir.")
while True:
    ciudad = input("\nDame el nombre de una ciudad: ")
    if ciudad == 'q':
        break
    pais = input("Dame el nombre de una pais: ")
    if pais == 'q':
        break
    poblacion = int(input('¿Cuales la poblaciòn de tu regiòn?: '))
    if poblacion == 'q':
        break

    formatted_name = formatted_country(ciudad, pais, poblacion)
    print(f"\tNombre con formato adecuado: {formatted_name}.")