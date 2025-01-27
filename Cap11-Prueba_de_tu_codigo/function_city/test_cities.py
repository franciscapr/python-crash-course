from city_functions import formatted_country

def test_formatted_country():
    """¿Funcionan los nombres formateados?"""
    formatted = formatted_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'


