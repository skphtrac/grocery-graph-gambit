import random
from random import choices
from random import randint
import numpy as np

from layout import Store




class Customer:

    def __init__(self):

        self.household = self.choose_household()
        self.shopping_type = self.choose_shopping_type()
        self.choose_segment()
        self.shopping_amount = self.calc_shopping_amount(self.household, self.shopping_type)

        self.shopping_list = []
        self.fill_shopping_list(self.shopping_list)


        self.print_customer()        
    


    def choose_household(self):
        # 1 Person household, prob = 42.3%
        # 2 Person household, prob = 33.2%
        # 3 Person household, prob = 11.9%
        # 4 Person household, prob = 9.1%
        # 5+ Person household, prob = 3.5%
        # source: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Haushalte-Familien/Tabellen/1-1-privathaushalte-haushaltsmitglieder

        population = [1,2,3,4,5]
        weights = [0.423, 0.332, 0.119, 0.091, 0.035]
        return choices(population, weights)[0]


    def choose_shopping_type(self):
        # shopping type (planned product amount):
        # spontaneous purchase (2-3), daily purchase (4-12), weekly purchase (13-25), sepcial offer (1)

        population = [randint(1 ,3), randint(3, 12), randint(12, 25), 0]
        weights = [0.45, 0.3, 0.2, 0.05]
        return choices(population, weights)[0]


    def choose_segment(self):

        if(self.shopping_type > 3):
            self.prefered_segment = "no prefered segment"
        else:            
            population = ['Lebensmittel', 'Getränke']
            weights = [0.5, 0.5]
            self.prefered_segment = choices(population,weights)[0]


    def calc_shopping_amount(self, household_mlt, type_amount):

        if type_amount == 0:
            return 1
        else:
            return household_mlt * type_amount
    

    def fill_shopping_list(self, sl):

        for _ in range(self.shopping_amount):
            sl.append(random.choice(Store()._assortment[random.choice(list(Store()._assortment))]))



    def print_customer(self):
        print( '\n' 'customer values: ' '\n' '-------------------')
        print('household:               ' + str(self.household))
        print('shopping type :          ' + str(self.shopping_type))
        print('prefered segment:        ' + str(self.prefered_segment))
        print('final shopping amount:   ' + str(self.shopping_amount))
        print( '\n' 'shopping list: ' '\n' '-------------------')
        print(*self.shopping_list, sep='\n')





class Shopping_sequence:

    def __init__(self, customer):
        self.customer = customer

        
    
    def start_sequence(self):

        self.look()
        self.evaluate()
        self.decide

    
    def look(self):
        #was sucht kunde?
            #aktuellen Knotenpunkt bestimmen
            #erreichbare segmente von diesem knotenpunkt aus

        return null

    def evaluate(self):
        # ist ein produkt von liste von hier erreichbar?
            #produkte auf einkaufsliste durchschauen
            #mit erreichbaren Produkten vergleichen (bei strings am besten "is" anstatt "==")

            #spontankauf? von geplanter einkaufsmenge abhängig machen und bei jedem knotenpunkt mit kleiner Wahrscheinlichkeit entscheiden lassen, ob ein ungeplantes produkt in den korb gelegt werden soll

        # welche knotenpunkte sind von hier erreichbar
            # was ist der beste nächste schritt?
                #wahrscheinlichkeiten, "man geht lieber nach rechts als links" 

        return null


    def decide(self):
        #Mögliche entscheidung treffen, wurde ein produkt gefunden?
            # ja -> produkt von liste streichen?
            # nein -> weitergehen, wohin? mögliche knotenpunkte/wahrscheinlichkeiten der knotenpunkte abwägen
        
        return null






cus1 = Customer()

# ss1 = Shopping_sequence(cust1)