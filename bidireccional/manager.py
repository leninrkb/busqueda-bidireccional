from agente import Agente
import random


def obtenerUbicacion(objetivo:str, matriz:list[list[str]]):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == objetivo:
                return (i, j)
    return None

totalHijos = 0
def generarHijos(padre:Agente, cantidad:int): # funcion sucesor 
    global totalHijos
    hijos = []
    for i in range(cantidad):
        totalHijos += 1
        nuevoHijo = Agente(padre)
        nuevoHijo.numero = totalHijos
        hijos.append(nuevoHijo)
    return hijos

def ejecutarMovimientos(agentes:list[Agente], mezclarMovimientos:bool=True):
    metodos = ['movArriba','movAbajo','movIzquierda','movDerecha']
    if mezclarMovimientos: # mezclo el orden de los movimientos solo para no obtener simepre la misma ruta
        random.shuffle(metodos) # nada que ver con el algoritmo, de pronto te pregunta...
    posibles = [] 
    for index, agente in enumerate(agentes):
        if getattr(agente, metodos[index])():
            posibles.append(agente)
    return posibles

def dibujarMapaVacio(filas:int, columnas:int):
    mapa = [['_'] * columnas for _ in range(filas)]
    return mapa

def dibujarRutaSolucion(agente:Agente, mapa:list[list[str]]):    
    for punto in agente.caminoRecorrido:
        mapa[punto[0]][punto[1]] = '#'
    for fila in mapa:
        print(fila)   