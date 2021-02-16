import json
import numpy as np
from shopping_sequence_simulation import create_shopping_sequences




class Weighted_Directed_Graph:

    def __init__(self, size):

        self.adj_matrix = []
        
        for x in range(size):
            self.adj_matrix.append([0 for x in range(size)])

        self.size = size
       
    

    def increase_weight(self, node1, node2):

        if node1 == node2:
            return None
        
        self.adj_matrix[node1][node2] += 1


    def print_matrix(self):

        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.adj_matrix]))
        



create_shopping_sequences(5000)

with open('shopping_sequences.json') as ss:
    ss = json.load(ss)


unique_products = []

for key in ss:
    for x in range(0, len(ss[key][0])):
        unique_products.append(ss[key][0][x])

unique_products = list(set(unique_products)) # products collected in simulated shopping sequences without duplicates



product_ids = {} # to determine adjacency matrix index

for element in unique_products:
    product_ids[element] = unique_products.index(element)



matrix = Weighted_Directed_Graph(len(unique_products))

for key in ss:
    for x in range(0, len(ss[key][0])-1):
        matrix.increase_weight(product_ids[ss[key][0][x]], product_ids[ss[key][0][x+1]]) # fills adjacency matrix with simulated shopping sequence products



weighted_graph = {}
weighted_graph['products'] = unique_products
weighted_graph['product_ids'] = product_ids
weighted_graph['adjacent_matrix'] = matrix.adj_matrix

with open('weighted_graph.json', 'w') as file:
    json.dump(weighted_graph, file, indent = 4)
