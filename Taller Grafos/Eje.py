from Krus import Graph


vertex = ['a','b','c','d']
edges = [(('a','b'),5),
         (('b','c'),6),
         (('c','d'),1),
         (('d','a'),8)
         ]


p1 = Graph(vertex,edges)
print(('a','b') in edges[0])
print p1.Kruskal()


