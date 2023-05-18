"""

"""
# Crear dos objetos de la clase 01
from mis_clases import Mascota

# objeto 01

# crear
mascota1 = Mascota('Juan', 'gato', 'copito', 'blanco', 2)

# Presentar objeto; usar el método __st__
print(str(mascota1))

# objeto 02

# crear ingresando valores por teclado
print("nombre del dueño:")
humano = input()
print("Ingrese el nombre de su mascota")
nombre = input()
print("Idique su tipo de mascota:")
tipo = input()
print("Indique el color de su mascota:")
color = input()
print("Indique la edad que tiene su mascota")
edad = int(input())

mascota2 = Mascota(humano, nombre, tipo, color, edad)

# Presentar objeto; usar el método __st__
print(str(mascota2))
