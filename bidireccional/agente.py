class Agente():
    def __init__(self, agente=None): # tomo al agente padre como parametro
        if agente == None:
            self.alto = 0 
            self.ancho = 0
            self.puntoInicial = (0,0) 
            self.puntoObjetivo = (0,0)
            self.puntoActual = (0,0)
            self.caminoRecorrido = []
            self.controlarRepetidos = True
            self.movimientoRealizado = 'inicio'
            self.numero = 0
        else:
            self.alto = agente.alto
            self.ancho = agente.ancho
            self.puntoInicial = agente.puntoInicial
            self.puntoObjetivo = agente.puntoObjetivo
            self.puntoActual = agente.puntoActual
            self.movimientoRealizado = agente.movimientoRealizado
            self.controlarRepetidos = agente.controlarRepetidos
            self.numero = agente.numero
            self.caminoRecorrido = []
            for camino in agente.caminoRecorrido: #herendo el camino del apdre
                self.caminoRecorrido.append(camino)
                
    def obtenerID(self):
        id = f'{self.movimientoRealizado}_{self.numero}'
        return id
        
    def inicio(self, matriz:list[list[str]], puntoInicial:tuple, puntoObjetivo:tuple):
        self.alto = len(matriz)
        self.ancho = len(matriz[0])
        self.puntoInicial = puntoInicial
        self.puntoObjetivo = puntoObjetivo
        self.puntoActual = self.puntoInicial
        self.caminoRecorrido.append(self.puntoActual)
    
    def evaluarMovimiento(self, mov:str): #agrego esto para poder activar/desactivar el control de repetidos
        if self.controlarRepetidos:
            if self.puntoActual in self.caminoRecorrido:
                return False
            else:
                self.caminoRecorrido.append(self.puntoActual)
                self.movimientoRealizado = mov
                return True
        else:
            self.caminoRecorrido.append(self.puntoActual)
            self.movimientoRealizado = mov
            return True
            
    def movArriba(self)->bool:
        if not self.puntoActual[0] - 1 < 0:
            self.puntoActual = (self.puntoActual[0] - 1, self.puntoActual[1])
            return self.evaluarMovimiento('arriba')
        return False

    def movAbajo(self)->bool:
        if not self.puntoActual[0] + 1 > self.alto - 1:
            self.puntoActual = (self.puntoActual[0] + 1, self.puntoActual[1])
            return self.evaluarMovimiento('abajo')
        return False

    def movIzquierda(self)->bool:
        if not self.puntoActual[1] - 1 < 0:
            self.puntoActual = (self.puntoActual[0], self.puntoActual[1] - 1)
            return self.evaluarMovimiento('izquierda')
        return False
    
    def movDerecha(self)->bool:
        if not self.puntoActual[1] + 1 > self.ancho - 1:
            self.puntoActual = (self.puntoActual[0], self.puntoActual[1] + 1)
            return self.evaluarMovimiento('derecha')
        return False
    
    def esObjetivo(self):
        if self.puntoActual == self.puntoObjetivo:
            self.movimientoRealizado = 'solucion'
            return True
        return False
    
    def mostrarcaminoRecorrido(self):
        print(self.caminoRecorrido)