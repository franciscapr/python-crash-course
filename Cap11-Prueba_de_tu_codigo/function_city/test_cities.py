from city_functions import formatted_country

def test_formatted_country():
    """¿Funcionan los nombres formateados?"""
    formatted = formatted_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile - '


def test_city_country():
    """¿Funcionan los nombres formateados?"""
    formatted = formatted_country('santiago', 'chile', 20000000)
    assert formatted == 'Santiago, Chile - 20000000'