"""
K-Nearest Neighbors
usage:
    - For classifying cases based on their similarity to other cases
    - cases that are near to each other are said to be "neighbor"
workflow:
    - choose a value for k
    - calculate the distance of unknown cases from all cases
    - select the k-observation in the training data that are "nearest" to the unknown data point
    - predict the response of the unknown data point using the most popular response value from the k-nearest neighbor
"""
from math import sqrt


def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(0, len(row1)):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


r1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r2 = [2, 1, 2, 5, 6, 8, 9, 10, 3, 6]

print(euclidean_distance(r1, r2))
