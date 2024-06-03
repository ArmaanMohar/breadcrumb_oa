from itertools import combinations
import sys
import re

def volume_of_tetrahedron(p1, p2, p3, p4):
    AB = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    AC = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
    AD = (p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2])

    cross_product_x = AB[1] * AC[2] - AB[2] * AC[1]
    cross_product_y = AB[2] * AC[0] - AB[0] * AC[2]
    cross_product_z = AB[0] * AC[1] - AB[1] * AC[0]

    scalar_triple_product = (
        AD[0] * cross_product_x +
        AD[1] * cross_product_y +
        AD[2] * cross_product_z
    )

    volume = abs(scalar_triple_product) / 6.0
    return volume

def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            line = re.sub(r'[^\d.,-]', '', line)
            x, y, z, n = map(float, line.split(','))
            points.append((x, y, z, int(n)))
    return points

def find_smallest_tetrahedron_indices(points):
    smallest_volume = sys.maxsize
    smallest_indices = None

    for comb in combinations(range(len(points)), 4):
        p1, p2, p3, p4 = points[comb[0]], points[comb[1]], points[comb[2]], points[comb[3]]
        sum_n = p1[3] + p2[3] + p3[3] + p4[3]
        if sum_n == 100:
            vol = volume_of_tetrahedron(p1, p2, p3, p4)
            if vol < smallest_volume:
                smallest_volume = vol
                smallest_indices = comb

    return smallest_indices

# Read points from the file
small_file = 'points_small.txt'  # Change this to 'points_large.txt' for the larger file
large_file = 'points_large.txt'  # Change this to 'points_large.txt' for the larger file
file_test = 'test.txt' # answer is 0, 3, 4, 6
points = read_points_from_file(small_file)

# Find the smallest tetrahedron indices
smallest_indices = find_smallest_tetrahedron_indices(points)
print(smallest_indices)
