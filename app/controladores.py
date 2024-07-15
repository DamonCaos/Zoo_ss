from app.vistas import VistaEntrada, VistaGrupo
from app.modelos import Grupo_Entrada
from simple_screen import DIMENSIONS, cls, locate, Input, Screen_manager

class Zoo:
    def __init__(self):
        self.grupo_entradas = Grupo_Entrada()
        self.x = (DIMENSIONS.w -37) // 2
        self.vista_grupo = VistaGrupo(self.grupo_entradas, self.x, 1)
        self.entrada_edad = VistaEntrada("EDAD: ", self.x, 10)
        self.entrada_seguir = VistaEntrada("Otra vez? (S/N)", self.x, 12)

    def run(self):
        with Screen_manager:
            while True:
                cls()
                self.vista_grupo.paint()
                edad = self.entrada_edad.paint()
                if edad == "":
                    respuesta = self.entrada_seguir.paint()
                    if respuesta == "S":
                        grupo_entradas = Grupo_Entrada()
                        self.vista_grupo.grupo = grupo_entradas
                        continue
                    else:
                        break
            
            

        edad = int(edad)
        self.vista_grupo.grupo.add_entrada(edad)

    
    
         
#final controlado de pantalla
locate(1, DIMENSIONS.h - 2)
Input("Pulse enter para salir")