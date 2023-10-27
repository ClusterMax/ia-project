
#en este archivo se encontraran diferentes laberintos, por el cual el agente debera pasar y resolver
#todos estos tableros son derivados del primer tablero original (el cual se recoore al inicial el juego)


#import Modelo.CostoUniformeRecursivo as cur
#import Vista.InterfazGrafica as GUI

import Modelo.CostoUniformeRecursivo as cur
import Vista.InterfazGrafica as GUI

#PRUEBA 1  POSICIONES INICIALES DE 4,6 Y META DE 0,0

tablero2a = [[1, 1, 3, 1, 1, 1, 1, 1],
           [1, -2, 0, 0, -2, 0, 0, 1],
           [1, 0, 1, 1, 1, 0, 0, 1],
           [1, 0, 1, 0, 0, 0, 3, 1],
           [1, -2, 1, 3, 1, 1, 1, 1]]



obj2 = GUI.tablero(tablero2a, posJugador=[4,6], posMeta=[0,0])

obj2.start()

#PRUEBA 2 AUMENTO DE GATOS
tablero2b = [[1, 1, 3, 1, 1, 1, 1, 1],
           [1, -2, 0, 0, -2, 0, 0, 1],
           [1, 0, 1, 1, 1, 0, 0, 1],
           [3, 0, 1, 0, 0, 0, 3, 1],
           [1, -2, 1, 3, 1, 1, 1, 1]]

obj2 = GUI.tablero(tablero2b)

obj2.start()

#PRUEBA 3 DIFRENTE POSICIONES DE META Y JUGADOR

tablero2c = [[1, 1, 3, 1, 1, 1, 1, 1],
           [1, -2, 0, 0, -2, 0, 0, 1],
           [1, 0, 1, 1, 1, 0, 0, 1],
           [3, 0, 1, 0, 0, 0, 3, 1],
           [1, -2, 1, 3, 1, 1, 1, 1]]



obj2 = GUI.tablero(tablero=tablero2c, posJugador=[4,7], posMeta=[2,3])
obj2.start()

#PRUEBA 4 AUMENTO DE AMOS Y DE MUROS

tablero3 = [[0, 0, 3, 1, 1, 1, 1, 1],
           [1, -2, 0, 0, -2, 0, 0, 1],
           [1, 0, 1, 1, 1, 0, 0, 1],
           [3, 0, 1, 0, 0, 0, 3, 1],
           [1, -2, 1, 3, 0, -2, 1, 1]]



obj2 = GUI.tablero(tablero=tablero3, posJugador=[4,7], posMeta=[2,3])
obj2.start()


#PRUEBA 5 ESCENARIO DIFERENE    

game_board = [[1, 0, 0, 0, 0, 0, 1, -2],
              [3, 1, 1, 1, 1, 1, 1, 0],
              [1, 1, 0, 1, -2, 1, -2, 0],
              [1, -2, 0, 1, 0, 1, 1, 1],
              [1, 1, 3, -2, 1, 3, 1, 3],
]

obj2 = GUI.tablero(tablero=game_board, posJugador=[4,0], posMeta=[1,5])
obj2.start()


#PRUEBA 6 SEGUNDO TABLERO MAS MUROS  

game_board = [[1, 0, 0, 0, 0, 0, 1, -2],
              [3, 1, 1, 1, 0, 1, 0, 0],
              [1, 1, 0, 1, -2, 1, -2, 0],
              [1, -2, 0, 1, 0, 1, 1, 1],
              [1, 1, 3, -2, 1, 3, 1, 3],
]

obj2 = GUI.tablero(tablero=game_board, posJugador=[4,0], posMeta=[1,5])
obj2.start()

#PRUEBA 7 ESCENARIO MAS GRANDE 
game_board = [ [1, 0, 0, 0, 0, 0, 1, -2, 1, 1, 1, 1],
              [3, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
              [1, 1, 0, 1, -2, 1, -2, 0, 1, 0, 1, 3],
              [1, -2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 3, -2, 1, 3, 1, 3, 1, 1, -2, 1],
]

obj2 = GUI.tablero(tablero=game_board, posJugador=[4,0], posMeta=[1,9])
obj2.start()

#PRUEBA 8 ESCENARIO MAS GRANDE DIFERENTES POSICIONES

game_board = [ [1, 0, 0, 0, 0, 0, 1, -2, 1, 1, 1, 1],
              [3, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
              [1, 1, 0, 1, -2, 1, -2, 0, 1, 0, 1, 3],
              [1, -2, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 3, -2, 1, 3, 1, 3, 1, 1, -2, 1],
]

obj2 = GUI.tablero(tablero=game_board, posJugador=[4,8], posMeta=[1,1])
obj2.start()

