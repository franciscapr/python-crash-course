from name_function import get_formatted_name


def test_first_last_name():
    """¿Funcionan nombres como 'Janis Joplin?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """¿Funcionan los nombres como 'Wolfgang Amadeus Mozart?"""
    formatted_name = get_formatted_name('Wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'