"""
               1         2         3        
      1234567890123456789012345678901234567
01    TIPO             PU     Q       TOTAL
02    =====================================
03    BEBE (≤2)      0.00    99     9999.99
04    NINO (≤12)    14.00    99     9999.99
05    ADULTO (<65)  23.00    99     9999.99
06    JUBILADO      18.00    99     9999.99
07    -------------------------------------
08                          999    99999.99
09                          
10    EDAD: 
11    CONF
"""
from app.modelos import Grupo_Entrada, TipoEntrada
from simple_screen import locate, Print, cls, Screen_manager, Input

class VistaGrupo:

    def __init__(self, grupo: Grupo_Entrada, x: int, y: int):
        self.grupo = grupo
        self.x = x
        self.y = y

    def paint(self):
        locate(self.x, self.y, 'TIPO             PU     Q       TOTAL')
        locate(self.x, self.y + 1, '=====================================')

        for indice, tipo in enumerate(TipoEntrada):
            locate(self.x, self.y + 3 + indice, 
                   f'{tipo.name:.<14s}{self.grupo.tipos_entrada[tipo]["P"]:5.2f}    '
                   f'{self.grupo.cantidad_entradas_por_tipo(tipo):2d}    {self.grupo.subtotal_tipo(tipo):7.2f}')

        locate(self.x, self.y + 7, '-------------------------------------')
        locate(self.x, self.y + 8, f'                     {self.grupo.num_entradas:3d}    {self.grupo.total:8.2f}')

class VistaEntrada:
    def __init__(self, etiqueta: str, x, y):
        self.etiqueta = etiqueta    
        self.y = y
        self.x = x
    

    def paint(self):
        locate(self.x, self.y, self.etiqueta)
        return Input()
    
print(__name__)
if __name__ == "__main__":
    with Screen_manager():
        grupo = Grupo_Entrada()
        grupo.add_entrada(2)
        vg = VistaGrupo(grupo, 1, 5)  # Definir x y y aquí
        vg.paint()
        vedad = VistaEntrada('EDAD: ', 1, 10)
        vedad.paint
        Input()