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
            
            else:
                s = set()
                r = set(u)
                g = set(self.vertex)
                g.remove(u)
                distance = {}
                distance[u] = 0
                while (len(r) != 0):
                    r_temp = r
                    for i in r_temp:
                        if i in r:
                            N = set()
                            if i == v:
                                return distance[i]
                            for j in self.vertex:
                                if j in g:
                                    if (i,j) in self.edges or (j,i) in self.edges:
                                        N.add(j)
                                        g.remove(j)
                                        distance[j] = distance[i]+1
                                    else:
                                        distance[j] = -1
                            r = r.union(N)
                            r.remove(i)
                            s.add(i)
                return distance[v]
        else:
            return "Error"
        
    
    
    def diametro(self):
        P = set(itertools.combinations(self.vertex,2))
        max = 0
        for i in P:
            valor = self.distancia(i[0],i[1])
            if(valor == -1):
                return -1
            elif(valor>max):
                max = valor
        return max 
            
            
    def excentricidad(self,n):
        valor = 0
        for i in self.vertex:
            dis = self.distancia(n, i)
            if(dis==-1):
                return -1
            elif(dis>valor):
                valor = dis
        return valor
    
    def radio(self):
        min = len(self.vertex)
        for i in self.vertex:
            valor = self.excentricidad(i)
            if(valor== -1):
                return -1
            elif(valor<min):
                min = valor
        return min
    
    
    def conectado(self):
        P = set(itertools.combinations(self.vertex,2))
        for i in P:
            valor = self.distancia(i[0],i[1])
            if(valor == -1):
                return False
            else:
                return True
            
            
    def esArbol(self):
        if(len(self.edges)==len(self.vertex)-1 and self.conectado()==True):
            return True;
        else:
            return False

    def gradoNodo(self,n):
        contador = 0
        for i in self.edges:
            if((n in i)==True and not((n,n)in self.edges)):
                contador+=1
        return contador

    def esEuleriano(self):
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
        for i in newVertex:
            if(self.gradoNodo(i)%2 != 0):
                valor = False
        if (self.conectado==False):
            valor = False
        return valor
            
                        

        
