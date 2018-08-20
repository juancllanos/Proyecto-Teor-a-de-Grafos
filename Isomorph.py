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
            print "Error"
        else:
            self.vertex = vertex
            self.edges = edges

            
    def AdjacencyMatrix(self):
        AM = []
        for i in self.vertex:
            A = []
            print "i =",i
            for j in self.vertex:
                print "j =" , j
                if (i,j) in self.edges or (j,i) in self.edges:
                    A.append(1)
                else:
                    A.append(0)
            print A
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



