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
        #Busca en el conjunto de los lados las ocurrencias de "nodo"
        for i in self.edges:
            if(nodo == i[0]):
                vecinos.append(i[1])
            elif(nodo == i[1]):
                vecinos.append(i[0])
        return vecinos


    def esBipartito(self):
        #Verifica primero si el grafo es Arbol o no
        if(self.esArbol()==True):
            return True
        #Si no es Arbol busca construir la biparticion 
        else:
            grafo = self.Biparticion()
            #Si la interseccion entre los dos conjuntos de la biparticion no es vacio, entonces no es bipartito
            if(len(set(grafo[0])& set(grafo[1]))!=0):
                return False
            else:
                return True

    def Biparticion(self):
        #listas X y Y que representan los dos conjuntos independientes
        x = []
        y = []
        #Para cada nodo en el conjunto de los nodos lo agrega a X o Y
        for i in self.vertex:
            #Si el nodo no esta en X pero si esta en Y, entonces agrega el vecindario del nodo a X
            if(not(i in x) and (i in y)):
                x = x + self.vecindario(i)
            #Si el nodo no esta en Y pero si esta en X, entonces agrega el vecindario del nodo a Y
            elif(not(i in y) and (i in x)):
                y = y + self.vecindario(i)
            #Agrega el nodo por defecto a X y su vecindario a Y
            else:
                x.append(i)
                y = y + self.vecindario(i)
        #Retorna la biparticion
        return [list(OrderedDict.fromkeys(x)),list(OrderedDict.fromkeys(y))]
        

    def findCA(self,grafo,emp,S,T,final):
        #Si el evaluador es "True" o la longitud de S es 0 termino y retorna una lista de listas con el cubrimiento minimo y el emparejamiento maximo 
        if(len(S)==0 or final==True):
            cubrimiento = (set(T) | (set(grafo[0])-set(S)))
            return [list(OrderedDict.fromkeys(cubrimiento)),emp]
        else:
            #Evalua cada nodo de S
            for i in S:
                #Evalua el vecindario del nodo "i"
                for j in self.vecindario(i):
                    #Busca entre el emparejamiento si el nodo "j" esta saturado
                    Jsaturado = False
                    for k in emp:
                        if(j in k):
                            Jsaturado = True
                    #Si el lado (i,j) o (j,i) no esta en el emparejamiento y el nodo "j" no esta saturado
                    if((not((i,j) in emp) or not((j,i) in emp)) and Jsaturado==False):
                        #Si encuentra que el nodo "i" esta en el emparejamiento borra ese lado y agrega el encontrado (i,j) o (j,i)
                        for q in emp:
                            if(i==q[0] or i==q[1]):
                                emp.pop(emp.index(q))
                                break
                        emp.append((i,j))
                        #Actualiza el conjunto S sin el nodo "i"
                        S = []
                        for mp in grafo[0]:
                            esta = False
                            for hi in emp:
                                if(mp in hi):
                                    esta = True
                            if(esta==False):
                                S.append(mp)
                        #Llama a la funcion "findCA" para continuar con el nuevo emparejamiento y conjunto S
                        return self.findCA(grafo,emp,S,[],False)
                    #Si el nodo "j" esta saturado 
                    else:
                        #Si el nodo "j" no esta en T lo agrega al conjunto T
                        if(not(j in T)):
                            T = T+[j]
                        w = 0
                        #Busca el nodo "w" del conjunto X adyacente a "j" en el emprejamiento
                        for p in emp:
                            if(j == p[0]):
                                w = p[1]
                                break
                            elif(j== p[1]):
                                w = p[0]
                                break
                        #Si el nodo "w" no esta en S lo agrega al conjunto S 
                        if(not(w in S)):
                            S = S+[w]
            #Si no hay mas elementos del conjunto S para evaluar llama a la función con el evaluador True
            if(i==S[len(S)-1]):
                return self.findCA(grafo,emp,S,T,True)
            else:
                return self.findCA(grafo,emp,S,T,False)
        
                
                        

        
    def caminoAumentador(self):
        #Si no es bipartito retorna Error
        if(self.esBipartito==False):
            return "Error"
        #Crea la biparticion y llama a la funcion "findCA" con el grafo, el emparejamiento vacio, el conjunto S no saturado, El conjunto T vacio y un evaluador
        else:
            grafo = self.Biparticion()
            return self.findCA(grafo,[],grafo[0],[],False)


########################################################################################################################################################
class WeightedGraph(object):

    def __init__(self,vertex,edges):
        v = True
        for i in edges:
            for j in i[0]:
                if j in vertex:
                    v = v and True
                else :
                    v = v and False
        if v == False:
            print("Error")
        else:
            self.vertex = vertex
            self.edges = edges

    def WeightMatrix(self):
        matrix = []
        #Creamos la matriz de pesos, inicialmente vacia.
        for i in self.vertex:
        #Iteramos sobre los nodos para sacar los pesos de los lados a los que es adyacente.
            temp = []
            #Esta lista contendrá esos pesos.
            for j in self.vertex:
                #Iteramos nuevamente sobre los nodos para saber a cules 'i' es vecino.
                var = False
                #Creamos una variable booleana para saber si existe el lado que une a 'i' con 'j'.
                for k in self.edges:
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
        

    def vecindario(self,nodo):
        vecinos = []
        #Busca en el conjunto de los lados las ocurrencias de "nodo"
        for i in self.edges:
            if(nodo == i[0][0]):
                vecinos.append(i[0][1])
            elif(nodo == i[0][1]):
                vecinos.append(i[0][0])
        return vecinos


    def esBipartito(self):
        grafo = self.Biparticion()
        #Si la interseccion entre los dos conjuntos de la biparticion no es vacio, entonces no es bipartito
        if(len(set(grafo[0])& set(grafo[1]))!=0):
            return False
        else:
            return True


    def Biparticion(self):
        #listas X y Y que representan los dos conjuntos independientes
        x = []
        y = []
        #Para cada nodo en el conjunto de los nodos lo agrega a X o Y
        for i in self.vertex:
            #Si el nodo no esta en X pero si esta en Y, entonces agrega el vecindario del nodo a X
            if(not(i in x) and (i in y)):
                x = x + self.vecindario(i)
            #Si el nodo no esta en Y pero si esta en X, entonces agrega el vecindario del nodo a Y
            elif(not(i in y) and (i in x)):
                y = y + self.vecindario(i)
            #Agrega el nodo por defecto a X y su vecindario a Y
            else:
                x.append(i)
                y = y + self.vecindario(i)
        #Retorna la biparticion
        return [list(OrderedDict.fromkeys(x)),list(OrderedDict.fromkeys(y))]
    
    

    def IAH(self,bipa,matriz,emp,puntX,puntY):
        #Si el emparejamiento es del mismo tamaño de alguno de los conjuntos de la biparticion termina
        if(len(emp)==len(bipa[0])):
            return emp
        else:
            #Busca todos los lados cullos nodos cumplan que su suma de pesos sea igual al peso del lado 
            lados = []
            for j in range(len(puntX)):
                for h in range(len(puntY)): 
                    suma = puntX[j]+puntY[h]
                    if(suma==matriz[j][h]):
                        #Agrega el lado a la lista lados
                        lados.append((self.vertex[j],self.vertex[h+len(bipa[0])]))

            
            #Busca los nodos para generar el grafo de aumento
            Nvertex = []
            for i in self.vertex:
                for j in lados:
                    if(i in j):
                        Nvertex.append(i)
            #Crea el grafo de aumento con los nodos de "Nvertex" y los lados de "lados"
            G = Graph(list(OrderedDict.fromkeys(Nvertex)),lados)
            #Llama a la funcion "caminoAumento" para encontrar el emparejamiento maximo y cubrimiento minimo
            camino =  G.caminoAumentador()
            #Si la longitud del cubrimiento es igual a la longitud del conjunto X o Y termina
            if(len(camino[0])==len(bipa[0])):
                return camino
            #Nodos del cubrimiento 
            Q = list(OrderedDict.fromkeys(camino[0]))
            #Nodos del cumbrimeinto X & Q
            R = list(set(Q)&set(bipa[0]))
            #Nodos del cumbrimiento Y & Q
            T = list(set(Q)&set(bipa[1]))

            #BUSCANDO EL MENOR VALOR PARA RESTAR A LOS VALORES DE LA MATRIZ QUE NO ESTAN EN R NI EN T
            
            matrizTemp = deepcopy(matriz)
            puntXTemp = puntX[:]
            puntYTemp = puntY[:]

            cotx = 0
            R.sort()
            for i in R:
                num = bipa[0].index(i)
                matrizTemp.pop(num-cotx)
                puntXTemp.pop(num-cotx)
                cotx+=1

            coty = 0
            T.sort()
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
        #Dada la matriz la reorganiza para evitar los pesos "-1"
        inicio = (len(matriz)/2)
        matrizN = []
        for i in range(inicio):
            temp = []
            for j in range(inicio):
                temp.append(matriz[i][inicio+j])
            matrizN.append(temp)
        return matrizN
        
    
    def algoritmoHungaro(self,matriz,bipa):
        #Verifica que el grafo sea bipartito completo
        if((len(matriz[0])!=len(matriz)) or self.esBipartito==False):
            return "Error"
        else:
            #Crea dos listas que representan los "pesos" de cada nodo del grafo. 
            puntX = []
            puntY = []
            #Asigna los "pesos". Para X el mayor valor de los pesos de los lados y para Y 0
            for i in self.MatrizBiparticion(matriz):
                puntX.append(max(i))
                puntY.append(0)
            print "MATRIZ INICIAL: ",self.MatrizBiparticion(matriz)
            print "PUNTOS INICIALES X: ",puntX
            print "PUNTOS INICIALES Y: ",puntY
            #Llama a la funcion IAH con la biparticion, la matrtiz, el emparejamiento, los pesos de X y los de Y
            return self.IAH(bipa,self.MatrizBiparticion(matriz),[],puntX,puntY)
            
    
    
    
    

    












        
