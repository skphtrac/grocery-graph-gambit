# Graph based Reconstruction of Grocery Store Layout based on User Collected Shopping Data

## General info
This project shows the code for a bachelor term paper presented to and conducted for the faculty of business administration and economics of university duisburg-essen. The aim was to optimize grocery shopping by sorting shopping lists which would shorten the paths customers take through stores. This was done by simulating shopping sequences to create data (*shopping_sequence_simulation.py*) which was represented using a weighted directed graph (*weighted_graph.py*) in order to generate sorted shopping lists (*optimization.py*).
  
## Technologies
The project is created with:
* Python version: 3.8.3
* Anaconda navigator version: 1.9.12
* Visual Studio Code version: 1.53.2
* Networkx version: 2.4
* Matplotlib version: 3.2.2
* Numpy version: 1.18.5

## Setup
To run this project install Python, Anaconda Navigator and Visual Studio Code. Open Anaconda Navigator and install the packages networkx, matplotlib and numpy. Using Anaconda Navigator start Visual Studio Code to view and run the .py-files. 

To achieve the results stated in the term paper, run the files in the following order:
1) weighted_graph.py 
2) optimization.py

*weighted_graph.py* simulates shopping sequences with both the *shopping_sequence_simulation.py* and *layout.py* file, and after execution two files should have been created: 

  * shopping_sequences.json, containing the simulated shopping sequences
  * weighted_graph.json, containing the weighted directed graph of past shopping sequences, products used in the graph and product ids which are later used to identify products (product id integer = adjacency matrix index integer)
    
*optimization.py* uses the created graph to optimize the shopping lists and prints out lists of found product bonds and rest products which could not have been connected
