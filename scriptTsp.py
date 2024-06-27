import itertools

# Liste des villes
cities = [
    "Rouen", "Le Petit-Quevilly", "La Bouille", "Deville-les-Rouen", 
    "Saint-Martin-du-Vivier", "Le Mesnil-Esnard", "Boos", 
    "Saint-Etienne-du-Rouvray", "Oissel", "Grand-Couronne", "Quevillon"
]

# Matrice des distances
distances = [
    [0.000000, 2.963495, 15.416571, 4.561632, 5.771724, 4.558626, 9.719719, 6.381599, 10.902434, 11.655627, 10.539540],
    [2.963495, 0.000000, 12.453464, 5.166462, 8.727359, 5.745849, 10.836939, 5.008939, 9.372577, 8.871207, 7.981572],
    [15.416571, 12.453464, 0.000000, 15.666415, 21.165524, 16.564320, 20.042405, 12.214686, 12.068822, 5.383602, 7.662052],
    [4.561632, 5.166462, 15.666415, 0.000000, 8.026752, 9.119771, 14.250350, 10.085208, 14.526250, 13.316107, 8.986413],
    [5.771724, 8.727359, 21.165524, 8.026752, 0.000000, 6.536691, 9.515260, 10.787410, 14.849493, 17.131263, 16.065461],
    [4.558626, 5.745849, 16.564320, 9.119771, 6.536691, 0.000000, 5.223160, 4.715242, 8.354535, 11.753791, 13.588076],
    [9.719719, 10.836939, 20.042405, 14.250350, 9.515260, 5.223160, 0.000000, 7.942991, 9.146071, 14.767055, 18.381224],
    [6.381599, 5.008939, 12.214686, 10.085208, 10.787410, 4.715242, 7.942991, 0.000000, 4.532051, 7.143140, 10.896226],
    [10.902434, 9.372577, 12.068822, 14.526250, 14.849493, 8.354535, 9.146071, 4.532051, 0.000000, 6.751385, 13.490058],
    [11.655627, 8.871207, 5.383602, 13.316107, 17.131263, 11.753791, 14.767055, 7.143140, 6.751385, 0.000000, 8.259031],
    [10.539540, 7.981572, 7.662052, 8.986413, 16.065461, 13.588076, 18.381224, 10.896226, 13.490058, 8.259031, 0.000000]
]

# Fonction pour calculer la distance totale d'un chemin donné
def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    total_distance += distances[path[-1]][path[0]]  # Retour à la ville de départ
    return total_distance

# Générer toutes les permutations possibles des indices de villes
city_indices = range(len(cities))
permutations = itertools.permutations(city_indices)

# Initialiser la meilleure distance et le meilleur chemin
best_distance = float('inf')
best_path = []

# Calculer la distance totale pour chaque permutation
for perm in permutations:
    current_distance = calculate_total_distance(perm, distances)
    if current_distance < best_distance:
        best_distance = current_distance
        best_path = perm

# Convertir les indices de villes en noms de villes pour le chemin optimal
best_path_cities = [cities[i] for i in best_path]

# Afficher le meilleur chemin et la meilleure distance
print(f"Meilleur chemin: {' -> '.join(best_path_cities)}")
print(f"Distance totale: {best_distance} km")
