import numpy as np
from functools import cached_property
import random

 
class Store():
    _assortment = {
        "MoPro": [
            "Meggle, gesalzen",
            "Arla, Kaergarden, ungesalzen",
            "Kerrygold, Irische Butter",
            "Zott, Sahnejoghurt, Erdbeer",
            "Froop, Fruchjoghurt, Pfirsch-Maracuja",
            "Elinas, Griechischer Joghurt, natur",
            "Salakis, Schafskäse",
        ],
        "Fleisch": [
            "GardenGourmet, Veggie-Filetstreifen",
            "Valess, Veggie-Schnitzel",
            "LikeMeat, Veggie-Schinkenwurst",
            "Die Echte, Veggie-Paprikawurst",
            "Rügenwalder, Veggie-Salami"
        ],
        "FG-nass": [
            "Landfreude Bratkartoffeln",
            "Henglein, Kartoffel-Gnocchi"
        ],
        "N-Alk": [
            "Valensina, Orange",
            "Hohes C, Milde Orange",
            "Coca-Cola, Fanta",
            "Coca-Cola, Sprite",
            "Coca-Cola, Cola",
            "HappyDay, Apfelsaft"
        ],
        "Alk": [
            "Radeberger, Pilsener",
            "Krombacher, Radler",
            "Becks, Gold",
            "Stauder, alkoholfrei",
            "Freixenet, Carta Nevada",
            "Rotkäppchen, rot",
            "Schneider, Riesling"
            "Gallo Family, Primitivo"
            "Barcadi, Razz",
            "Absolut"
        ],
        "Tee/Kaffe": [
            "Dallmeyer, Prodomo",
            "Jacobs, Krönung",
            "Melitta, Auslese",
            "Eduscho, Gala Nr. 1",
            "Teekanne, Ländertee, Italienische Limone",
            "Meßmer, Grün",
            "Nestlé, Nesquik"
        ],
        "FG-TK": [
            "McCain, Pommes 1-2-3",
            "Dr. Oetker, Ristorante, Quattro Formaggi",
            "Agrarfrost, Kroketten",
            "Wagner, Margarita",
            "Bördegold, Rösti-Ecken"
        ], 
        "Eis": [
            "Langnese, Königsrolle",
            "Cornetto, Classico",
            "Magnum, Classic",
            "Langnese, Dolomiti",
            "Nestlé Schöller, Sandwich"
        ],
        "Milch": [
            "Bärenmarke, Haltbare Milch",
            "Weihenstephan",
            "Landliebe",
            "MinusL, Schmand",
            "Bärenmarke, Die Ergebiege"
        ], 
        "Drogerie": [
            "Tempo",
            "Charmin, 4lagig",
            "Zewa, Wisch-und-weg",
            "Hakle, Kamille",
            "DuschDas, For Men",
            "Nivea, Creme-Dusche",
            "Schauma, 7 Kräuter",
            "Rexona, Cobalt Dry",
            "Dove, original"
        ],
        "Presse": [
            "TV14",
            "Welt",
            "Spiegel"
        ],
        "Hygiene": [
            "Ariel, Pulver",
            "Persil, flüssig",
            "Frosch, Essigreiniger",
            "Meister Proper",
            "VIM"
        ],
        "Snacks": [
            "FunnyFrisch, ungarisch",
            "Chio, Hot Cheese",
            "Lorenz, Crunchips",
            "Pringles, Hot & Spicy",
            "Lorenz, Saltletts",
            "Katjes, Glücksgefühle",
            "Katjes, Salzige Heringe"
        ],
        "Backen": [
            "Dr. Oetker, Vanillinzucker",
            "Dr. Oetker, Backpulver",
            "Mondamin, Pfannkuchen",
            "Oreo, Cupcakes",
            "Diamant, Ciabatta"
        ],
        "FG-trocken": [
            "Knorr, Saucen, 3-Pfeffer-Sauce",
            "Maggi, Fix, Napoli",
            "Maggi, Fix, Chilli con carne",
            "Miracoli, mit Tomatensauce",
            "Kühne, Gewürzgurken"   
        ],
        "Konserven": [
            "Bonduelle, Mais",
            "Oro di Parma, Stückige Tomaten",
            "Mutti, Passierte Tomaten",
            "Bonduelle, Erbsen und Möhren, fein"
        ],
        "Gewürze/Saucen": [
            "Hela, Gewürzketchup",
            "Thomy, Delikatess-Senf, mittelscharf",
            "Heinz, Tomato-Ketchup",
            "Surig, Essig-Essenz",
            "Knorr, Knoblauch",
            "Miracel Whip",
        ],
        "Nudeln/Reis": [
            "Barilla", "Spaghetti, n. 5",
            "Buitoni, Eliche",
            "Uncle Ben's Spitzen-Lankorn-Reis",
            "Oryza, Natur-Reis",
            "Pfanni, Kartoffel-Püree"
        ],
        "Gebäck/Schokolade": [
            "Schogetten, Vollmilch",
            "Milka, Luflée",
            "Ritter Sport, Marzipan",
            "Prinzenrolle",
            "Duplo",
            "Merci",
            "Toffifee"
        ],
        "Brot/Aufstrich": [
            "Nutella",
            "Wasa, Mjölk",
            "Harry, Rosinenstuten",
            "Golden Toast, Vollkorn",
            "Brandt, Der Markenzwieback"
        ],
        "Müsli": [
            "Kellogs, Smacks",
            "Kölln, Flocken",
            "Corny, Schoko",
            "Dr. Oetker, Vitalis",
            "Nestlé, CiniMinis"
        ],
        "Backstation": [
            "Lange, Weltmeisterbrötchen",
            "Lange, Krapfen",
            "Lange, Käsebrot",
            "Lange, Donuts"
        ],
        "Obst": [
            "Bauer Heinrich, Banane",
            "Bauer Heinrich, Apfel",
            "Bauer Heinrich, Zwiebeln",
            "Bauer Heinrich, Knoblauch",
            "Bauer Heinrich, Pilze",
            "Bauer Heinrich, Blaubeeren",
            "Bauer Heinrich, Bauernsalat"
        ],
        "Wochenaktionen": [
            "Toastmann, Toaster",
            "Wollmann, Unterhemden",
            "Klemmbaumann, Sternkriegs Raumschiff"
        ]
    }
 
    _layout_edges = [
        ("start", "A", 0),
        ("A", "B", 1),
        ("B", "C", 1),
        ("C", "D", 1),
        ("D", "E", 1),
        ("E", "F", 1),
        ("F", "G", 1),
        ("G", "H", 1),
        ("H", "I", 1),
        ("B", "X1", .5),
        ("X1", "H", .5),
        ("X1", "O", .5),
        ("X1", "N", .5),
        ("X1", "K", .5),
        ("X1", "I", .5),
        ("O", "P", 1),
        ("K", "L", 1),
        ("L", "M", 1),
        ("I", "J", 1),
        ("P", "X2", .5),
        ("N", "X2", .5),
        ("M", "X2", .5),
        ("J", "X2", .5),
        ("X2", "end", 0)
    ]
    
    _layout_shelfs_by_vertices = {
        "A": [ "Brot/Aufstrich" ],
        "B": [ "Müsli" ],
        "C": [ "FG-nass" ],
        "D": [ "Fleisch" ],
        "E": [ "MoPro"],
        "F": [ "FG-TK"],
        "G": [ "Eis" ],
        "H": [ "Milch" ],
        "I": [ "Konserven", "Drogerie" ],
        "J": [ "Presse", "Hygiene"],
        "K": [ "Gewürze/Saucen", "FG-trocken" ],
        "L": [ "Nudeln/Reis" ],
        "M": [ "Backen", "Snacks" ],
        "N": [ "N-Alk", "Alk" ],
        "O": [ "Tee/Kaffee" ],
        "P": [ "Gebäck/Schokolade" ]
    }
   
      
    _layout = [
        ("start", "Brot/Auftrich"),
        ("Brot/Auftrich", "Müsli"),
        ("Müsli", "FG-nass"),
        ("Müsli", "X1"),
        ("FG-nass", "Fleisch"),
        ("Fleisch", "MoPro"),
        ("MoPro", "FG-TK"),
        ("FG-TK", "Eis"),
        ("Eis", "Milch"),
        ("Milch", "X1"),
        ("Milch", "")
    ]
    
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