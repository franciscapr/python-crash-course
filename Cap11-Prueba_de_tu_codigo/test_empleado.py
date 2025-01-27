from empleado import Empleado
import pytest

def test_dar_aumento_predeterminado():
    empleado = Empleado('Juan', 'Perez', 30000)
    empleado.dar_aumento()
    assert empleado.salario == 35000

def test_dar_aumento_personalizado():
    empleado = Empleado("Ana", "Lopez", 30000)
    empleado.dar_aumento(7000)
    assert empleado.salario == 37000

@pytest.fixture
def empleado():
    return Empleado("Carlos", "Gomez", 40000)

def test_dar_aumento_predeterminado_con_fixture(empleado):
    empleado.dar_aumento()
    assert empleado.salario == 45000

def test_dar_aumento_personalizado_con_fixture(empleado):
    empleado.dar_aumento(6000)
    assert empleado.salario == 46000