from WG import WeightedGraph
import random

places = ["Casa","Universidad","D1","Parque","Centro Comercial","Peluqueria","Amig@s","Novi@"]
ways = [(("Centro Comercial","D1"),5),(("D1","Casa"),10),(("Casa","Peluqueria"),20),(("Casa","Parque"),30),(("Peluqueria","Novi@"),18),(("Parque","Novi@"),35),(("Parque","Amig@s"),10),(("Novi@","Amig@s"),10),(("Amig@s","Universidad"),25)]
mapa =WeightedGraph(places,ways)
mapa.sim_comp()







    


    


