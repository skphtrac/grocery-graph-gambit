import json
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from customer import Customer


with open('weighted_graph.json') as wg:
    wg = json.load(wg)




matrix = np.matrix(wg['adjacent_matrix'])


class Optimization:

    def __init__(self, unsorted_list):
        self.usl = set(unsorted_list)
        self.usl = list(self.usl)

        # doppelte einträge aus liste nehmen und am ende nach jeweiligen werten einfügen

        self.pairs = {}
        self.pairs['pairs'] = []


        # länge der liste könnte quantile entscheiden? -> kurze listen bräuchten niedriegere verbindungswerte
        self.pair_max_val = np.quantile(matrix, 0.98) # grenze, ab der verbindung von produkten zu klein ist um paare zu bilden
        self.con_max_val = np.quantile(matrix, 0.90) # grenze, ab der Verbindung von produkten zu klein ist um teil-sortierte listen sie zu verketten

        self.runs = 0
        self.find_paires()


    def find_paires(self):

        

        while matrix.max() > self.pair_max_val: # ab wann ist maximaler gefundener wert zu klein für aussage, dass produkte beieinander liegen -> 90% quantil
            
            self.runs += 1
        

            pAind = math.floor(matrix.argmax()/len(matrix))
            pBind = matrix.argmax()%len(matrix)

            stop = False

            for value in self.pairs['pairs']:
                
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




                # testen, ob höchste gewicht-beziehung in pairs ist
            if len(self.pairs['pairs']) > 1:

                for index, value in enumerate(self.pairs['pairs']):

                    for x in range(index+1, len(self.pairs['pairs'])-1):

                        if wg['products'][pAind] == value[-1] and wg['products'][pBind] == self.pairs['pairs'][x][0]: # zB element 0 letztes -> element 1 erstes #wenn letztes element mit ersten des nächsten pairs übereinstimmt # auf matrix werte übertragen!
                            
                            value.extend(self.pairs['pairs'][x])
                            self.pairs['pairs'].remove(self.pairs['pairs'][x])
                            matrix[pAind, pBind] = 0
                            stop = True
                            break
                
                if wg['products'][pAind] == self.pairs['pairs'][-1][-1] and wg['products'][pBind] == self.pairs['pairs'][0][0]: # element letztes letztes -> element erstes erstes

                    self.pairs['pairs'][-1].extend(self.pairs['pairs'][0])
                    self.pairs['pairs'].remove(self.pairs['pairs'][0])
                    matrix[pAind, pBind] = 0
                    stop = True


            if stop:
                continue




            if wg['products'][pAind] in self.usl and wg['products'][pBind] in self.usl:

                new_pair = [wg['products'][pAind], wg['products'][pBind]]
                self.pairs['pairs'].append(new_pair)
                self.usl.remove(wg['products'][pAind])
                self.usl.remove(wg['products'][pBind])

                print(matrix[math.floor(matrix.argmax()/len(matrix)),matrix.argmax()%len(matrix)])
            
            matrix[pAind, pBind] = 0
        
        print('\n' + 'Restliste: ' + str(self.usl))
        print('\n' + 'Paare: ' + str(self.pairs))
        print(matrix.max())
        print(self.runs)


        if len(self.pairs['pairs']) == 0:
            # was passiert, wenn liste so kurz, dass bisher keine gewichte gefunden wurde/ len(pairs)==0 ? Sonderfall implementieren 
            return None
        
        

        if self.usl:
            self.connect_leftovers()

        if len(self.pairs['pairs']) > 1:
            self.connect_paires()


    

    def connect_leftovers(self):

        matrix = np.matrix(wg['adjacent_matrix'])


        for x in range(0, len(self.usl)):

            highest_weight = 0
            listA = []
            listB = []

            for item in self.usl:

                for value in self.pairs['pairs']:

                    if matrix[wg['product_ids'][item], wg['product_ids'][value[0]]] > highest_weight:

                        listA = item
                        listB = value
                        highest_weight = matrix[wg['product_ids'][item], wg['product_ids'][value[0]]]
                    
                    if matrix[wg['product_ids'][value[-1]], wg['product_ids'][item]] > highest_weight:

                        listA = value
                        listB = item
                        highest_weight = matrix[wg['product_ids'][item], wg['product_ids'][value[0]]]
            

            print('highest lefotver: ' +  str(highest_weight))

            if(highest_weight > self.con_max_val): # minimale verbindung anpassen
                if isinstance(listB, str):
                    self.pairs['pairs'].remove(listA)
                    self.usl.remove(listB)
                    listA.append(listB)
                    self.pairs['pairs'].append(listA)

                elif isinstance(listA, str):
                    self.pairs['pairs'].remove(listB)
                    self.usl.remove(listA)
                    listB.insert(0, listA)
                    self.pairs['pairs'].append(listB)
        
        print('\n' + 'Restliste: ' + str(self.usl))
        print('\n' + 'Paare: ' + str(self.pairs))


            




    def connect_paires(self):

        matrix = np.matrix(wg['adjacent_matrix'])

        # alle letzten mit allen ersten pair-listen vergleichen und größtes gewicht davon verbinden

        #solange bis len(pairs) == 1?

        for x in range(0, len(self.pairs['pairs'])-1):
        # if len(self.pairs['pairs']) > 1:

            listA = []
            listB = []
            highest_weight = 0

            for index, value in enumerate(self.pairs['pairs']):

                for x in range(index+1, len(self.pairs['pairs'])-1):
                    
                    if matrix[wg['product_ids'][value[-1]], wg['product_ids'] [self.pairs['pairs'][x][0] ]] > highest_weight:# letztes A element -> erstem des nächsten B
                        
                        listA = value
                        listB = self.pairs['pairs'][x]
                        highest_weight = matrix[wg['product_ids'][value[-1]], wg['product_ids'] [self.pairs['pairs'][x][0] ]]


            
            if matrix[wg['product_ids'][self.pairs['pairs'][-1][-1]], wg['product_ids'][self.pairs['pairs'][0][0]]] > highest_weight: # letztes letztes element -> erstes erstes

                listA = self.pairs['pairs'][-1]
                listB = self.pairs['pairs'][0]
                highest_weight = matrix[wg['product_ids'][self.pairs['pairs'][-1][-1]], wg['product_ids'][self.pairs['pairs'][0][0]]]

            print('highest pair connect: ' + str(highest_weight))

            if highest_weight > self.con_max_val and listA in self.pairs['pairs'] and listB in self.pairs['pairs']:# minimale verbindung anpassen >5

                self.pairs['pairs'].remove(listA)
                self.pairs['pairs'].remove(listB)
                listA.extend(listB)
                self.pairs['pairs'].append(listA)
        
        print('\n' + 'Restliste: ' + str(self.usl))
        print('\n' + 'Paare: ' + str(self.pairs))
        print('\n' + 'sorted lists: ' + str(len(self.pairs['pairs'])))


            

opt = Optimization(Customer().shopping_list)



