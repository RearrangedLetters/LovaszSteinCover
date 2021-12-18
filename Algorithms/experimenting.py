from Algorithms.hypergraph import *
from Algorithms.covering_algorithms import *

M_example = [[0, 1, 2, 3],  # f_1
             [3, 4, 5],  # f_2
             [5, 7, 8, 11],  # f_3
             [7, 8, 9, 10],  # f_4
             [0, 1, 2, 4, 6, 11],  # f_5
             [10, 12, 13, 14, 15],  # f_6
             [11, 20],  # f_7
             [11, 12, 14, 16, 17],  # f_8
             [15, 17],  # f_9
             [17, 18, 19, 20],  # f_10
             ]

G = Hypergraph(M_example)

print("#Vertices: " + str(G.num_points()))
print("#Edges: " + str(G.num_hedges()))

covering = lovasz_stein_covering(G)
print("#Covering: " + str(len(covering)))
print(covering)
