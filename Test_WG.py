from WG import WeightedGraph

vertex = ['a','b','c']
edges = [(('a','b'),2),(('b','c'),5)]
G = WeightedGraph(vertex,edges)
print G.WeighMatrix()
