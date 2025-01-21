# Creamos una clase
class Restaurant:
    """Creaciòn de una clase restaurante"""

    # Creamos el mètodo inicializador
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    # Creamos un mètodo para imprimir la informaciòn
    def describe_restaurant(self):
        print(f"El {self.restaurant_name.title()} tiene comida de tipo {self.cuisine_type}")

    # Creamos un mètodo que imprime un mensaje indicando que el restaurante està abierto.
    def open_restaurant(self):
        print(f"El restaurant {self.restaurant_name.title()} se encuentra abierto")


# Creamos una instancia a partir de la clase Restaurant
restaurant = Restaurant('millenium', 'peruana')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# Creamos una clase IceCreamStand que hereda de Restaurant
class IceCreamStand(Restaurant):
    """Represeta un puesto de helado, un tipo especìfico de restaurante"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Inicializa los atributos del restaurante y los especificos del puesto de helados"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        """Muestra los sabores de helados disponibles"""
        print(f"Sabores disponibles en {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

# Creamos una instancia de IceCreamStand
ice_cream_stand = IceCreamStand('Frozen Delight', 'Heladeria', ['vainilla', 'menta chip', 'chocolate', 'frutilla', 'menta', 'mango'])

# Llamamos a los mètodo
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.show_flavors()
    