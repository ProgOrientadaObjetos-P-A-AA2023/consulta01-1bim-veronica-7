"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Mascota:
    humano = ''
    tipo = ''
    nombre = ''
    color = ''
    edad = 0

    def __init__(self, human, tip, nom, clr, edd):
        self.humano = human
        self.nombre = nom
        self.tipo = tip
        self.color = clr
        self.edad = edd


    def __str__(self):
        cadena = "Mi nombre es {} y tengo una mascota, su nombre es {} \nEs un{} de color {} y tiene {} años de edad".format(
            self.humano, self.nombre, self.tipo, self.color, self.edad)
        return cadena


# clase 02
class Bicicletas:
    tipo = ''
    color = ''
    tamanio = ''
    ruedas = 0

    def __init__(self, tip, clr, tam, rue):
        self.tipo = tip
        self.color = clr
        self.tamanio = tam
        self.ruedas = rue

    def __str__(self):
        cadena = "Tengo una bicicleta {}, es de color {}, es {} y tiene {} \nEs mi medio de transporte!".format(
            self.tipo, self.color, self.tamanio, self.ruedas)
        return cadena


