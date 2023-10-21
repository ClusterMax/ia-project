import Modelo.Arbol as A
import math 

# Inicio del personaje en la casilla [2,7]
#El orden de las operaciones es arriba, derecha, abajo, izquierda
#La meta se encuentra en [2,0]
#para ir hacia arriba se debe de reducir el conteo de filas
#para ir hacia la derecha se debe de aumentar el numero de columnas
#para ir hacia abajo se debe de aumentar el numero de fila
#para ir hacia la izquierda se debe de reducir el numero de columnas

class AlgoritmoCURecursivo:
    
    def __init__(self, tablero, puntoInicial =[2,7], puntoFinal = [2,0]):
          
        self.tablero = tablero
        self.puntoInicial = puntoInicial
        self.PuntoFinal = puntoFinal
          


    def expandirNodos(self, nodoActual=None, nodosExtendidosGlobal=[]):

            nodosExtendidosPorNodo = [] #lista para evaluar si sigue en la misma rama o si cambia y se debe de comprimir
            posicion = nodoActual.get_coordenadas()
            

            ##Expandimos el nodo de arriba
            ##Si esta en los limites de arriba
            if posicion[0] != 0:#como el siguiente nodo  esta en el limite del tablero
                # no lo podemos crear, por ende tenemos que añadirlo a la lista y decir que tiene un valor de infinito positivo
                print("calcula el de arriba")
                posicionSiguiente = [posicion[0]-1, posicion[1]]

                if nodoActual.get_padre() is None or nodoActual.get_padre().get_coordenadas() != posicionSiguiente:

                    valorReal = self.tablero[posicionSiguiente[0]][posicionSiguiente[1]]
                    if valorReal != 0: #quiere decir que en esa casilla hay un muro, por ende no puede ir hacia allá
                        ValorAcumulado = nodoActual.get_ValorAcumulado() + valorReal
                        nodoArriba = A.Arbol(padre=nodoActual,coordenadas=posicionSiguiente, valorReal=valorReal, ValorAcumulado=ValorAcumulado, valorHijoMenorAcumulado=0)

                        #guardamos en la lista de nodos extendidos, en la extendidos global y añadimos al hijo izquierdo del arbol principal
                        
                        nodoActual.set_hijoUp(nodoArriba)
                        nodosExtendidosPorNodo.append(nodoActual.get_hijoUp())
                        nodosExtendidosGlobal.append(nodoActual.get_hijoUp())
            
            #si esta en los limites de la derecha

        
            if posicion[1] != 7: #se encuenta en el limite de la derecha
                
                print("calcula el de ¿derecha")
                posicionSiguiente = [posicion[0], posicion[1]+1]
                if nodoActual.get_padre() is None or nodoActual.get_padre().get_coordenadas() != posicionSiguiente:
                    valorReal = self.tablero[posicionSiguiente[0]][posicionSiguiente[1]]
                    if valorReal != 0: #quiere decir que en esa casilla hay un muro, por ende no puede ir hacia allá

                        ValorAcumulado = nodoActual.get_ValorAcumulado() + valorReal
                        nodoDerecha = A.Arbol(padre=nodoActual,coordenadas=posicionSiguiente, valorReal=valorReal, ValorAcumulado=ValorAcumulado, valorHijoMenorAcumulado=0)

                        #añadimos al hijo derecho del arbol principal, luego añadimos el hijo que se añadio, para tener una instancia de ese mismo objeto
                        
                        nodoActual.set_hijoRight(nodoDerecha)
                        nodosExtendidosPorNodo.append(nodoActual.get_hijoRight())
                        nodosExtendidosGlobal.append(nodoActual.get_hijoRight())
            
            if posicion[0] != 4: #se encuenta en el limite de abajo
                
                    print("calcula el de abajo")
                    posicionSiguiente = [posicion[0]+1, posicion[1]]
                    if nodoActual.get_padre() is None or nodoActual.get_padre().get_coordenadas() != posicionSiguiente:
                        valorReal = self.tablero[posicionSiguiente[0]][posicionSiguiente[1]]
                        if valorReal != 0: #quiere decir que en esa casilla hay un muro, por ende no puede ir hacia allá

                            ValorAcumulado = nodoActual.get_ValorAcumulado() + valorReal
                            nodoAbajo = A.Arbol(padre=nodoActual,coordenadas=posicionSiguiente, valorReal=valorReal, ValorAcumulado=ValorAcumulado, valorHijoMenorAcumulado=0)

                            #guardamos en la lista de nodos extendidos, en la extendidos global y añadimos al hijo izquierdo del arbol principal
                            
                            nodoActual.set_hijoBottom(nodoAbajo)
                            nodosExtendidosPorNodo.append(nodoActual.get_hijoBottom())
                            nodosExtendidosGlobal.append(nodoActual.get_hijoBottom())
            
            if posicion[1] != 0: #se encuenta en el limite de la izquierda

                    print("calcula el de izquierda")
                    posicionSiguiente = [posicion[0], posicion[1]-1]
                    if nodoActual.get_padre() is None or nodoActual.get_padre().get_coordenadas() != posicionSiguiente:
                        valorReal = self.tablero[posicionSiguiente[0]][posicionSiguiente[1]]
                        if valorReal != 0: #quiere decir que en esa casilla hay un muro, por ende no puede ir hacia allá

                            ValorAcumulado = nodoActual.get_ValorAcumulado() + valorReal
                            nodoIzquierda = A.Arbol(padre=nodoActual,coordenadas=posicionSiguiente, valorReal=valorReal, ValorAcumulado=ValorAcumulado, valorHijoMenorAcumulado=0)

                            #guardamos en la lista de nodos extendidos, en la extendidos global y añadimos al hijo izquierdo del arbol principal
                            
                            nodoActual.set_hijoLeft(nodoIzquierda)
                            nodosExtendidosPorNodo.append(nodoActual.get_hijoLeft())
                            nodosExtendidosGlobal.append(nodoActual.get_hijoLeft())
            
        #  nodoElejido = min(nodosExtendidosPorNodo)

        # nodosExtendidosGlobal.remove(nodoElejido)

            return nodoActual, nodosExtendidosPorNodo



    def costoUniformeRecursivo(self):
        
        nodosExtendidosGlobal = []
        contadorComprimidos =0
        contadorReExpancion = 0
        #nodosComprimidos = []
    
        #arbolPrincipal = A.Arbol(coordenadas=[2,7], valorReal=0, ValorAcumulado=0, valorHijoMenorAcumulado=0)
        nodoActual = A.Arbol(coordenadas=self.puntoInicial, valorReal=0, ValorAcumulado=0, valorHijoMenorAcumulado=0)
        nodoMeta = A.Arbol(coordenadas=self.PuntoFinal, valorReal=1)

        while nodoActual.get_coordenadas() != nodoMeta.get_coordenadas():
        #for i in range(20):

            if nodoActual.get_valorHijoMenorAcumulado() == 0:
                print("nodo actual en el que estamos".center(50,"-"))
                print(nodoActual)
                nodoActual,nodosExtendidosPorNodo = self.expandirNodos(nodoActual=nodoActual, nodosExtendidosGlobal=nodosExtendidosGlobal)
            else:
                print("estas re-expandiendo un nodo que ya se expandio, pero tranqui aqui le solucionamos los hijos jsjs")
                nodoActual.set_valorHijoMenorAcumulado(0) # Como haremos el mismo proceso de expansión, establecemos el valor del hijo a 0.
                # Al parecer, tendremos que independizar el método de expansión, 
                # ya que para poder volver a expandirlo, necesitamos tener los hijos y saber cuál es el mínimo para expandirlo.
                # En otras palabras, se realiza una doble expansión de dominio.
                contadorReExpancion += 1

                nodoDobleExpancion, nodosExtendidosPorNodo= self.expandirNodos(nodoActual= nodoActual, nodosExtendidosGlobal=nodosExtendidosGlobal)
                print("el nodo elejido para hacer la doble expancion fue : {}".format(nodoDobleExpancion))

                nodoElejido = min(nodosExtendidosPorNodo)

                nodosExtendidosGlobal.remove(nodoElejido)

                nodoDobleExpancionFinal, nodosExtendidosPorNodo= self.expandirNodos(nodoActual= nodoElejido, nodosExtendidosGlobal=nodosExtendidosGlobal)

                nodoActual = nodoDobleExpancionFinal

                print("el nodo actual es: {}".format(nodoActual))
            #print(nodosExtendidosGlobal)
            

                
            #Evaluamos la listaNodosExtendidos global, y preguntamos cual tiene el menor valor acumulado (nodo siguiente para avanzar)

            print("imprimimos la lista de nodos extendidos globales")
            for nodo in nodosExtendidosGlobal:
                print(nodo)
            #print(nodoElejido)

            nodoElejido = min(nodosExtendidosGlobal) #se elije el nodo menor de la lista de expandidos globales, independientmente si ya fue comprimido o no

            if nodoElejido not in nodosExtendidosPorNodo:
                #si no es un nodo que acabamos de expandir, quiere decir que se cambio de rama, en esta parte del codigo es donde se comprime la rama
                print("se cambio de rama, iniciando proceso de compresion")
                hijoMenor = min(nodosExtendidosPorNodo)
                    
                nodoActual.set_valorHijoMenorAcumulado(hijoMenor.get_ValorAcumulado()) #añadimos el valor del hijo menor acumulado a la variable correspondinete en el padre,

                #ahora debemos de eliminar los hijos de ese nodo, todos los hijos ademas de removerlos de nodosEstendisosGlobal


                print("SONA DE ELIMINACION".center(50,"-"))

                print(nodoActual.get_hijoUp())
                print(nodoActual.get_hijoRight())
                print(nodoActual.get_hijoBottom())
                print(nodoActual.get_hijoLeft())
                print("".center(50,"-"))


                if nodoActual.get_hijoUp() is not None:
                    print("entra aqui en el de arrriba")

                    nodosExtendidosGlobal.remove(nodoActual.get_hijoUp())
                
                if nodoActual.get_hijoRight() is not None:
                    print("entra aqui en el de derecha")
                    nodosExtendidosGlobal.remove(nodoActual.get_hijoRight())
                
                if nodoActual.get_hijoBottom() is not None:
                    print("entra aqui en el de abajo")
                    nodosExtendidosGlobal.remove(nodoActual.get_hijoBottom())

                if nodoActual.get_hijoLeft() is not None:
                    print("entra aqui en el hp problema :)")

                    nodosExtendidosGlobal.remove(nodoActual.get_hijoLeft())
                
                print("al momento de elimar los hijos, la lista expandidos global queda asi.".center(90,"-"))

                for nodo in nodosExtendidosGlobal:
                    print(nodo)

                #de esta forma eliminamos de la estructura los hijos que acabamos de crear y comprimimos la rama
                nodoActual.set_hijoUp(None)
                nodoActual.set_hijoRight(None)
                nodoActual.set_hijoBottom(None)
                nodoActual.set_hijoLeft(None)
                contadorComprimidos +=1


                nodosExtendidosGlobal.append(nodoActual)
                print("añadimos a la lista el siguiente nodo: {}".format(nodoActual))

    
            else: 
                print("se escogio un nodo de la misma rama, es decir del nodo que acabamos de expandir.")
            
            print("nodo elejido: {}".format(nodoElejido))        
            nodosExtendidosGlobal.remove(nodoElejido)

            nodoActual = nodoElejido #nos dirijimos al nodo seleccionado
                


        listaCamino =[]

        print("camino calculado hasta ahora")
        while nodoActual.get_padre() is not None:
            
            listaCamino.append([nodoActual.get_coordenadas(), nodoActual.get_ValorAcumulado()])

            #print(nodoActual)

            nodoActual = nodoActual.get_padre()
        
        print(listaCamino[::-1])
        print("la cantidad de nodos comprimidos son de: {}".format(contadorComprimidos))
        print("la cantidad de nodos re-expandidos son de: {}".format(contadorReExpancion))