import Modelo.CostoUniformeRecursivo as cur
import Vista.InterfazGrafica as GUI

#ESTO SOLO ES UN EJEMPLO DE COMO FUNCIONA EL ALROGITMO
#LO QUE DEBE DE TENER ESTE ARCHIVO SERA EL LLAMADO A INICIAR LA VISTA


#para instalar todas las librerias trabajadas del entorno se debe de escribir dentro del entorno pip install -r requiriments.txt

tablero = [[1,1,3,1,1,1,1,1],
           [1,-2,0,0,-2,0,0,1],
           [1,0,1,1,1,0,0,1], 
           [1,0,1,0,0,0,1,1],
           [1,-2,1,3,1,1,1,1]]


# matriz para graficar
tablero2 = [[1, 1, 3, 1, 1, 1, 1, 1],
           [1, 2, 0, 0, 2, 0, 0, 1],
           [4, 0, 1, 1, 1, 0, 0, -1],
           [1, 0, 1, 0, 0, 0, 1, 1],
           [1, 2, 1, 3, 1, 1, 1, 1]]


algoritmo = cur.AlgoritmoCURecursivo(tablero=tablero, puntoInicial = [2,7], puntoFinal = [2,0])

print(algoritmo.costoUniformeRecursivo())


obj = GUI.tablero(tablero2)

obj.start()
