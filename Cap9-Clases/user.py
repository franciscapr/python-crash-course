
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

class Privileges:
    """Clase para manejar los privilegios de una usuario."""

    def __inint__(self, privileges=None):
        """Inicializa los privilegios con una lista opcional."""
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        """Muestra los privilegios asignados."""
        print("Privilegios:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege.title()}")
            else:
                print("- No hay privilegios asignados.")

# Clase Admin que hereda de User
class Admin(User):
    """Representa un administrador, un tipo especial de usuario."""

    def __init__(self, first_name, last_name, age, gender):
        """Inicializa los atributos del usuario y crea un instancia de Privileges"""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()

