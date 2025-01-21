#Creamos una clase para User
class User:
    """Creamos una clase user con mètodos"""

    # Creamos el mètodo inicializados
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    # Creamos un mètodo para imprimir el resumen de la informaciòn del usuario.
    def describe_user(self):
        print(f"User: \nNombre: {self.first_name.title()} \nApellido: {self.last_name.title()} \nEdad: {self.age} \nGenero: {self.gender}")

    # Creamos otro mètodo
    def greet_use(self):
        print(f"\nBienvenido {self.first_name.title()} {self.last_name.title()}.!!!\n")
