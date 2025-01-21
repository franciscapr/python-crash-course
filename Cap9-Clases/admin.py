from user import User, Admin, Privileges


# Creamos una instancia de admin y mostramos sus privilegios
admin_user = Admin('Antonio', 'Mele', 29, 'Masculino')
admin_user.describe_user()

# Asignamos privilegios al asministrador y los mostramos
admin_user.privileges.privileges = ['puede agregar publicaciòn', 'puede eliminar publicaciòn', 'puede prohibir usuarios']
admin_user.privileges.show_privileges()