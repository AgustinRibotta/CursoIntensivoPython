""" Pruebas pag 49  """

name = 'Roberto'

print(f'Hola {name}, como estas ?')
print(f'Hola {name.lower()}, como estas ?')
print(f'Hola {name.upper()}, como estas ?')
print(f'Hola {name.title()}, como estas ?')


famous_person = "Yo"
mensage = "Este es el mensaje que"
mensage2 = "escribi"

print(f'{mensage} {famous_person} {mensage2}')

name_space = " Agustin "

print(name_space.lstrip())  # Izquierda
print(name_space.rstrip())  # Derecha
print(name_space.strip())   # Los dos

filname = "./python_note.txt"

print(filname.removesuffix(".txt")) # Remueve un parte del string


import this