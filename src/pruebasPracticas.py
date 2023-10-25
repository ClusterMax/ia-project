
#en este archivo se encontraran diferentes laberintos, por el cual el agente debera pasar y resolver
#todos estos tableros son derivados del primer tablero original (el cual se recoore al inicial el juego)


#import Modelo.CostoUniformeRecursivo as cur
#import Vista.InterfazGrafica as GUI

import Modelo.CostoUniformeRecursivo as cur
import Vista.InterfazGrafica as GUI



# PRUEBA 1 TABLERO ORIGINAL, DIFERENTE POSICIONES DE META E INICIO
tablero1a = [[1,1,3,1,1,1,1,1],
           [1,-2,0,0,-2,0,0,1],
           [1,0,1,1,1,0,0,1], 
           [1,0,1,0,0,0,1,1],
           [1,-2,1,3,1,1,1,1]]

puntoInicial1 = [2,7]
PuntoFinal = [2,0]

# Define la matriz del tablero
tablero1 = [[1, -1, 3, 1, 1, 1, 1, 1],
           [1, 2, 0, 0, 2, 0, 0, 1],
           [1, 0, 1, 1, 1, 0, 0, 1],
           [1, 0, 1, 0, 0, 0, 1, 1],
           [1, 2, 1, 3, 1, 1, 4, 1]]


#algoritmo = cur.AlgoritmoCURecursivo(tablero=tablero1, puntoInicial = [2,7], puntoFinal = [2,0])

#print(algoritmo.costoUniformeRecursivo())


#obj = GUI.tablero(tablero1)

#obj.start()


#PRUEBA 2 TABLERO ORIGINAL, DIFERENTE POSICIONES DE GATOS

tablero1 = [[1, 1, 1, 1, 1, 1, 1, 1],
           [1, 2, 0, 0, 2, 0, 0, 1],
           [4, 0, 1, 3, 1, 0, 0, -1],
           [3, 0, 1, 0, 0, 0, 1, 1],
           [1, 2, 1, 3, 1, 1, 1, 1]]

#obj = GUI.tablero(tablero1)

#obj.start()

#PRUEBA 3 TABLERO ORIGINAL, DIFERENTE POSICICIONES DE AMOS
tablero1 = [[2, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 0, 0, 1, 0, 0, 1],
           [4, 0, 1, 3, 1, 0, 0, -1],
           [3, 0, 1, 0, 0, 0, 1, 1],
           [1, 2, 1, 3, 1, 2, 1, 1]]

#obj = GUI.tablero(tablero1)

#obj.start()
#PRUEBA 4 TABLERO NUEVO, POSICIONES INICIALES DE 4,6 Y META DE 0,0
tablero2 = [[4, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [1, 0, 2, 0, 2, 0, 1],
            [1, 0, 1, 1, 0, 2, -1],
            [1, 1, 1, 1, 1, 1, 1]]

tablero2a = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [1, 0, -2, 0, -2, 0, 1],
            [1, 0, 1, 1, 0, -2, 1],
            [1, 1, 1, 1, 1, 1, 1]]


algoritmo = cur.AlgoritmoCURecursivo(tablero=tablero2a, puntoInicial = [4,6], puntoFinal = [0,0])

print(algoritmo.costoUniformeRecursivo())

obj2 = GUI.tablero(tablero2)

obj2.start()

#PRUEBA 5 SEGUNDO TABLERO, AUMENTO DE GATOS

tablero2 = [[4, 3, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [3, 0, 2, 0, 2, 0, 1],
            [1, 0, 1, 1, 0, 2, -1],
            [1, 1, 3, 1, 1, 1, 1]]

tablero2b = [[1, 3, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [3, 0, -2, 0, -2, 0, 1],
            [1, 0, 1, 1, 0, -2, 1],
            [1, 1, 3, 1, 1, 1, 1]]


algoritmo = cur.AlgoritmoCURecursivo(tablero=tablero2b, puntoInicial = [4,6], puntoFinal = [0,0])

print(algoritmo.costoUniformeRecursivo())


obj2 = GUI.tablero(tablero2)

obj2.start()

#PRUEBA 6 SEGUNDO TABLERO AUMENTO DE AMOS

tablero2 = [[4, 3, 1, 3, 1, 1, 1],
            [1, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [3, 0, 2, 0, 2, 0, 1],
            [1, 0, 1, 1, 0, 2, -1],
            [2, 1, 3, 1, 2, 1, 1]]

tablero2c = [[1, 3, 1, 3, 1, 1, 1],
            [1, 0, 0, 0, 3, 0, 1],
            [1, 0, 0, 1, 0, 0, 1],
            [3, 0, -2, 0, -2, 0, 1],
            [1, 0, 1, 1, 0, -2, 1],
            [-2, 1, 3, 1, -2, 1, 1]]


algoritmo = cur.AlgoritmoCURecursivo(tablero=tablero2c, puntoInicial = [4,6], puntoFinal = [0,0])

print(algoritmo.costoUniformeRecursivo())

obj2 = GUI.tablero(tablero2)


obj2.start()
