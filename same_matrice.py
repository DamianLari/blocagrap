import numpy as np
import networkx as nx
import pickle

def create_graph(cities_count, complete=True, threshold=0.5):
    mat = np.random.random((cities_count, cities_count))
    mat = mat + mat.T
    np.fill_diagonal(mat, 0)
    adj_matrix = mat * cities_count
    if not complete:
        adj_matrix[adj_matrix < threshold] = 0  
    G = nx.from_numpy_array(adj_matrix)
    if not nx.is_connected(G):
        raise ValueError("Le graphe généré n'est pas connecté. Essayez de régénérer la matrice.")
    return G, adj_matrix

def save_graph_and_matrix(G, adj_matrix, matrix_file='adj_matrix.npy', graph_file='graph.pkl'):
    np.save(matrix_file, adj_matrix)
    with open(graph_file, 'wb') as f:
        pickle.dump(G, f)

def load_graph_and_matrix(matrix_file='adj_matrix.npy', graph_file='graph.pkl'):
    adj_matrix = np.load(matrix_file)
    
    with open(graph_file, 'rb') as f:
        G = pickle.load(f)
    
    return G, adj_matrix

cities_count = 40
G, adj_matrix = create_graph(cities_count, complete=False, threshold=0.7)
print(adj_matrix)
print(G)

save_graph_and_matrix(G, adj_matrix)

# pour charger les données:
# G, adj_matrix = load_graph_and_matrix()
# print(loaded_adj_matrix)
# print(loaded_G.edges)
