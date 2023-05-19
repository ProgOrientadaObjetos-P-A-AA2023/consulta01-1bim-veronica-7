"""

"""
# Crear dos objetos de la clase 02
from mis_clases import Bicicletas

# objeto 01

# crear
bicicleta1 = Bicicletas('BMX', 'rojo', 'pequeña', 2)

# Presentar objeto; usar el método __st__
print(bicicleta1.__str__())

# objeto 02

# crear ingresando valores por teclado
print("Tipo de Bicicleta:")
tipo = input()
print("Idique el color de la bicicleta")
color = input()
print("Tamaño de la bicicleta:")
tamanio = input()
print("Cuántas ruedas tiene su bicicleta?")
ruedas = int(input())

bicicleta2 = Bicicletas(tipo, color, tamanio, ruedas)

# Presentar objeto; usar el método __st__
print(bicicleta2.__str__())