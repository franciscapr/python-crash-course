from city_functions import formatted_country

print("Ingresa 'q' en cualquier momento para salir.")
while True:
    ciudad = input("\nDame el nombre de una ciudad: ")
    if ciudad == 'q':
        break
    pais = input("Dame el nombre de una pais: ")
    if pais == 'q':
        break

    formatted_name = formatted_country(ciudad, pais)
    print(f"\tNombre con formato adecuado: {formatted_name}.")