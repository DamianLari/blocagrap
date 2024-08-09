#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

double calculateTotalDistance(const vector<int>& path, const vector<vector<double> >& distances) {
    double totalDistance = 0;
    for (size_t i = 0; i < path.size() - 1; ++i) {
        totalDistance += distances[path[i]][path[i + 1]];
    }
    totalDistance += distances[path.back()][path.front()]; 
    return totalDistance;
}

int main() {
    vector<string> cities;
    cities.push_back("Rouen");
    cities.push_back("Le Petit-Quevilly");
    cities.push_back("La Bouille");
    cities.push_back("Deville-les-Rouen");
    cities.push_back("Saint-Martin-du-Vivier");
    cities.push_back("Le Mesnil-Esnard");
    cities.push_back("Boos");
    cities.push_back("Saint-Etienne-du-Rouvray");
    cities.push_back("Oissel");
    cities.push_back("Grand-Couronne");
    cities.push_back("Quevillon");

    vector<vector<double> > distances = {
        {0.000000, 2.963495, 15.416571, 4.561632, 5.771724, 4.558626, 9.719719, 6.381599, 10.902434, 11.655627, 10.539540},
        {2.963495, 0.000000, 12.453464, 5.166462, 8.727359, 5.745849, 10.836939, 5.008939, 9.372577, 8.871207, 7.981572},
        {15.416571, 12.453464, 0.000000, 15.666415, 21.165524, 16.564320, 20.042405, 12.214686, 12.068822, 5.383602, 7.662052},
        {4.561632, 5.166462, 15.666415, 0.000000, 8.026752, 9.119771, 14.250350, 10.085208, 14.526250, 13.316107, 8.986413},
        {5.771724, 8.727359, 21.165524, 8.026752, 0.000000, 6.536691, 9.515260, 10.787410, 14.849493, 17.131263, 16.065461},
        {4.558626, 5.745849, 16.564320, 9.119771, 6.536691, 0.000000, 5.223160, 4.715242, 8.354535, 11.753791, 13.588076},
        {9.719719, 10.836939, 20.042405, 14.250350, 9.515260, 5.223160, 0.000000, 7.942991, 9.146071, 14.767055, 18.381224},
        {6.381599, 5.008939, 12.214686, 10.085208, 10.787410, 4.715242, 7.942991, 0.000000, 4.532051, 7.143140, 10.896226},
        {10.902434, 9.372577, 12.068822, 14.526250, 14.849493, 8.354535, 9.146071, 4.532051, 0.000000, 6.751385, 13.490058},
        {11.655627, 8.871207, 5.383602, 13.316107, 17.131263, 11.753791, 14.767055, 7.143140, 6.751385, 0.000000, 8.259031},
        {10.539540, 7.981572, 7.662052, 8.986413, 16.065461, 13.588076, 18.381224, 10.896226, 13.490058, 8.259031, 0.000000}
    };

    vector<int> bestPath;
    double bestDistance = numeric_limits<double>::infinity();

    vector<int> indices(cities.size());
    for (size_t i = 0; i < indices.size(); ++i) {
        indices[i] = i;
    }

    do {
        double currentDistance = calculateTotalDistance(indices, distances);
        if (currentDistance < bestDistance) {
            bestDistance = currentDistance;
            bestPath = indices;
        }
    } while (next_permutation(indices.begin(), indices.end()));

    cout << "Meilleur chemin: ";
    for (size_t i = 0; i < bestPath.size(); ++i) {
        cout << cities[bestPath[i]];
        if (i < bestPath.size() - 1) {
            cout << " -> ";
        }
    }
    cout << endl;
    cout << "Distance totale: " << bestDistance << " km" << endl;

    return 0;
}
