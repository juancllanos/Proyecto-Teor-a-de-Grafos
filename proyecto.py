# -*- coding: cp1252 -*-
import itertools


class Graph(object):
    
    def __init__(self,vertex,edges):
        v = True
        for i in edges:
            for j in i:
                if j in vertex:
                    v = v and True
                else :
                    v = v and False
        if v == False:
            print ("Error")
        else:
            self.vertex = vertex
            self.edges = edges

            
    def AdjacencyMatrix(self):
        AM = []
        for i in self.vertex:
            A = []
            for j in self.vertex:
                if (i,j) in self.edges or (j,i) in self.edges:
                    A.append(1)
                else:
                    A.append(0)
            AM.append(A)
        return AM
            


    def isIsomorphTo(self,H):
        if len(self.edges) == len(H.edges) and len(self.vertex) == len(H.vertex):
            AM = self.AdjacencyMatrix()
            P = itertools.permutations(H.vertex)
            PL = []
            for i in P:
                PL.append(list(i))
            for j in PL:
                G = Graph(j,H.edges)
                AMG = G.AdjacencyMatrix()
                if AM == AMG:
                    return True
            return False
            
        else:
            return False
    
    
    def distancia(self,u,v):
        if (u in self.vertex) and (v in self.vertex):
            N_u = []
            N_v = []
            for i in self.vertex:
                if (u,i) in self.edges or (i,u) in self.edges:
                    N_u.append(i)
            for i in self.vertex:
                if (v,i) in self.edges or (i,v) in self.edges:
                    N_v.append(i)
            if (len(N_u) == 0 or len(N_v) == 0):
                return -1
            if u == v:
                return 0
            # En esta ejecuci�n revisamos si los dos nodos estan en el grafo y ademas si estan
            # desconectados o si son el mismo, en caso de que alguno de los dos est� desconectado
            # retorna -1 y son el mismo nodo retorna 0.
            
            else:
                s = set()
                r = set(u)
                g = set(self.vertex)
                g.remove(u)
                distance = {}
                distance[u] = 0
            # Inicializamos 's' (nodos ya visitados), 'r' (nodos por visitar) , 'g' (nodos que no estan ni en r ni en s) y
            # un diccionario 'distance' en el cual vamos guardando la distancia de u a cada nodo.
                while (len(r) != 0):
                    r_temp = r
                    # Creamos un r temporal para poder ejecutar el for sobre 'r'.
                    for i in r_temp:
                        if i in r:
                            N = set()
                    # 'N' es el conjunto de los vecinos.
                            if i == v:
                                return distance[i]
                    # En el caso de que 'v' ya lo hayamos visitado significa que ya sabemos su distancia
                    # por lo tanto la retornamos sin necesidad de ejecutar todo el algoritmo.
                            for j in self.vertex:
                                if j in g:
                                    if (i,j) in self.edges or (j,i) in self.edges:
                                        N.add(j)
                                        g.remove(j)
                                        distance[j] = distance[i]+1
                    # En este paso revisamos los nodos que estan en 'g' y vemos si son vecinos del nodo que estamos
                    # evaluando, si es se agrega a los vecino, se quita de 'g' y se agrega su distancia al diccionario
                    # sumandole uno a la distancia del nodo que estamos evaluando.
                                    else:
                                        distance[j] = -1
                    # De lo contrario quiere decir que desde el nodo que estamos evaluando no podemos llegar a 'j'
                    # todavia por lo tanto su distancia es -1 (infinito).
                            r = r.union(N)
                            r.remove(i)
                            s.add(i)
                    # Cuando salimos del for a 'r' le agregamos los vecinos, los nodos que vamos a visitar,
                    # quitamos el nodo que ya evaluamos y lo agregamos a 's'.
                return distance[v]
            # Cuando ya visitamos todos los nodos posibles retornamos la distancia de 'v'.
        else:
            return "Error"
        # Si alguno de los nodos no esta en el conjunto de los vertices entonces retorna error.
        
    
    
    def diametro(self):
        #Todas las combinaciones de tama�o 2 posibles entre el conjunto de nodos 
        P = set(itertools.combinations(self.vertex,2))
        maximo = 0
        for i in P:
            #distancia que existe entre el par de nodos
            valor = self.distancia(i[0],i[1])
            #Si la distancia es infinita retorna -1
            if(valor == -1):
                return -1
            #Si la distancia que se logr� es mayor a la que se tenia se renueva la variable m�ximo
            elif(valor>maximo):
                maximo = valor
        #Retorna la distancia m�xima 
        return maximo 
            
            
    def excentricidad(self,n):
        valor = 0
        #Evalua la disitancia entre el nodo n y todos los otros nodos del conjunto
        for i in self.vertex: 
            dis = self.distancia(n, i)
            #Si la distancia es infinita retorna -1
            if(dis==-1):
                return -1
            #Si la distancia es mayor al valor que ya se ten�a se renueva la variable valor
            elif(dis>valor):
                valor = dis
        #Retorna la mayor distancia entre el nodo n y otro nodo del grafo
        return valor
    
    def radio(self):
        minimo = len(self.vertex)
        #Evalua la excentricidad de todos los nodos del grafo
        for i in self.vertex:
            valor = self.excentricidad(i)
            print "------>radio:",valor
            #Si la distancia es infinita retorna -1
            if(valor== -1):
                return -1
            #Si la distancia es menor al valor que ya se ten�a se renueva la variable m�nimo
            elif(valor<minimo):
                minimo = valor
        #Retorna la excentricidad m�nima 
        return minimo
    
    
    def conectado(self):
        #Todas las combinaciones de tama�o 2 posibles entre el conjunto de nodos
        P = set(itertools.combinations(self.vertex,2))
        #Evalua todos los pares de nodos
        for i in P:
            #Distancia entre el par de nodos
            valor = self.distancia(i[0],i[1])
            #Si la distancia es infinita entonces retorna False, no est� conectado
            if(valor == -1):
                return False
        #En el caso en el que no se encuentre una distancia infinita entonces retorna True, est� conectado
        return True
            
            
    def esArbol(self):
        #Evalua si la longitud de los lados es igual a la de los nodos-1, y si est� conectado
        if(len(self.edges)==len(self.vertex)-1 and self.conectado()==True):
            return True;
        else:
            return False

    def gradoNodo(self,n):
        #Retorna el grado de un nodo
        contador = 0
        for i in self.edges:
            if((n in i)==True and not((n,n)in self.edges)):
                contador+=1
        return contador

    def esEuleriano(self):
        #Crea un nuevo grafo quitando la posibilidad de que haya un nodo de grado cero
        newVertex = []
        newEdges = self.edges
        for i in self.vertex:
            if(self.gradoNodo(i)!=0):
                newVertex.append(i)
            else:
                for j in newEdges:
                    if(i in j):
                        newEdges.pop(newEdges.index(j))
        valor = True
        #Evalua la paridad de todos los nodos 
        for i in newVertex:
            if(self.gradoNodo(i)%2 != 0):
                valor = False
        #Evalua si el grafo est� conectado
        if (self.conectado==False):
            valor = False
        #Si el grado de todos los nodos es par y est� conectado estnonces es euleriano
        return valor
