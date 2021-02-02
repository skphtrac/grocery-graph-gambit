import json
import numpy as np
import networkx as nx

with open('shopping_sequences.json') as ss:
    ss = json.load(ss)




class WeightedGraph:

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
        


        

products = []

for key in ss:
    for x in range(0, len(ss[key][0])):
        products.append(ss[key][0][x])

# print('unique products: ' + str(len(set(products))))



unique_products = list(set(products))



product_ids = {}

for element in set(products):
    product_ids[element] = unique_products.index(element)


matrix = WeightedGraph(len(unique_products))

for key in ss:
    for x in range(0, len(ss[key][0])-1):
        matrix.increase_weight(product_ids[ss[key][0][x]], product_ids[ss[key][0][x+1]])

# matrix.print_matrix()

weighted_graph = {}

weighted_graph['product_ids'] = product_ids
weighted_graph['adjacent_matrix'] = matrix.adj_matrix

with open('weighted_graph.json', 'w') as file:
    json.dump(weighted_graph, file, indent = 4)


B = np.matrix(matrix.adj_matrix)

print(B)