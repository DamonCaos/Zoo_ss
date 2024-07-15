from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = 0
    NIÑO = 14
    ADULTO = 23
    JUBILADO = 18



class Entrada:
    def __init__(self, edad: int):
        #self.__validate_edad(edad)
        #self.__edad = edad
        if edad < 0:
            raise ValueError('La edad no puede ser negativa')
        if edad  <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = 0
        elif edad < 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = 14
        elif edad < 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else:
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18

class Grupo_Entrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {}
        for tipo in TipoEntrada:
            self.tipos_entrada[tipo] = {'Q': 0, 'P': tipo.value}
        """self.tipos_entrada = {
            TipoEntrada.BEBE: {'Q': 0, 'P': 0},
            TipoEntrada.NIÑO: {'Q': 0, 'P': 14},
            TipoEntrada.ADULTO: {'Q': 0, 'P': 23},
            TipoEntrada.JUBILADO: {'Q': 0, 'P': 18}

        }"""

    def add_entrada(self, edad):
        """
        En funcion de la edad. crear una entrada e incrementar el contador de entradas 
        con el precio de la entrada nueva incrementar el total
        """
        nueva_entrada = Entrada(edad)
        self.num_entradas += 1
        self.total += nueva_entrada.precio

        self.tipos_entrada[nueva_entrada.tipo]['Q'] += 1


    def cantidad_entradas_por_tipo(self, tipo: TipoEntrada):
        return self.tipos_entrada[tipo]['Q']

    def subtotal_tipo(self, tipo: TipoEntrada):
        return self.tipos_entrada[tipo]['Q'] * self.tipos_entrada[tipo]['P']
        