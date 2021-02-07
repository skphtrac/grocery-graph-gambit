import json
import math
import collections
import numpy as np
from shopping_sequence_simulation import Customer
# from layout import Store



with open('weighted_graph.json') as wg:
    wg = json.load(wg)

matrix = np.matrix(wg['adjacent_matrix'])



class Optimization:

    def __init__(self, unsorted_list):

        self.dupl = [item for item, count in collections.Counter(unsorted_list).items() if count > 1] # duplicate products, are readded at the end of optimization

        self.usl = list(set(unsorted_list))

        self.bonds = {}
        self.bonds['bonds'] = [] # dict with lists of found connected products with high edge weights

        self.pair_max_val = np.quantile(matrix, 0.90) # value determines when edge weights are no longer high enough to make assumptions to add new product connections
        self.con_max_val = np.quantile(matrix, 0.70) # value determines when edge weights are no longer high enough to make assumptions to order existing product connections

        self.find_bonds()

        # if self.usl:
        #     self.connect_leftovers()

        # if len(self.bonds['bonds']) > 1:
        #     self.connect_bonds()

        if self.dupl:
            self.reinsert_duplicates()

        # for lists in self.bonds['bonds']:
        #     for value in lists:
        #         print(Store().get_segment(value))
            
        #     print('\n')



   
    def find_bonds(self):

        while matrix.max() > self.pair_max_val:
            
            stop = False
        
            pAind = math.floor(matrix.argmax()/len(matrix))
            pBind = matrix.argmax()%len(matrix)            

            for value in self.bonds['bonds']: # check if highest edge weight connects previously added product and product from unsorted product list
                
                if wg['products'][pAind] == value[-1] and wg['products'][pBind] in self.usl:

                    value.append(wg['products'][pBind])
                    self.usl.remove(wg['products'][pBind])
                    matrix[pAind, pBind] = 0
                    stop = True
                    break

                elif wg['products'][pAind] in self.usl and wg['products'][pBind] == value[0]:
                    value.insert(0, wg['products'][pAind])
                    self.usl.remove(wg['products'][pAind])
                    matrix[pAind, pBind] = 0
                    stop = True
                    break

            if stop:
                continue



            if len(self.bonds['bonds']) > 1: # check if heighest edge weight connects two previously added products

                for index, value in enumerate(self.bonds['bonds']):

                    for x in range(index+1, len(self.bonds['bonds'])-1):

                        if wg['products'][pAind] == value[-1] and wg['products'][pBind] == self.bonds['bonds'][x][0]: 
                            
                            value.extend(self.bonds['bonds'][x])
                            self.bonds['bonds'].remove(self.bonds['bonds'][x])
                            matrix[pAind, pBind] = 0
                            stop = True
                            break
                
                if wg['products'][pAind] == self.bonds['bonds'][-1][-1] and wg['products'][pBind] == self.bonds['bonds'][0][0]:

                    self.bonds['bonds'][-1].extend(self.bonds['bonds'][0])
                    self.bonds['bonds'].remove(self.bonds['bonds'][0])
                    matrix[pAind, pBind] = 0
                    stop = True


            if stop:
                continue



            if wg['products'][pAind] in self.usl and wg['products'][pBind] in self.usl: # check if highest edge weight connects two products from unsorted product list

                new_pair = [wg['products'][pAind], wg['products'][pBind]]
                self.bonds['bonds'].append(new_pair)
                self.usl.remove(wg['products'][pAind])
                self.usl.remove(wg['products'][pBind])

                print(matrix[math.floor(matrix.argmax()/len(matrix)),matrix.argmax()%len(matrix)])
            
            matrix[pAind, pBind] = 0
        
        print('\n' + 'Restliste: ' + str(self.usl))
        print('\n' + 'Paare: ' + str(self.bonds))
        print(matrix.max())


        if len(self.bonds['bonds']) == 0:
            print('Edge weights too low to make assumptions')
         


    def connect_leftovers(self): # find highest edge weight between leftover products and existing product bonds

        matrix = np.matrix(wg['adjacent_matrix']) # reset matrix values

        for x in range(0, len(self.usl)):

            highest_weight = 0
            listA = []
            listB = []

            for item in self.usl:

                for value in self.bonds['bonds']:

                    if matrix[wg['product_ids'][item], wg['product_ids'][value[0]]] > highest_weight:

                        listA = item
                        listB = value
                        highest_weight = matrix[wg['product_ids'][item], wg['product_ids'][value[0]]]
                    
                    if matrix[wg['product_ids'][value[-1]], wg['product_ids'][item]] > highest_weight:

                        listA = value
                        listB = item
                        highest_weight = matrix[wg['product_ids'][item], wg['product_ids'][value[0]]]
            
            if(highest_weight > self.con_max_val):
                if isinstance(listB, str):
                    self.bonds['bonds'].remove(listA)
                    self.usl.remove(listB)
                    listA.append(listB)
                    self.bonds['bonds'].append(listA)

                elif isinstance(listA, str):
                    self.bonds['bonds'].remove(listB)
                    self.usl.remove(listA)
                    listB.insert(0, listA)
                    self.bonds['bonds'].append(listB)
        
        print('\n' + 'Restliste: ' + str(self.usl))
        print('\n' + 'Paare: ' + str(self.bonds))



    def connect_bonds(self): # find heighest edge weights between existing product bonds

        matrix = np.matrix(wg['adjacent_matrix']) # reset matrix values

        for x in range(0, len(self.bonds['bonds'])-1):

            highest_weight = 0
            listA = []
            listB = []
            
            for index, value in enumerate(self.bonds['bonds']):

                for x in range(index+1, len(self.bonds['bonds'])-1):
                    
                    if matrix[wg['product_ids'][value[-1]], wg['product_ids'] [self.bonds['bonds'][x][0] ]] > highest_weight:
                        
                        listA = value
                        listB = self.bonds['bonds'][x]
                        highest_weight = matrix[wg['product_ids'][value[-1]], wg['product_ids'] [self.bonds['bonds'][x][0] ]]

            
            if matrix[wg['product_ids'][self.bonds['bonds'][-1][-1]], wg['product_ids'][self.bonds['bonds'][0][0]]] > highest_weight:

                listA = self.bonds['bonds'][-1]
                listB = self.bonds['bonds'][0]
                highest_weight = matrix[wg['product_ids'][self.bonds['bonds'][-1][-1]], wg['product_ids'][self.bonds['bonds'][0][0]]]


            if highest_weight > self.con_max_val and listA in self.bonds['bonds'] and listB in self.bonds['bonds']:

                self.bonds['bonds'].remove(listA)
                self.bonds['bonds'].remove(listB)
                listA.extend(listB)
                self.bonds['bonds'].append(listA)
        
        print('\n' + 'Restliste: ' + str(self.usl))
        print('\n' + 'Paare: ' + str(self.bonds))
        print('\n' + 'sorted lists: ' + str(len(self.bonds['bonds'])))



    def reinsert_duplicates(self):
        
        for item in self.dupl:
            for lists in self.bonds['bonds']:
                for index, value in enumerate(lists):
                    if item == value:
                        lists.insert(index, item)
                        break




opt = Optimization(Customer().shopping_list)



