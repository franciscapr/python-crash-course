class Empleado:

    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def dar_aumento(self, aumento=5000):
        self.salario += aumento