# funciòn con dos parametros

#def get_formatted_name(first, last):
 #   """Genera un nombre completo con formato adecuado."""
 #   full_name = f'{first} {last}'
 #   return full_name.title()

# funciòn con error

#def get_formatted_name(first, middle, last):
#    """Genera un nombre completo formateado de manera ordenada."""
#    full_name = f"{first} {middle} {last}"
#    return full_name.title()

# funciòn con tres parametros, middle es opcional

def get_formatted_name(first, last, middle=''):
    """Genera un nombre completo formateado de manera ordenada."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()