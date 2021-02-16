import random
import json

from layout import Store
from layout import Graph



class Customer:

    def __init__(self):

        self.shopping_amount = round(random.normalvariate(9.5, 2.0)) # mu based on: https://de.statista.com/statistik/daten/studie/303179/umfrage/gekaufte-artikel-pro-einkauf-im-lebensmitteleinzelhandel-in-deutschland
        self.shopping_list = []
        self.fill_shopping_list(self.shopping_list)
        # self.print_customer()
    

    def fill_shopping_list(self, sl):

        for _ in range(self.shopping_amount):
            sl.append(random.choice(Store()._assortment[random.choice(list(Store()._assortment))]))


    def print_customer(self):
        print( 'shopping list: ')
        print(*self.shopping_list, sep='\n')
        print('shopping list length: ' + str(len(self.shopping_list)))




class Shopping_sequence:

    def __init__(self, customer):

        self.customer = customer

        self.path = []                      # visited nodes 
        self.compare_counter = 0
        self.visited_isles = []             # path without decision-nodes

        self.shopping_cart = []             # list of products in the order they were collected

        self.current_location = 'Entrance'  
        self.walk(self.current_location)
    


    def walk(self, nxt_loc):

        self.last_location = self.current_location
        self.current_location = nxt_loc

        if self.current_location != 'X1' and self.current_location != 'X2':
            self.visited_isles.append(self.current_location)

        self.path.append(self.current_location)

        self.next_locations = Store()._layout_edges.get(self.current_location) 

        self.search_shelfes()    


    def search_shelfes(self):

        self.accessible_shelfs = Store()._accessible_shelfs.get(self.current_location) 

        if self.accessible_shelfs:

            next_prod = False

            for x in self.customer.shopping_list:           
                for y in self.accessible_shelfs:            
                    for z in Store()._assortment.get(y):    
                        if x == z:
                            self.shopping_cart.append(x)
                            next_prod = True
                            break
                    if next_prod:
                        next_prod = False
                        break
                
                self.compare_counter += 1


            for x in self.shopping_cart:
                if x in self.customer.shopping_list:
                    self.customer.shopping_list.remove(x)


        if self.customer.shopping_list:

            if self.next_locations:

                while True:

                    poss_nxt_loc = random.choice(self.next_locations)

                    if (
                        poss_nxt_loc not in self.visited_isles and 
                        poss_nxt_loc != self.last_location and
                        poss_nxt_loc != 'Exit'
                    ) :
                        self.walk(poss_nxt_loc)
                        break
                        
        # else:
        #     print('Path to last Product on List: ' + '\n' + str(self.path))
        #     Graph().draw_customer_path(self.visited_isles)

    def get_compare_count(self):
        return self.compare_counter


def create_shopping_sequences(customer_amount):

    shopping_sequences = {}

    for index in range(0, customer_amount):
        shopping_sequences['CID' + str(index)] = []
        shopping_sequences['CID' + str(index)].append(Shopping_sequence(Customer()).shopping_cart)

    with open('shopping_sequences.json', 'w') as file:
        json.dump(shopping_sequences, file, indent = 4)
    
    print('Simulated ' + str(customer_amount) + ' shopping sequences')

