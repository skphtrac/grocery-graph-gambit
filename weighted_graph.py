import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



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
        




with open('shopping_sequences.json') as ss:
    ss = json.load(ss)


unique_products = []

for key in ss:
    for x in range(0, len(ss[key][0])):
        unique_products.append(ss[key][0][x])

unique_products = list(set(unique_products)) # alle uniquen products aus allen shopping sequences



product_ids = {} # Dictionary mit Produkten und dazugehöriger ID zum bestimmen der Matrix-Plätze

for element in unique_products:
    product_ids[element] = unique_products.index(element)



matrix = WeightedGraph(len(unique_products))

for key in ss:
    for x in range(0, len(ss[key][0])-1):
        matrix.increase_weight(product_ids[ss[key][0][x]], product_ids[ss[key][0][x+1]])



weighted_graph = {}
weighted_graph['products'] = unique_products
weighted_graph['product_ids'] = product_ids
weighted_graph['adjacent_matrix'] = matrix.adj_matrix

with open('weighted_graph.json', 'w') as file:
    json.dump(weighted_graph, file, indent = 4)


with open('weighted_graph.json') as wg:
    wg = json.load(wg)


sorted_weights = []

for x in wg['adjacent_matrix']: # x sind einzelne Reihen
    for element in x:
        sorted_weights.append(element)


sorted_weights.sort()
print(sorted_weights)

print(np.quantile(sorted_weights, 0.90))
# plt.boxplot(sorted_weights)
# plt.show()




# B = np.matrix(matrix.adj_matrix)

# D = nx.from_numpy_matrix(B, create_using=nx.DiGraph)

# C = nx.adjacency_matrix(D)



# print(B)

# prod = list(product_ids.keys())

# fig, ax = plt.subplots(figsize=(len(B)*1.2,len(B)*1.2))
# ax.matshow(B, cmap='seismic')

# for (i, j), z in np.ndenumerate(B):
#     ax.text(j, i, '{:0.1f}'.format(z), ha='center', va='center', bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'))


# ax.set_xticks(np.arange(len(B)))
# ax.set_yticks(np.arange(len(B)))

# ax.set_yticklabels(['']+prod)   # startet immer mit zweiter reihe?


# plt.savefig('product_matrix.png')