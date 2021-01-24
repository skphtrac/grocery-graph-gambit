import numpy as np
from functools import cached_property
import random

 
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


# bla = 'A'
# print(Store()._accessible_shelfs.get(bla))



      
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

#print(random.choice(Store()._assortment[random.choice(list(Store()._assortment))]))