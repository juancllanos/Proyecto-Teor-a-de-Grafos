
class Graph(object):

    def __init__(self,vertex,edges):

        self.vertex = vertex
        self.edges = edges


    def MatrixP(self):
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
                    temp.append(-1)
            matrix.append(temp)
        return matrix

    def Kruskal(self):
        subGraph = self.edges
        lados = []
        mini = self.edges[0]
        for i in self.edges:
            if mini[1] > i[1]:
                mini = i
        lados.append(mini)
        return lados
            
            
            
                        
                
            
        
