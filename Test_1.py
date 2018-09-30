from p2 import Graph
import itertools

vertex1 = ["a","b","c","d"]
edges1 = [("a","b"),("b","c"),("d","c"),("a","d")]
#edges1 = [("a","a"),("b","c"),("d","c")]

G1 = Graph(vertex1,edges1)

vertex2 = ["f","g","h","i"]
edges2 = [("f","g"),("g","h"),("i","h"),("f","i")]

G2 = Graph(vertex2,edges2)

#print "Vertex :"
#for i in G1.vertex :
#    print i
#print "------------------"
#print "Edges :"
#for j in G1.edges:
#    print j

#print G1.AdjacencyMatrix()
#print G2.AdjacencyMatrix()
#print G1.isIsomorphTo(G2)

print G1.isIsomorphTo(G2)
print G1.gradoNodo("a")
print G1.esEuleriano()



    
