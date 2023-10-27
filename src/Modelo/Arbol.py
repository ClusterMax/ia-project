
#2.Nodo.py == (nodoPadre, [x,y], valorReal, 
# ValorAcumulado, valorHijoMenorAcumulado, }
#hijos1, hijo2, hijo3, hijo4)


#Esta clase es para crear un nodo, la unidad minima de un arbol, en el proyecto, este representa una casilla en la que el jugador puede pasar 

class Arbol:
    

    #Metodo constructor, el cual se llama implicitamente al momento de crear una instancia de la clase
    def __init__(self, padre=None, coordenadas=[], valorReal=None, ValorAcumulado=None, valorHijoMenorAcumulado=None, hijoUp=None, hijoRight=None, hijoBottom=None, hijoLeft=None, tipo="vacio"):
        self.padre = padre
        self.coordenadas = coordenadas
        self.valorReal = valorReal
        self.ValorAcumulado = ValorAcumulado
        self.valorHijoMenorAcumulado = valorHijoMenorAcumulado
        self.hijoUp = hijoUp
        self.hijoRight = hijoRight
        self.hijoBottom = hijoBottom
        self.hijoLeft = hijoLeft
        self.tipo = tipo
    
    #Metodo del operador == par apoder comprarar objetos de la misma clase
    def __eq__(self, other):

        if self is None and other is None:
            return True
        
        elif self is None and other is not None:
            return False
        elif self is not None and other is None:
            return False
        else:
            return self.coordenadas == other.coordenadas and self.padre == other.padre and self.ValorAcumulado == other.valorAcumulado
    
    #Metodo del operador > par apoder comprarar objetos de esta clase
    def __gt__(self, other):

        if self.valorHijoMenorAcumulado == 0 and other.valorHijoMenorAcumulado == 0:
            return self.ValorAcumulado > other.ValorAcumulado
        elif self.valorHijoMenorAcumulado != 0 and other.valorHijoMenorAcumulado != 0:
            return self.valorHijoMenorAcumulado > other.valorHijoMenorAcumulado
        elif self.valorHijoMenorAcumulado == 0 and other.valorHijoMenorAcumulado != 0:
            return self.ValorAcumulado > other.valorHijoMenorAcumulado
        elif self.valorHijoMenorAcumulado != 0 and other.valorHijoMenorAcumulado == 0:
            return self.valorHijoMenorAcumulado > other.ValorAcumulado
    
    #Metodo del operador >= par apoder comprarar objetos de esta clase
    def __ge__(self, other):
        if self.valorHijoMenorAcumulado == 0 and other.valorHijoMenorAcumulado == 0:
            return self.ValorAcumulado >= other.ValorAcumulado
        elif self.valorHijoMenorAcumulado != 0 and other.valorHijoMenorAcumulado != 0:
            return self.valorHijoMenorAcumulado >= other.valorHijoMenorAcumulado
        elif self.valorHijoMenorAcumulado == 0 and other.valorHijoMenorAcumulado != 0:
            return self.ValorAcumulado >= other.valorHijoMenorAcumulado
        elif self.valorHijoMenorAcumulado != 0 and other.valorHijoMenorAcumulado == 0:
            return self.valorHijoMenorAcumulado >= other.ValorAcumulado

    #Metodo del operador < par apoder comprarar objetos de esta clase
    def __lt__(self, other):
        if self.valorHijoMenorAcumulado == 0 and other.valorHijoMenorAcumulado == 0:
            return self.ValorAcumulado < other.ValorAcumulado
        elif self.valorHijoMenorAcumulado != 0 and other.valorHijoMenorAcumulado != 0:
            return self.valorHijoMenorAcumulado < other.valorHijoMenorAcumulado
        elif self.valorHijoMenorAcumulado == 0 and other.valorHijoMenorAcumulado != 0:
            return self.ValorAcumulado < other.valorHijoMenorAcumulado
        elif self.valorHijoMenorAcumulado != 0 and other.valorHijoMenorAcumulado == 0:
            return self.valorHijoMenorAcumulado < other.ValorAcumulado

    #Metodo del operador <= par apoder comprarar objetos de esta clase
    def __le__(self, other):
        if self.valorHijoMenorAcumulado == 0 and other.valorHijoAcumulado == 0:
            return self.ValorAcumulado <= other.ValorAcumulado
        elif self.valorHijoMenorAcumulado != 0 and other.valorHijoMenorAcumulado != 0:
            return self.valorHijoMenorAcumulado <= other.valorHijoMenorAcumulado
        elif self.valorHijoMenorAcumulado == 0 and other.valorHijoMenorAcumulado != 0:
            return self.ValorAcumulado <= other.valorHijoMenorAcumulado
        elif self.valorHijoMenorAcumulado != 0 and other.valorHijoMenorAcumulado == 0:
            return self.valorHijoMenorAcumulado <= other.ValorAcumulado
    

    #METODOS DE GET Y SET

    def get_padre(self):
        return self.padre
    
    def set_padre(self, padre):
        self.padre = padre

    def get_coordenadas(self):
        return self.coordenadas
    
    def set_coordenadas(self, coordenadas):
        self.coordenadas = coordenadas

    def get_valorReal(self):
        return self.valorReal
    
    def set_valorReal(self, valorReal):
        self.valorReal = valorReal

    def get_ValorAcumulado(self):
        return self.ValorAcumulado
    
    def set_ValorAcumulado(self, ValorAcumulado):
        self.ValorAcumulado = ValorAcumulado

    def get_valorHijoMenorAcumulado(self):
        return self.valorHijoMenorAcumulado
    
    def set_valorHijoMenorAcumulado(self, valorHijoMenorAcumulado):
        self.valorHijoMenorAcumulado = valorHijoMenorAcumulado

    def get_hijoUp(self):
        return self.hijoUp
    
    def set_hijoUp(self, hijoUp):
        self.hijoUp = hijoUp

    def get_hijoRight(self):
        return self.hijoRight
    
    def set_hijoRight(self, hijoRight):
        self.hijoRight = hijoRight

    def get_hijoBottom(self):
        return self.hijoBottom
    
    def set_hijoBottom(self, hijoBottom):
        self.hijoBottom = hijoBottom

    def get_hijoLeft(self):
        return self.hijoLeft
    
    def set_hijoLeft(self, hijoLeft):
        self.hijoLeft = hijoLeft

    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo):
        self.tipo = tipo
    

    #Metodo que retorna todos los atributos de una instancia de la clase
    def data(self):

        datos = [
        self.padre ,
        self.coordenadas,
        self.valorReal,
        self.ValorAcumulado ,
        self.valorHijoMenorAcumulado,
        self.hijoUp ,
        self.hijoRight,
        self.hijoBottom ,
        self.hijoLeft
        ]

        return datos

    #Metodo para poder imprimir un objeto en consola
    def __str__(self):
        return "Coordenadas: {}  valorAcumulado: {} valorHijoMenor: {}".format(self.coordenadas, self.ValorAcumulado, self.valorHijoMenorAcumulado)
