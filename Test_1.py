from proyecto import Graph
from proyecto import WeightedGraph
import itertools

vertex1 = ["a","b","c","d"]
edges1 = [("a","b"),("b","c"),("d","c"),("a","d")]

G1 = Graph(vertex1,edges1)

vertex2 = ["f","g","h","i"]
edges2 = [("f","g"),("g","h"),("i","h"),("f","i")]

G2 = Graph(vertex2,edges2)

vertex3 = ['a','b','c','d','e','f']
edges3 = [('a','b'),('a','f'),('b','c'),('b','e'),('c','d'),('c','f'),
          ('d','e'),('f','e')]

G3 = Graph(vertex3,edges3)

vertex4 = ['a','b','c','d','e']
edges4 = [('a','b'),('c','b'),('d','e')]

G4 = Graph(vertex4,edges4)

##print G3.distancia('a','d')
##print G3.diametro()
##print G3.excentricidad('a')
##print G3.radio()
##print G3.conectado()
##print G3.esArbol()
##print G3.esEuleriano()
##print G4.esBipartito()
##print G4.Biparticion()
##print G4.caminoAumentador()


vertex5 = ['x1','x2','x3','y1','y2','y3']
edges5 = [(('x1','y1'),4),(('x1','y2'),7),(('x1','y3'),16),
          (('x2','y1'),1),(('x2','y2'),2),(('x2','y3'),3),
          (('x3','y1'),9),(('x3','y2'),7),(('x3','y3'),13),]

g5 = WeightedGraph(vertex5,edges5)
##print g5.WeightMatrix()
##print g5.vecindario('d')
##print g5.esBipartito()
##print g5.Biparticion()
##print g5.algoritmoHungaro(g5.WeightMatrix(),g5.Biparticion())

vertex6 = ['x1','x2','x3','x4','x5','y1','y2','y3','y4','y5']
edges6 = [(('x1','y1'),4),(('x1','y2'),4),(('x1','y3'),4),(('x1','y4'),3),(('x1','y5'),6),
          (('x2','y1'),1),(('x2','y2'),1),(('x2','y3'),4),(('x2','y4'),3),(('x2','y5'),4),
          (('x3','y1'),1),(('x3','y2'),4),(('x3','y3'),5),(('x3','y4'),3),(('x3','y5'),5),
          (('x4','y1'),5),(('x4','y2'),6),(('x4','y3'),4),(('x4','y4'),7),(('x4','y5'),9),
          (('x5','y1'),5),(('x5','y2'),3),(('x5','y3'),6),(('x5','y4'),8),(('x5','y5'),3)]

g6 = WeightedGraph(vertex6,edges6)
print g6.algoritmoHungaro(g6.WeightMatrix(),g6.Biparticion())



    
