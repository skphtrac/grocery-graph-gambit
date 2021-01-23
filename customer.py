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
        self.path = []

        self.current_location = 'Entrance'  
        self.walk(self.current_location)
    


    def walk(self, next):
        self.last_location = self.current_location
        self.current_location = next

        if self.current_location != 'X1' and self.current_location != 'X2':
            self.path.append(self.current_location)

        self.next_locations = Store()._layout_edges.get(self.current_location) # Knotenpunkt "Exit" hat keine next-locations

        print('\n' + 'walked from ' + str(self.last_location) + ' to ' + str(self.current_location))

        self.search_shelfes()    


    def search_shelfes(self):

        
        if self.customer.shopping_list:

            #erreichbare segmente von diesem knotenpunkt aus
            self.accessible_shelfs = Store()._accessible_shelfs.get(self.current_location)

            # ist ein produkt von liste von hier erreichbar?
            if self.accessible_shelfs:

                #produkte auf einkaufsliste durchschauen
                print('checking shelfes: ')
                for x in self.customer.shopping_list:
                    for y in self.accessible_shelfs:
                        for z in Store()._assortment.get(y):
                            if x is z:
                                print('Found Product: ' + str(x))
                                # product von liste streichen
                                self.customer.shopping_list.remove(x)
                                # später graphen gewichten
                
                
                #spontankauf? von geplanter einkaufsmenge abhängig machen und bei jedem knotenpunkt mit kleiner Wahrscheinlichkeit entscheiden lassen, ob ein ungeplantes produkt in den korb gelegt werden soll

            #sucht kunde noch nach produkten?
            if self.customer.shopping_list:

                print('remaining shopping list: ' + str(self.customer.shopping_list))

                # welche knotenpunkte sind von hier erreichbar
                if self.next_locations:

                    while True:
                        poss_nxt_loc = random.choice(self.next_locations)

                        print('possible next location: ' + str(poss_nxt_loc))
                        print(self.path)
                        print('remaining shopping list: ' + str(self.customer.shopping_list))
                        print('current location: ' + str(self.current_location))
                        
                        if (
                            poss_nxt_loc not in self.path and 
                            poss_nxt_loc != self.last_location and
                            poss_nxt_loc != 'Exit'
                        ) :

                            self.walk(poss_nxt_loc)
                            break

                        
                        elif (
                            (self.current_location == 'X1' or self.current_location == 'X2') and
                            poss_nxt_loc not in self.path and 
                            poss_nxt_loc != self.last_location and
                            poss_nxt_loc != 'Exit'
                        ) :
                            print('ERROR')
                            print(self.path)
                            print('remaining shopping list: ' + str(self.customer.shopping_list))
                            print('current location: ' + str(self.current_location))
                            #self.walk(poss_nxt_loc)
                            break
                        

            else:
                print('Shopping list empty, go to exit')
                print(self.path)
                #self.go_to_exit(self.current_location)

 


    def decide(self):
        #Mögliche entscheidung treffen, wurde ein produkt gefunden?
            # ja -> produkt von liste streichen?
            # nein -> weitergehen, wohin? mögliche knotenpunkte/wahrscheinlichkeiten der knotenpunkte abwägen
                # letzten knotenpunkt speichern, somit prüfen, wo man zuletzt war um so stets vorwärts in eine richutng zu gehen
        return None

    def go_to_exit(self, current_location):
        return None
        # finde den stellsten ausgang vom Knotenpunkt "current location" aus


cus1 = Customer()

ss1 = Shopping_sequence(cus1)



# test = Store()._accessible_shelfs.get('Entrance')
# # print(test)

# # for x in test:
# #     print(Store()._assortment.get(x))

# for x in cus1.shopping_list:
#     for i in test:
#         for y in Store()._assortment.get(i):
#             if x is y:
#                 print('Found Product: ' + str(x))


