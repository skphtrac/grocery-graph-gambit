import json
import math
import numpy as np
from customer import Customer


with open('weighted_graph.json') as wg:
    wg = json.load(wg)




matrix = np.matrix(wg['adjacent_matrix'])

# sorted_weights = []

# for x in wg['adjacent_matrix']: # x sind einzelne Reihen
#     for element in x:
#         sorted_weights.append(element)

# sorted_weights.sort()


# print(matrix)
# print(matrix.argsort())

# print(matrix.max())

# print(math.floor(matrix.argmax()/len(matrix))) # index Product A

# print(matrix.argmax()%len(matrix)) # index Product B

# print(matrix[math.floor(matrix.argmax()/len(matrix)),matrix.argmax()%len(matrix)])


class Optimization:

    def __init__(self, unsorted_list):
        self.usl = set(unsorted_list)
        self.usl = list(self.usl)

        # doppelte einträge aus liste nehmen und am ende nach jeweiligen werten einfügen

        self.pairs = {}
        self.pairs['pairs'] = []

        self.runs = 0
        self.find_paires()


    def find_paires(self):

        

        while matrix.max() > 40: # ab wann ist maximaler gefundener wert zu klein für aussage, dass produkte beieinander liegen
            
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

                # for i, item in enumerate(value):
                    
                #     if wg['products'][pBind] == item and wg['products'][pAind] in self.usl: # wenn produkt in paaren gefunden wurde und keinen vorgänger hat, hinzufügen
                #         if i == 0:

                #             value.insert(i, wg['products'][pAind])
                #             self.usl.remove(wg['products'][pAind])
                #             matrix[pAind, pBind] = 0
                #             stop = True
                #             break

                #     if wg['products'][pAind] == item and wg['products'][pBind] in self.usl: # Wenn produkt in pairs gefunden wurde und dieses keinen nachfolger hat, hinzufügen
                #         if i == len(value)-1:

                #             value.append(wg['products'][pBind])
                #             self.usl.remove(wg['products'][pBind])
                #             matrix[pAind, pBind] = 0
                #             stop = True
                #             break

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

                        # elif wg['products'][pAind] == self.pairs['pairs'][x][0] and wg['products'][pBind] == value[-1]: # element 1 erstes -> element 0 letztes
                            
                        #     # folgende logik evtl anpassen, wenn kantengewicht auch richtung vorgibt, entsteht durch folgende logik fehler in pair-listen
                            
                        #     value.extend(self.pairs['pairs'][x])
                        #     self.pairs['pairs'].remove(self.pairs['pairs'][x])   
                        #     matrix[pAind, pBind] = 0
                        #     break
                
                if wg['products'][pAind] == self.pairs['pairs'][-1][-1] and wg['products'][pBind] == self.pairs['pairs'][0][0]: # element letztes letztes -> element erstes erstes

                    self.pairs['pairs'][-1].extend(self.pairs['pairs'][0])
                    self.pairs['pairs'].remove(self.pairs['pairs'][0])
                    matrix[pAind, pBind] = 0
                    stop = True
                
                # elif wg['products'][pAind] == self.pairs['pairs'][0][0] and wg['products'][pBind] == self.pairs['pairs'][-1][-1]: # element erstes erstes -> element letztes letztes
                    
                #     # folgende logik evtl anpassen, wenn kantengewicht auch richtung vorgibt, entsteht durch folgende logik fehler in pair-listen
                    
                #     self.pairs['pairs'][-1].extend(self.pairs['pairs'][0])
                #     self.pairs['pairs'].remove(self.pairs['pairs'][0])
                #     matrix[pAind, pBind] = 0


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
        print(self.runs)

        self.connect_paires()
        # was passiert, wenn liste so kurz, dass bisher keine gewichte gefunden wurde/ len(pairs)==0 ? Sonderfall implementieren 
    
    def connect_paires(self):

        matrix = np.matrix(wg['adjacent_matrix'])

        # alle letzten mit allen ersten pair-listen vergleichen und größtes gewicht davon verbinden

        highest_weight = 0
        prodA = ''
        prodB = ''
        
        # print(self.pairs['pairs'][1])

        # if len(self.pairs['pairs']) > 1:

        #     for index, value in enumerate(self.pairs['pairs']):

        #         for x in range(index+1, len(self.pairs['pairs']-1)):

        #             if value[len(value)-1] == self.pairs['pairs'][x][0]: # wenn letztes element mit ersten des nächsten pairs übereinstimmt # auf matrix werte übertragen!
                    
        #             if self.pairs['pairs'][x][0] == value[len(value)-1]:
            
        #     if self.pairs['pairs'][len(self.pairs['pairs'])-1] == self.pairs['pairs'][0][0]:
            
        #     if self.pairs['pairs'][0][0] == self.pairs['pairs'][len(self.pairs['pairs'])-1]













            # if index > len(self.pair['pairs'][0]-1):
            #     #         matrix nimmt nur int an, ID der string-produkte aus json file nehmen
            #     if matrix[value[len(value)-1], self.pair['pairs'][0][index+1]] > heighest_weight: # value[len(value)-1]  -> self.pair['pairs'][0][index+1]

            #         heighest_weight = matrix[value[len(value)-1],self.pair['pairs'][0][index+1]]
            #         prodA = value[len(value)-1]
            #         probB = self.pair['pairs'][0][index+1]

            #     if matrix[self.pair['pairs'][0][index+1], value[len(value)-1]] > heighest_weight:

            #         heighest_weight = matrix[self.pair['pairs'][0][index+1], value[len(value)-1]]
            #         prodA = self.pair['pairs'][0][index+1]
            #         prodB = value[len(value)-1]
                

            #     self.pair['pairs'][0][index+1] -> value[len(value)-1]

            # elif index == len(self.pair['pairs'][0]-1):

            #     value[len(value)-1] -> self.pair['pairs'][0][0]

            #     self.pair['pairs'][0][0] -> value[len(value)-1]

        


            

opt = Optimization(Customer().shopping_list)



