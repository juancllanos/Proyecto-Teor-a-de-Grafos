from proyecto import Graph
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

print G3.distancia('a','d')
print G3.diametro()
print G3.excentricidad('a')
print G3.radio()
print G3.conectado()
print G3.esArbol()
print G3.esEuleriano()



    
