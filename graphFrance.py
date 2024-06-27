import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import networkx as nx
import pandas as pd
import ssl
import certifi
import geopy
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

# Liste des villess
#cities = ["Rouen", "Le Petit-Quevilly", "Le Grand-Quevilly", "Petit-Couronne", "Canteleu", "Sahurs", "La Bouille", "Moulineaux"]
"""
cities = [
    "Rouen", "Le Petit-Quevilly",
    "La Bouille", "Deville-les-Rouen",
    "Saint-Martin-du-Vivier",
    "Le Mesnil-Esnard", "Boos", "Saint-Etienne-du-Rouvray", "Oissel",
    "Grand-Couronne", "Quevillon"
]
"""
cities = [
    "Rouen", "Le Petit-Quevilly", "Le Grand-Quevilly", "Petit-Couronne", 
    "Canteleu", "Sahurs", "La Bouille", "Moulineaux", "Saint-Martin-de-Boscherville", "Hénouville", "Deville-les-Rouen", "Bois-Guillaume", 
    "Saint-Martin-du-Vivier", "Bonsecours", "Saint-Aubin-Epinay", 
    "Le Mesnil-Esnard", "Amfreville-la-Mi-Voie", "Franqueville-Saint-Pierre", 
    "Belbeuf", "Boos", "Saint-Etienne-du-Rouvray", "Oissel", "Sotteville-les-Rouen",
    "Grand-Couronne", "Le Val Adam", "Quevillon", "Saint-Aubin-Celloville"
]




# Initialisation du géolocalisateur
geolocator = Nominatim(user_agent="vrp_france")

# Obtenir les coordonnées géographiques des villes
locations = {}
for city in cities:
    location = geolocator.geocode(city + ", France")
    locations[city] = (location.latitude, location.longitude)

# Création du graphe
G = nx.Graph()

# Ajout des nœuds
for city, coord in locations.items():
    G.add_node(city, pos=coord)

# Calcul des distances et ajout des arêtes
distances = {}
for city1 in cities:
    for city2 in cities:
        if city1 != city2:
            distance = geodesic(locations[city1], locations[city2]).km
            G.add_edge(city1, city2, weight=distance)
            distances[(city1, city2)] = distance

# Création de la carte Folium
map_france = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Ajout des marqueurs pour chaque ville
for city, coord in locations.items():
    folium.Marker(location=coord, popup=city).add_to(map_france)

# Ajout des lignes entre les villes
for (city1, city2), distance in distances.items():
    folium.PolyLine([locations[city1], locations[city2]], color="blue", weight=2.5, opacity=1).add_to(map_france)

# Sauvegarde de la carte dans un fichier HTML sur le bureau

map_france.save("carte_vrp_france.html")

# Générer la matrice d'adjacence des distances
adj_matrix = nx.adjacency_matrix(G, weight='weight').todense()
df_adj_matrix = pd.DataFrame(adj_matrix, index=cities, columns=cities)
print("Matrice d'adjacence des distances (en km) :\n", df_adj_matrix)
# sauvegarde de la matrice d'adjacence dans un fichier CSV
df_adj_matrix.to_markdown("matrice_adjacence_distances.md")