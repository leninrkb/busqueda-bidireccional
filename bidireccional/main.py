from queue import Queue
from agente import Agente
import manager as mn
from graphviz import Digraph

mapa = [
    ['', 'uta', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', 'mall', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
]


# defino para el primer arbol
a1_puntoInicial = mn.obtenerUbicacion('uta', mapa)
a1_puntoObjetivo = mn.obtenerUbicacion('mall', mapa)

raiz_uta = Agente()
raiz_uta.inicio(mapa, a1_puntoInicial, a1_puntoObjetivo)
raiz_uta.controlarRepetidos = True

a1_grafo = Digraph()
a1_cola = Queue()
a1_cola.put(raiz_uta)

a1_solucion:Agente = None

# defino para el segundo
a2_puntoInicial = mn.obtenerUbicacion('mall', mapa)
a2_puntoObjetivo = mn.obtenerUbicacion('uta', mapa)

raiz_mall = Agente()
raiz_mall.inicio(mapa, a2_puntoInicial, a2_puntoObjetivo)
raiz_mall.controlarRepetidos = True

a2_grafo = Digraph()
a2_cola = Queue()
a2_cola.put(raiz_mall)

a2_solucion:Agente = None

print('buscando solucion ...')

while True:
    a1_estadoActual:Agente = a1_cola.get()
    a2_estadoActual:Agente = a2_cola.get()
    
    a1_grafo.node(a1_estadoActual.obtenerID(), a1_estadoActual.obtenerID())
    a2_grafo.node(a2_estadoActual.obtenerID(), a2_estadoActual.obtenerID())
    
    if a1_estadoActual.puntoActual == a2_estadoActual.puntoActual:
        print('encontrado...')
        print(a1_estadoActual.puntoActual)
        print(a2_estadoActual.puntoActual)
        a1_solucion = a1_estadoActual
        a1_grafo.node(a1_estadoActual.obtenerID(), a1_estadoActual.obtenerID())
        a2_solucion = a2_estadoActual
        a2_grafo.node(a2_estadoActual.obtenerID(), a2_estadoActual.obtenerID())
        break
        
    if a1_estadoActual.esObjetivo(): 
        a1_solucion = a1_estadoActual
        a1_grafo.node(a1_estadoActual.obtenerID(), a1_estadoActual.obtenerID())
        break
    if a2_estadoActual.esObjetivo(): 
        a2_solucion = a2_estadoActual
        a2_grafo.node(a2_estadoActual.obtenerID(), a2_estadoActual.obtenerID())
        break
    
    a1_nuevosEstados = mn.ejecutarMovimientos(mn.generarHijos(a1_estadoActual, 4), True)
    a2_nuevosEstados = mn.ejecutarMovimientos(mn.generarHijos(a2_estadoActual, 4), True)
    
    for nuevo in a1_nuevosEstados:
        a1_grafo.node(nuevo.obtenerID(), nuevo.obtenerID())
        a1_grafo.edge(a1_estadoActual.obtenerID(), nuevo.obtenerID())
        a1_cola.put(nuevo)
    for nuevo in a2_nuevosEstados:
        a2_grafo.node(nuevo.obtenerID(), nuevo.obtenerID())
        a2_grafo.edge(a2_estadoActual.obtenerID(), nuevo.obtenerID())
        a2_cola.put(nuevo)

if not a1_solucion == None:    
    mapaVacio = mn.dibujarMapaVacio(len(mapa), len(mapa[0]))
    mn.dibujarRutaSolucion(a1_solucion, mapaVacio)
    a1_solucion.mostrarcaminoRecorrido()
    a1_grafo.render("arbol1", view=True)

if not a2_solucion == None: 
    mapaVacio = mn.dibujarMapaVacio(len(mapa), len(mapa[0]))
    mn.dibujarRutaSolucion(a2_solucion, mapaVacio)
    a2_solucion.mostrarcaminoRecorrido()
    a2_grafo.render("arbol2", view=True)
