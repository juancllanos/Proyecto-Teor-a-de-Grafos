# -*- coding: utf-8 -*-


class WeightedGraph(object):

    def __init__(self,N,E):
        v = True
        for i in E:
            for j in i[0]:
                if j in N:
                    v = v and True
                else :
                    v = v and False
        if v == False:
            print("Error")
        else:
            self.N = N
            self.E = E

    def WeighMatrix(self):
        matrix = []
        #Creamos la matriz de pesos, inicialmente vacia.
        for i in self.N:
        #Iteramos sobre los nodos para sacar los pesos de los lados a los que es adyacente.
            temp = []
            #Esta lista contendrá esos pesos.
            for j in self.N:
                #Iteramos nuevamente sobre los nodos para saber a cules 'i' es vecino.
                var = False
                #Creamos una variable booleana para saber si existe el lado que une a 'i' con 'j'.
                for k in self.E:
                #Iteramos sobre los lados para confirmar que la pareja 'i' con 'j' es un lado
                    if((i,j) in k or (j,i) in k):
                    #Comparamos para ver si existe el lado.
                        temp.append(k[1])
                        #Como existe el lado, nos metemos en su segundo elemento para acceder a su peso.
                        var = var or True
                        #Cambiamos el valor a var porque efectivamente el lado existe.
                    else:
                        var =var or False
                        #Si el lado no existe se queda con el valor de falso.
                if var == False:
                    temp.append(0)
                #Cuando termine de iterar sobre los lados si var queda valiendo falso quiere decir que el lado no
                #existe, entonces agregamos el valor 0.
            matrix.append(temp)
        return matrix






    
