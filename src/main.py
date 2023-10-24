import Modelo.CostoUniformeRecursivo as cur


#ESTO SOLO ES UN EJEMPLO DE COMO FUNCIONA EL ALROGITMO
#LO QUE DEBE DE TENER ESTE ARCHIVO SERA EL LLAMADO A INICIAR LA VISTA


#para instalar todas las librerias trabajadas del entorno se debe de escribir dentro del entorno pip install -r requiriments.txt

tablero = [[1,1,3,1,1,1,1,1],
           [1,-2,0,0,-2,0,0,1],
           [1,0,1,1,1,0,0,1], 
           [1,0,1,0,0,0,1,1],
           [1,-2,1,3,1,1,1,1]]

algoritmo = cur.AlgoritmoCURecursivo(tablero=tablero)

print(algoritmo.costoUniformeRecursivo())