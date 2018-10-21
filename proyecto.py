# -*- coding: cp1252 -*-
import itertools
from collections import OrderedDict
from copy import deepcopy


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
            # En esta ejecución revisamos si los dos nodos estan en el grafo y ademas si estan
            # desconectados o si son el mismo, en caso de que alguno de los dos esté desconectado
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
        #Todas las combinaciones de tamaño 2 posibles entre el conjunto de nodos 
        P = set(itertools.combinations(self.vertex,2))
        maximo = 0
        for i in P:
            #distancia que existe entre el par de nodos
            valor = self.distancia(i[0],i[1])
            #Si la distancia es infinita retorna -1
            if(valor == -1):
                return -1
            #Si la distancia que se logró es mayor a la que se tenia se renueva la variable máximo
            elif(valor>maximo):
                maximo = valor
        #Retorna la distancia máxima 
        return maximo 
            
            
    def excentricidad(self,n):
        valor = 0
        #Evalua la disitancia entre el nodo n y todos los otros nodos del conjunto
        for i in self.vertex: 
            dis = self.distancia(n, i)
            #Si la distancia es infinita retorna -1
            if(dis==-1):
                return -1
            #Si la distancia es mayor al valor que ya se tenía se renueva la variable valor
            elif(dis>valor):
                valor = dis
        #Retorna la mayor distancia entre el nodo n y otro nodo del grafo
        return valor
    
    def radio(self):
        minimo = len(self.vertex)
        #Evalua la excentricidad de todos los nodos del grafo
        for i in self.vertex:
            valor = self.excentricidad(i)
            #Si la distancia es infinita retorna -1
            if(valor== -1):
                return -1
            #Si la distancia es menor al valor que ya se tenía se renueva la variable mínimo
            elif(valor<minimo):
                minimo = valor
        #Retorna la excentricidad mínima 
        return minimo
    
    
    def conectado(self):
        #Todas las combinaciones de tamaño 2 posibles entre el conjunto de nodos
        P = set(itertools.combinations(self.vertex,2))
        #Evalua todos los pares de nodos
        for i in P:
            #Distancia entre el par de nodos
            valor = self.distancia(i[0],i[1])
            #Si la distancia es infinita entonces retorna False, no está conectado
            if(valor == -1):
                return False
        #En el caso en el que no se encuentre una distancia infinita entonces retorna True, está conectado
        return True
            
            
    def esArbol(self):
        lados = self.edges
        for i in range(1,len(self.edges)-1):
            valor = lados[len(lados)-i]
            if((valor[1],valor[0]) in lados):
                lados.pop(lados.index((valor[1],valor[0])))
        #Evalua si la longitud de los lados es igual a la de los nodos-1, y si está conectado
        if(len(lados)==len(self.vertex)-1 and self.conectado()==True):
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
        #Evalua si el grafo está conectado
        if (self.conectado==False):
            valor = False
        #Si el grado de todos los nodos es par y está conectado estnonces es euleriano
        return valor

    def vecindario(self,nodo):
        vecinos = []
        for i in self.edges:
            if(nodo == i[0]):
                vecinos.append(i[1])
            elif(nodo == i[1]):
                vecinos.append(i[0])
        return vecinos


    def esBipartito(self):
        if(self.esArbol()==True):
            return True
        else:
            grafo = self.Biparticion()
            if(len(set(grafo[0])& set(grafo[1]))!=0):
                return False
            else:
                return True

    def Biparticion(self):
        x = []
        y = []
        for i in self.vertex:
            if(not(i in x) and (i in y)):
                x = x + self.vecindario(i)
            elif(not(i in y) and (i in x)):
                y = y + self.vecindario(i)
            else:
                x.append(i)
                y = y + self.vecindario(i)
        return [list(OrderedDict.fromkeys(x)),list(OrderedDict.fromkeys(y))]
        

    def findCA(self,grafo,emp,S,T,final):
        print "----------------->Conj. INICIAL S: ",S
        print "----------------->Conj. INICIAL T: ",T
        if(len(S)==0 or final==True):
            print "S ESTA VACIO"
            cubrimiento = (set(T) | (set(grafo[0])-set(S)))
            return [cubrimiento,emp]
        else:
            for i in S:
                print "--------->PRIMER VALOR DE S: ",i
                for j in self.vecindario(i):
                    print "----------------->PRIMER VALOR DE J: ",j
                    Jsaturado = False
                    for k in emp:
                        if(j in k):
                            Jsaturado = True
                    print "----------------->J ESTA SATURADO?: ",Jsaturado
                    if((not((i,j) in emp) or not((j,i) in emp)) and Jsaturado==False):
                        print "----------------->SE ENCONTRO CAMINO AUMENTADOR EN : (%r,%r)" %(i,j)
                        emp.append((i,j))
                        print "########################################################################################################"
                        S = []
                        for mp in grafo[0]:
                            esta = False
                            for hi in emp:
                                if(mp in hi):
                                    esta = True
                            if(esta==False):
                                S.append(mp)
                        return self.findCA(grafo,emp,S,[],False)
                    else:
                        print "Emparejamiento: ",emp
                        T = T+[j]
                        w = 0
                        for p in emp:
                            print "Valor de p: ",p
                            if(j == p[0]):
                                w = p[1]
                                break
                            elif(j== p[1]):
                                w = p[0]
                                break
                        print "Valor w: ",w
                        if(not(w in S)):
                            S = S+[w]
                        print "----------------->Conj. S: ",S
                        print "----------------->Conj. T: ",T
                #S.pop(S.index(i))
            return self.findCA(grafo,emp,S,T,True)
        
                
                        

        
    def caminoAumentador(self):
        if(self.esBipartito==False):
            return "Error"
        else:
            grafo = self.Biparticion()
            return self.findCA(grafo,[],grafo[0],[],False)


########################################################################################################################################################
class WeightedGraph(object):

        def __init__(self,vertex,edges):
            self.vertex = vertex
            self.edges = edges


        def WeightMatrix(self):
            matrix = []
            for i in self.vertex:
                temp = []
                for j in self.vertex:
                    var = False
                    for k in self.edges:
                        if((i,j) in k or (j,i) in k):
                            temp.append(k[1])
                            var = var or True
                        else:
                            var =var or False
                    if var == False:
                        if(i==j):
                            temp.append(0)
                        else:
                            temp.append(-1)
                matrix.append(temp)
            return matrix
        

        def vecindario(self,nodo):
            vecinos = []
            for i in self.edges:
                if(nodo == i[0][0]):
                    vecinos.append(i[0][1])
                elif(nodo == i[0][1]):
                    vecinos.append(i[0][0])
            return vecinos


        def esBipartito(self):
            grafo = self.Biparticion()
            if(len(set(grafo[0])& set(grafo[1]))!=0):
                return False
            else:
                return True


        def Biparticion(self):
            x = []
            y = []
            for i in self.vertex:
                if(not(i in x) and (i in y)):
                    x = x + self.vecindario(i)
                elif(not(i in y) and (i in x)):
                    y = y + self.vecindario(i)
                else:
                    x.append(i)
                    y = y + self.vecindario(i)
            return [list(OrderedDict.fromkeys(x)),list(OrderedDict.fromkeys(y))]
        
        

        def IAH(self,bipa,matriz,emp,puntX,puntY):
            if(len(emp)==len(bipa[0])):
                return emp
            else:
                lados = []
                for j in range(len(puntX)):
                    for h in range(len(puntY)): 
                        suma = puntX[j]+puntY[h]
                        print "SUMA VITALMENTE IMPORTANTE: (%r+%r)= %r, (%r)" %(puntX[j],puntY[h],suma,matriz[j][h])
                        if(suma==matriz[j][h]):
                            print "Entrada"
                            lados.append((self.vertex[j],self.vertex[h+len(bipa[0])]))

                

                print "SUPER IMPORTANTE LADOS: ",lados
                Nvertex = []
                for i in self.vertex:
                    for j in lados:
                        if(i in j):
                            Nvertex.append(i)
                print "--->Nuevos vertices: ",list(OrderedDict.fromkeys(Nvertex))
                G = Graph(list(OrderedDict.fromkeys(Nvertex)),lados)
                #print "SUPER IMPORTANTE BIPARTICION: ",G.Biparticion()
                camino =  G.caminoAumentador()
                print "----------------->CAMINO: ",camino
                Q = list(camino[0])
                R = list(set(Q)&set(bipa[0]))
                T = list(set(Q)&set(bipa[1]))

                print "----------------->CONJUNTO Q: ",Q
                print "----------------->CONJUNTO R: ",R
                print "----------------->CONJUNTO T: ",T

                #BUSCANDO EL MENOR VALOR PARA RESTAR A LOS VALORES DE LA MATRIZ QUE NO ESTAN EN R NI EN T
                
                matrizTemp = deepcopy(matriz)
                puntXTemp = puntX[:]
                puntYTemp = puntY[:]

                cotx = 0
                for i in R:
                    num = bipa[0].index(i)
                    matrizTemp.pop(num-cotx)
                    puntXTemp.pop(num-cotx)
                    cotx+=1

                coty = 0
                for j in T:
                    num = bipa[1].index(j)
                    print "num problema: ",num
                    print "Matriz: ",matrizTemp
                    for k in matrizTemp:
                        k.pop(num-coty)
                    puntYTemp.pop(num-coty)
                    coty+=1
                    
                print "--->BIPARTICION: ",bipa
                print "--->MATRIZ: ",matrizTemp
                print "--->PUNTAJE CAMBIO X: ",puntXTemp
                print "--->PUNTAJE CAMBIO Y: ",puntYTemp

                menor = 0
                for i in range(len(puntXTemp)):
                    menor = menor + puntXTemp[i]
                for i in range(len(puntYTemp)):
                    menor = menor+puntYTemp[i]
                    
                for i in range(len(matrizTemp)):
                    for j in range(len(matrizTemp[0])):
                        suma = puntXTemp[i]+puntYTemp[j]-matrizTemp[i][j]
                        print "SUMA DE LOS VALORES (%r+%r)-%r : %r" %(puntXTemp[i],puntYTemp[j],matrizTemp[i][j],suma)
                        if(suma<menor):
                            menor = suma
                print "...............................................>VALOR MENOR A OPERAR",menor

                #RESTANDO 'menor' A LOS VALORES CORRESPONDIENTES DEL CONJUNTO X Y SUMANDOLO A LOS CORRESPONDIENTES DE Y
                
                for i in range(len(puntX)):
                    num = bipa[0][i]
                    if(not(num in R)==True):
                        puntX[i]-=menor
                for i in range(len(puntY)):
                    num = bipa[1][i]
                    if(num in T):
                        puntY[i]+=menor
                print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                print "BIPARTICION: ",bipa
                print "MATRIZ: ",matriz
                print "Emparejamiento: ",camino[1]
                print "PUNTAJE X: ",puntX
                print "PUNTAJE Y: ",puntY
                return self.IAH(bipa,matriz,camino[1],puntX,puntY)

                        
                    
                
            
            

        def MatrizBiparticion(self,matriz):
            inicio = (len(matriz)/2)
            matrizN = []
            for i in range(inicio):
                temp = []
                for j in range(inicio):
                    temp.append(matriz[i][inicio+j])
                matrizN.append(temp)
            return matrizN
            
        
        def algoritmoHungaro(self,matriz,bipa):
            if((len(matriz[0])!=len(matriz)) or self.esBipartito==False):
                return "Error"
            else:
                puntX = []
                puntY = []
                for i in self.MatrizBiparticion(matriz):
                    puntX.append(max(i))
                    puntY.append(0)
                print "MATRIZ INICIAL: ",self.MatrizBiparticion(matriz)
                print "PUNTOS INICIALES X: ",puntX
                print "PUNTOS INICIALES Y: ",puntY
                return self.IAH(bipa,self.MatrizBiparticion(matriz),[],puntX,puntY)
                
        
        
        
        

        












        
