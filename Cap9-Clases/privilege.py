from onlyuser import User

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


# Creamos una instancia de admin y mostramos sus privilegios
admin_user = Admin('Antonio', 'Mele', 29, 'Masculino')
admin_user.describe_user()

# Asignamos privilegios al asministrador y los mostramos
admin_user.privileges.privileges = ['puede agregar publicaciòn', 'puede eliminar publicaciòn', 'puede prohibir usuarios']
admin_user.privileges.show_privileges()
