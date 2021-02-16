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

    def get_segment(self, product):

        for key, value in self._assortment.items():
            for item in value:
                if product == item:
                    return key

        return 'product not found'


class Graph:

    def __init__(self):

        self.store_graph = nx.DiGraph()
        self.customer_store_graph = nx.DiGraph()
        
        self.store_graph.add_nodes_from(Store._layout_edges.keys())
        self.position_nodes(self.store_graph)

        for key in Store._layout_edges.keys():
            for value in Store._layout_edges.get(key):
                self.store_graph.add_edge(key,value)

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

        path_to_exit = nx.bidirectional_shortest_path(self.store_graph, path[-1], 'Exit')

        path.extend(path_to_exit)

        if 'X1' in path:
            path.remove('X1')
        if 'X2' in path:
            path.remove('X2')

        for x in range(0, len(path)-1):
            self.customer_store_graph.add_edge(path[x], path[x+1])
        
        print('Customer Path: ' + '\n' + str(path))

        self.draw_graph(self.customer_store_graph)


    def draw_store_layout(self):

        self.draw_graph(self.store_graph)


    def draw_graph(self, graph):
        nx.draw_networkx(graph, self.store_nodes_pos, node_size = 450)
        nx.draw_networkx_labels(graph, self.store_nodes_pos)
        nx.draw_networkx_edge_labels(graph, self.store_nodes_pos, edge_labels=nx.get_edge_attributes(graph,'weight'))
        plt.axis('off')
        plt.show()

# Graph().draw_store_layout()
