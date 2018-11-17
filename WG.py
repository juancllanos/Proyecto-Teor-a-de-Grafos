# -*- coding: utf-8 -*-
import random


class WeightedGraph(object):
    

    def __init__(self,N,E):
        v = True
        #Creamos una variable booleana
        for i in E:
            #Iteramos sobre los lados para verificar que todos los nodos de estos estan en N.
            for j in i[0]:
                #Tomamos la tupla del lado.
                if j in N:
                    v = v and True
                    #Verificamos que cada nodo de la tupla esta en N y le cambiamos el valor a 'v'.
                else :
                    v = v and False
                    #Si hay un nodo que no existe 'v' es falso.
        if v == False:
            print("Error")
        #Si 'v' llega a quedar como falso quiere decir que hubo un nodo de los lados de E no estaba en N, luego
        #imprime error.
        else:
        #Si todos los nodos estan entonces crea el grafo con N y con E.
            self.N = N
            self.E = E

    def Dijkstra(self,u,v):
        if u == v:
            return 0
        # Si u y v son el mismo nodo retorna cero.
        s = [u]
        d = {}
        d[u] = 0
        path = {}
        #Creamos s (Conjunto de nodos visitados) y creamos d( diccionario de distancias).
        for i in self.N:
            p = False
            c=0
            for j in self.E:
                if (u,i) == j[0] or (i,u) == j[0]:
                    c = j[1]
                    p = p or True
                else:
                    p = p or False
            if p == True:
                d[i] = c
                path[i] = u
            else:
                d[i] = -1
                path[i] = ''
            
        # Aca revisamos todos los nodos partiendo de 'u' , agregamos su distancia respectiva al diccionario
        # y tambien el camino hasta esos nodos.

        cont = 1
        while len(s) != len(self.N):
            #print "While #",cont
            q = list(set(self.N)-set(s))
            #print "q = %s" %(q)
            m = ''
            mini = 0
            for j in self.E:
                mini = mini + j[1]
            for i in q:
                #print "BUSCANDO mini :",i,"--" ,d[i]
                if d[i]<=mini and d[i] != -1:
                    mini = d[i]
                    m = i
            #print "m = %s y mini = %i" %(m,mini) 
            s.append(m)
            #En este paso se busca el nodo de distancia minima (mini) que no esta en s, agregamos su distancia y luego
            # agregamos el nodo (m).
            if s == self.N:
                break
            #print " S = ",s, "S con mini"
            b = list(set(self.N)-set(s))
            #Sacamos como un s' para sacar la distancia de m a los nodos que no estan en s.
            #print "V(G) - S =",b
            for i in b:
                p = False
                c=0
                for j in self.E:
                    if (m,i) == j[0] or (i,m) == j[0]:
                        c = j[1]
                        p = p or True
                    else:
                        p = p or False
                # En este for vemos si el nodo i es vecino de m, si es vecino tomamos el peso del lado
                # como c y p lo volvemos verdadero porque es vecino, si no entonces p es falso.
                if p == True and (d[i]>d[m]+c or d[i] == -1):
                    d[i] = d[m]+c
                    path[i] = path[m] + ' -> ' +m
                # Si i es vecino de m y la distancia de m mas el peso del lado que lo conecta con i es
                # menor que la disancia que tiene i, o si la distancia de i es infinito entonces actualiza
                # la distancia y el camino.
                elif p == True and (d[i]<=d[m]+c or d[i] == -1):
                    d[i] = d[i]
                    path[i] = path[i]
                # Si i es vecino y la distancia que tiene i es menor que la distancia que tiene m mas el peso
                # del lado que lo conecta con i, entonces se deja el peso de i quieto y el camino tambien.
                else:
                    if d[i] != -1:
                        d[i] = d[i]
                    else:
                        d[i] = -1
                #Si no es vecino entonces se deja su distancia igual.
            cont = cont +1
        for i in path.keys():
            path[i] = path[i] +" -> "+i
        #print "Camino : ",path[v] , ' | ', "Path ", path
        #print "Distancia total : ",d[v]
        return (path[v],d[v])

 
    def simulacion(self,u,v,t):
        # Recibimos el punto inicial, punto final y el tiempo.
        x = 0
        if "am" in t:
            if len(t) == 3:
                if 1 <= int(t[0]) <= 5:
                    print "   Es muy temprano, se aconseja salir mas tarde."
                    new_ways = []
                    for i in self.E:
                        j = (i[0],i[1]*0.5)
                        new_ways.append(j)
                    new_graph = WeightedGraph(self.N,new_ways)
                    #Creamos un nuevo grafo con los mismos lugares y lados pero con tiempos diferentes.
                    print "    Estos son los nuevos tiempos de los caminos :"
                    self.printE(new_graph.E)
                    #Los imprimimos para ver como cambiaron.
                    x = new_graph.Dijkstra(u,v)
                    #Le damos nuevo valor a x, con camino y tiempo.

                if 6 <=int(t[0])<=9:
                    print "   Vias con flujo normal "
                    x = self.Dijkstra(u,v)
                    #Aca si es hora normal se deja con los pesos por defecto
                
            if len(t) == 4:
                print "   Vias con flujo normal, cuidsese del sol."
                x = self.Dijkstra(u,v)
        #Aca vemos en que hora se encuentra, si es muy temprano entonces se demora la mitad del tiempo, si
                
        if "pm" in t:
            if len(t) == 3:
                if 1 <= int(t[0]) <= 3:
                    print "   Las vias estan con flujo normal, mucho cuidado con el sol"
                    x = self.Dijkstra(u,v)

                if 4 <= int(t[0]) <= 7:
                    print "   Hora pico, vias demoradas."
                    new_ways = []
                    for i in self.E:
                        j = (i[0],i[1]*random.randint(1,3))
                        new_ways.append(j)
                    new_graph = WeightedGraph(self.N,new_ways)
                    print "    Estos son los nuevos tiempos de los caminos :"
                    self.printE(new_graph.E)
                    x = new_graph.Dijkstra(u,v)
                    
                if 8 <= int(t[0]) <=9:
                    print "   Las vias estan despejadas pero es muy tarde. Se aconseja no salir, en caso de que lo haga, maneje con cuidado."
                    x = self.Dijkstra(u,v)
            if len(t) == 4:
                print "   ¡ Es muy tarde !, se aconseja no salir."
                new_ways = []
                for i in self.E:
                    j = (i[0],i[1]*0.5)
                    new_ways.append(j)
                new_graph = WeightedGraph(self.N,new_ways)
                print "    Estos son los nuevos tiempos de los caminos :"
                self.printE(new_graph.E)
                x = new_graph.Dijkstra(u,v)
        #Algo similar pasa a la hora "am", ya que si se encuentra en hora pico el tiempo puede aumentar.
        # Si ya es muy tarde pasa lo mismo como si fuese muy temprano, se demora la mitad.

            return x
        #Retorna la tupla (camino, tiempo)

    def printE(self,a):
        for i in a:
            print " ",i

    def sim_comp(self):
        print "Estos son los posibles destinos :"
        self.printE(self.N)
        print "Estas son las vias. Formato((inicio,destino), tiempo en minutos)"
        self.printE(self.E)
        print "Ingrese su lugar de inicio : "
        a = raw_input()
        print "Ingrese su lugar de destino : "
        b = raw_input()
        print "Ingrese a la hora que solicita la ruta. Solo ingrese hora, no minutos, además indique si es 'am' o 'pm'."
        print "    Ejepmlo : 12am, 1pm, 3am, 4am, 5pm"
        c = raw_input()
        x = self.simulacion(a,b,c)
        print "Camino mas rapido :"
        print x[0]
        print "Tiempo en minutos :"
        print x[1]
        print "--- Buen viaje. Use proteccion, reflectivos y sobretodo respeste las señales de transito. ---"
        #Esta funcion solo recibe los lugares del usuario y le hace la simulacion, despues eso lo retorna.
        





         
            
"""
    def WeighMatrix(self):
        matrix = []
        #Creamos la matriz de pesos, inicialmente vacia.
        for i in self.N:
        #Iteramos sobre los nodos para sacar los pesos de los lados a los que es adyacente.
            temp = []
            #Esta lista contendrá esos pesos.
            for j in self.N:
                #Iteramos nuevamente sobre los nodos para saber a cules 'i' es vecino.
                var = False
                #Creamos una variable booleana para saber si existe el lado que une a 'i' con 'j'.
                for k in self.E:
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

"""




    
