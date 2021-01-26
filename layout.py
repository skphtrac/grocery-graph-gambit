# import numpy as np
from functools import cached_property
# import random
import networkx as nx
import matplotlib.pyplot as plt
 
class Store():
    _assortment = {
        'MoPro': [
            'Meggle, gesalzen',
            'Arla, Kaergarden, ungesalzen',
            'Kerrygold, Irische Butter',
            'Zott, Sahnejoghurt, Erdbeer',
            'Froop, Fruchjoghurt, Pfirsch-Maracuja',
            'Elinas, Griechischer Joghurt, natur',
            'Salakis, Schafskaese',
        ],
        'Fleisch': [
            'GardenGourmet, Veggie-Filetstreifen',
            'Valess, Veggie-Schnitzel',
            'LikeMeat, Veggie-Schinkenwurst',
            'Die Echte, Veggie-Paprikawurst',
            'Ruegenwalder, Veggie-Salami'
        ],
        'FG-nass': [
            'Landfreude Bratkartoffeln',
            'Henglein, Kartoffel-Gnocchi'
        ],
        'N-Alk': [
            'Valensina, Orange',
            'Hohes C, Milde Orange',
            'Coca-Cola, Fanta',
            'Coca-Cola, Sprite',
            'Coca-Cola, Cola',
            'HappyDay, Apfelsaft'
        ],
        'Alk': [
            'Radeberger, Pilsener',
            'Krombacher, Radler',
            'Becks, Gold',
            'Stauder, alkoholfrei',
            'Freixenet, Carta Nevada',
            'Rotkaeppchen, rot',
            'Schneider, Riesling'
            'Gallo Family, Primitivo'
            'Barcadi, Razz',
            'Absolut'
        ],
        'Tee/Kaffee': [
            'Dallmeyer, Prodomo',
            'Jacobs, Kroenung',
            'Melitta, Auslese',
            'Eduscho, Gala Nr. 1',
            'Teekanne, Laendertee, Italienische Limone',
            'Meßmer, Gruen',
            'Nestle, Nesquik'
        ],
        'FG-TK': [
            'McCain, Pommes 1-2-3',
            'Dr. Oetker, Ristorante, Quattro Formaggi',
            'Agrarfrost, Kroketten',
            'Wagner, Margarita',
            'Boerdegold, Roesti-Ecken'
        ], 
        'Eis': [
            'Langnese, Koenigsrolle',
            'Cornetto, Classico',
            'Magnum, Classic',
            'Langnese, Dolomiti',
            'Nestle Schoeller, Sandwich'
        ],
        'Milch': [
            'Baerenmarke, Haltbare Milch',
            'Weihenstephan',
            'Landliebe',
            'MinusL, Schmand',
            'Baerenmarke, Die Ergebiege'
        ], 
        'Drogerie': [
            'Tempo',
            'Charmin, 4lagig',
            'Zewa, Wisch-und-weg',
            'Hakle, Kamille',
            'DuschDas, For Men',
            'Nivea, Creme-Dusche',
            'Schauma, 7 Kraeuter',
            'Rexona, Cobalt Dry',
            'Dove, original'
        ],
        'Presse': [
            'TV14',
            'Welt',
            'Spiegel'
        ],
        'Hygiene': [
            'Ariel, Pulver',
            'Persil, fluessig',
            'Frosch, Essigreiniger',
            'Meister Proper',
            'VIM'
        ],
        'Snacks': [
            'FunnyFrisch, ungarisch',
            'Chio, Hot Cheese',
            'Lorenz, Crunchips',
            'Pringles, Hot & Spicy',
            'Lorenz, Saltletts',
            'Katjes, Gluecksgefuehle',
            'Katjes, Salzige Heringe'
        ],
        'Backen': [
            'Dr. Oetker, Vanillinzucker',
            'Dr. Oetker, Backpulver',
            'Mondamin, Pfannkuchen',
            'Oreo, Cupcakes',
            'Diamant, Ciabatta'
        ],
        'FG-trocken': [
            'Knorr, Saucen, 3-Pfeffer-Sauce',
            'Maggi, Fix, Napoli',
            'Maggi, Fix, Chilli con carne',
            'Miracoli, mit Tomatensauce',
            'Kuehne, Gewuerzgurken'   
        ],
        'Konserven': [
            'Bonduelle, Mais',
            'Oro di Parma, Stueckige Tomaten',
            'Mutti, Passierte Tomaten',
            'Bonduelle, Erbsen und Moehren, fein'
        ],
        'Gewuerze/Saucen': [
            'Hela, Gewuerzketchup',
            'Thomy, Delikatess-Senf, mittelscharf',
            'Heinz, Tomato-Ketchup',
            'Surig, Essig-Essenz',
            'Knorr, Knoblauch',
            'Miracel Whip',
        ],
        'Nudeln/Reis': [
            'Barilla', 'Spaghetti, n. 5',
            'Buitoni, Eliche',
            'Uncle Bens Spitzen-Lankorn-Reis',
            'Oryza, Natur-Reis',
            'Pfanni, Kartoffel-Pueree'
        ],
        'Gebaeck/Schokolade': [
            'Schogetten, Vollmilch',
            'Milka, Luflée',
            'Ritter Sport, Marzipan',
            'Prinzenrolle',
            'Duplo',
            'Merci',
            'Toffifee'
        ],
        'Brot/Aufstrich': [
            'Nutella',
            'Wasa, Mjoelk',
            'Harry, Rosinenstuten',
            'Golden Toast, Vollkorn',
            'Brandt, Der Markenzwieback'
        ],
        'Muesli': [
            'Kellogs, Smacks',
            'Koelln, Flocken',
            'Corny, Schoko',
            'Dr. Oetker, Vitalis',
            'Nestle, CiniMinis'
        ],
        'Backstation': [
            'Lange, Weltmeisterbroetchen',
            'Lange, Krapfen',
            'Lange, Kaesebrot',
            'Lange, Donuts'
        ],
        'Obst': [
            'Bauer Heinrich, Banane',
            'Bauer Heinrich, Apfel',
            'Bauer Heinrich, Zwiebeln',
            'Bauer Heinrich, Knoblauch',
            'Bauer Heinrich, Pilze',
            'Bauer Heinrich, Blaubeeren',
            'Bauer Heinrich, Bauernsalat'
        ],
        'Wochenaktionen': [
            'Toastmann, Toaster',
            'Wollmann, Unterhemden',
            'Klemmbaumann, Sternkriegs Raumschiff'
        ]
    }
 
    _layout_edges = {
        'Entrance': ['A'],
        'A': ['B'],
        'B': ['C'],
        'C': ['X1'],

        'D': ['E', 'X1'],
        'E': ['F', 'D'],
        'F': ['G', 'E'],
        'G': ['H', 'F'],
        'H': ['I', 'G'],
        'I': ['X1', 'H'],

        'X1': ['L', 'O', 'P', 'D', 'I', 'J'],

        'J': ['K', 'X1'],
        'K': ['X2', 'J'],

        'L': ['M', 'X1'],
        'M': ['N', 'L'],
        'N': ['X2', 'M'],

        'O': ['X2', 'X1'],

        'P': ['Q', 'X1'],
        'Q': ['X2', 'P'],

        'X2': ['K', 'N', 'O', 'Q', 'Exit'],
        'Exit': []

    }

    # _layout_edges = [
    #     ('start', 'A', 0),
    #     ('A', 'B', 1),
    #     ('B', 'C', 1),
    #     ('C', 'D', 1),
    #     ('D', 'E', 1),
    #     ('E', 'F', 1),
    #     ('F', 'G', 1),
    #     ('G', 'H', 1),
    #     ('H', 'I', 1),
    #     ('B', 'X1', .5),
    #     ('X1', 'H', .5),
    #     ('X1', 'O', .5),
    #     ('X1', 'N', .5),
    #     ('X1', 'K', .5),
    #     ('X1', 'I', .5),
    #     ('O', 'P', 1),
    #     ('K', 'L', 1),
    #     ('L', 'M', 1),
    #     ('I', 'J', 1),
    #     ('P', 'X2', .5),
    #     ('N', 'X2', .5),
    #     ('M', 'X2', .5),
    #     ('J', 'X2', .5),
    #     ('X2', 'end', 0)
    # ]
    
    # _layout_shelfs_by_vertices = {
    #     'A': [ 'Brot/Aufstrich' ],
    #     'B': [ 'Backstation' ],
    #     'C': [ 'Müsli'],
    #     'D': [ 'FG-nass' ],
    #     'E': [ 'Fleisch' ],
    #     'F': [ 'MoPro'],
    #     'G': [ 'FG-TK'],
    #     'H': [ 'Eis' ],
    #     'I': [ 'Milch' ],
    #     'J': [ 'Konserven', 'Drogerie' ],
    #     'K': [ 'Presse', 'Hygiene'],
    #     'L': [ 'Gewürze/Saucen', 'FG-trocken' ],
    #     'M': [ 'Nudeln/Reis' ],
    #     'N': [ 'Backen', 'Snacks' ],
    #     'O': [ 'N-Alk', 'Alk' ],
    #     'P': [ 'Tee/Kaffee' ],
    #     'Q': [ 'Gebäck/Schokolade' ]
    # }

    _accessible_shelfs = {
        'Entrance': [],
        'A': [ 'Brot/Aufstrich', 'Obst' ],
        'B': [ 'Backstation', 'Obst' ],
        'C': [ 'Muesli' , 'Obst'],
        'X1': [],
        'D': [ 'FG-nass', 'Wochenaktionen' ],
        'E': [ 'Fleisch', 'Wochenaktionen'  ],
        'F': [ 'MoPro', 'Wochenaktionen' ],
        'G': [ 'FG-TK', 'Wochenaktionen' ],
        'H': [ 'Eis', 'Wochenaktionen' ],
        'I': [ 'Milch', 'Wochenaktionen' ],
        'J': [ 'Konserven', 'Drogerie' ],
        'K': [ 'Presse', 'Hygiene'],
        'L': [ 'Gewuerze/Saucen', 'FG-trocken' ],
        'M': [ 'Nudeln/Reis' ],
        'N': [ 'Backen', 'Snacks' ],
        'O': [ 'N-Alk', 'Alk' ],
        'P': [ 'Tee/Kaffee', 'Obst' ],
        'Q': [ 'Gebaeck/Schokolade', 'Obst' ],
        'X2': [],
        'Exit': []
    }


    # _layout = [
    #     ('start', 'Brot/Auftrich'),
    #     ('Brot/Auftrich', 'Müsli'),
    #     ('Müsli', 'FG-nass'),
    #     ('Müsli', 'X1'),
    #     ('FG-nass', 'Fleisch'),
    #     ('Fleisch', 'MoPro'),
    #     ('MoPro', 'FG-TK'),
    #     ('FG-TK', 'Eis'),
    #     ('Eis', 'Milch'),
    #     ('Milch', 'X1'),
    #     ('Milch', '')
    # ]
    
    # def compute_path_cost():
    
  
    # def random_sample(self, len_mu=15, len_sigma=3):
    #     return random.sample(self.flat_assortment, int(abs(random.gauss(len_mu, len_sigma))))
        
    # @cached_property
    # def flat_assortment(self):
    #     flat_assortment = []
        
    #     for category_names, category_articles in self._assortment.items():
    #         flat_assortment.extend(category_articles)
 
    #     return flat_assortment

weighted_products = {}

class Graph:

    def __init__(self):

        self.store_graph = nx.DiGraph()
        self.customer_store_graph = nx.DiGraph()

        
        
        self.store_graph.add_nodes_from(Store._layout_edges.keys())

        self.position_nodes(self.store_graph)
        self.make_store_layout()

    def position_nodes(self, graph1):

        graph1.nodes['Entrance']['pos'] = (0,0)
        graph1.nodes['A']['pos'] = (0,4)
        graph1.nodes['B']['pos'] = (0,8)
        graph1.nodes['C']['pos'] = (0,12)
        graph1.nodes['X1']['pos'] = (8,14)
        graph1.nodes['D']['pos'] = (0,16)
        graph1.nodes['E']['pos'] = (0,20)
        graph1.nodes['F']['pos'] = (10,20)
        graph1.nodes['G']['pos'] = (16,20)
        graph1.nodes['H']['pos'] = (16,18)
        graph1.nodes['I']['pos'] = (16,16)
        graph1.nodes['J']['pos'] = (16,12)
        graph1.nodes['K']['pos'] = (16,5.5)
        graph1.nodes['L']['pos'] = (12,12.5)
        graph1.nodes['M']['pos'] = (12,10)
        graph1.nodes['N']['pos'] = (12,5.5)
        graph1.nodes['O']['pos'] = (8,10)
        graph1.nodes['P']['pos'] = (4,12)
        graph1.nodes['Q']['pos'] = (4,8)
        graph1.nodes['X2']['pos'] = (10,4)
        graph1.nodes['Exit']['pos'] = (10,0)

        self.store_nodes_pos = nx.get_node_attributes(self.store_graph, 'pos')
    
    def draw_customer_path(self, path):
        
        

        path_to_exit = nx.bidirectional_shortest_path(self.store_graph, path[len(path)-1], 'Exit')
        
        for x in range(1, len(path_to_exit)):
            path.append(path_to_exit[x])

        for x in range(0, len(path)-1):
            self.customer_store_graph.add_edge(path[x], path[x+1])
        
        print('Path to Exit: ' + '\n' + str(path_to_exit))
        self.draw_graph(self.customer_store_graph)


    def make_store_layout(self):

        for x in Store._layout_edges.keys():
            for y in Store._layout_edges.get(x):
                self.store_graph.add_edge(x,y)

        # self.draw_graph(self.store_graph)


    def draw_graph(self, graph):
        nx.draw_networkx(graph, self.store_nodes_pos, node_size = 450)
        nx.draw_networkx_labels(graph, self.store_nodes_pos)
        plt.axis('off')
        plt.show()


    def add_to_weighted_product_graph(self, products):

        for x in range(0, len(products)-1):
            if products[x] in weighted_products:
                
                value_exists = False

                # prüfe, ob value schon vorhanden ist, dann nur wert erhöhen
                for key in weighted_products:
                    if key == products[x]:

                        

                        for y in range(0, len(weighted_products[key])-1):
                            
                            if len(weighted_products[key])>2:
                                print(weighted_products[key])
                                if weighted_products[key][0][y] == products[x+1]:
                                    value_exists = True
                                    weighted_products[key][0][y+1] += 1
                                    
                            else:
                                if weighted_products[key][y] == products[x+1]:
                                    value_exists = True
                                    weighted_products[key][y+1] += 1
                                    
                        break
                            

                # prüfe, ob value schon vorhanden ist, dann nur wert erhöhen
                # for y in range(0, len(weighted_products[products[x]])):
                    

                    


                #     product2 = products[x+1]
                #     product1 = str(products[x])
                #     print(weighted_products[product1][y][0])
                    
                #     # if weighted_product == product2:
                        
                #     #     print('ssssssssssssssssssssssss')

                #     #     # value_exists = True
                #     #     # weighted_products[products[int(x)]][int(y)][1] += 1


                # füge key mit folgendem artikel als value hinzu
                if not value_exists:

                    new_value = [products[x+1], 1]
                    weighted_products[str(products[x])].append(new_value)

            else:
                weighted_products[products[x]] = [products[x+1], 1]

        print(weighted_products)

            


    def draw_product_graph(self, products):

        product_graph = nx.DiGraph()
        product_graph.add_nodes_from(products)

        for x in range(0, len(products)-1):
            product_graph.add_edge(products[x], products[x+1])
        
        nx.draw_networkx(product_graph, pos=None, node_size = 100)
        plt.axis('off')
        plt.show()



gle = ['B',3]
gleb = ['C', 0]

bla = {}
bla['A'] = gle, gleb
bla['B'] = gleb
bla['C'] = ['D', 2]


ble = ['A', 'B', 'C']


for index in range(0, len(ble)-1):

    for key in bla:
        if key == ble[index]:
            for y in range(0, len(bla[key])-1):

                if len(bla[key])>1:
                    if bla[key][0][y] == ble[index]:
                        bla[key][0][y+1] += 1
                else:
                    if bla[key][y] == ble[index]:
                        bla[key][y+1] += 1

                




# for key1 in ble:
#     print(key1)

#     for key2 in bla:
#         if key1 == key2:
#             # print(bla[key2])
#             print(bla[key2][0])




print(bla)