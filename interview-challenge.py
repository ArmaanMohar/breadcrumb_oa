from itertools import combinations
import sys
import re

"""
For processing the large file, we should consider using parallel computing techniques, such as threading or leveraging big data technologies like Hadoop

Time Complexity: O(n^4)
Space Complexity: O(n) 

volume_of_tetrahedron:

Time Complexity: O(1) because the operations to calculate the volume (vector subtractions, cross product, and dot product) are all constant time operations.
Space Complexity: O(1) because it only uses a fixed amount of space for storing vectors and intermediate results.
read_points_from_file:

Time Complexity: O(n) where n is the number of lines in the file. Each line is processed once.
Space Complexity: O(n) because it stores all the points read from the file in a list.
find_smallest_tetrahedron_indices:

Time Complexity: O(C(n, 4)) * O(volume_of_tetrahedron) = O(n^4), since it iterates over all possible combinations of 4 points out of n, and for each combination, it calls volume_of_tetrahedron.
Space Complexity: O(1) as it only uses a fixed amount of additional space for storing intermediate results like the smallest volume and corresponding indices.

"""

def volume_of_tetrahedron(p1, p2, p3, p4):
    """
    Calculates the volume of a tetrahedron formed by four points using the scalar triple product formula.

    Args:
        p1, p2, p3, p4 (tuple): Points forming the tetrahedron, each in the form (x, y, z).

    Returns:
        float: The volume of the tetrahedron.
    """
    # Vectors from p1 to p2, p3, and p4
    AB = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    AC = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
    AD = (p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2])

    # Direct calculation of the cross product components
    cross_product_x = AB[1] * AC[2] - AB[2] * AC[1]
    cross_product_y = AB[2] * AC[0] - AB[0] * AC[2]
    cross_product_z = AB[0] * AC[1] - AB[1] * AC[0]

    # Dot product of AD with the cross product of AB and AC
    scalar_triple_product = (
        AD[0] * cross_product_x +
        AD[1] * cross_product_y +
        AD[2] * cross_product_z
    )

    # The volume of the tetrahedron
    volume = abs(scalar_triple_product) / 6.0
    return volume

def read_points_from_file(filename):
    """
    Reads a file containing points in the format (x, y, z, n) and returns a list of tuples.
    Each tuple contains the coordinates (x, y, z) as floats and the associated number n as an integer.

    Args:
        filename (str): Path to the input file.

    Returns:
        list: A list of tuples where each tuple is of the form (x, y, z, n).
    """
    points = []
    with open(filename, 'r') as file:
        for line in file:
            # Remove all characters except digits, commas, periods, and hyphens
            line = re.sub(r'[^\d.,-]', '', line)
            x, y, z, n = map(float, line.split(','))
            points.append((x, y, z, int(n)))
    return points

def find_smallest_tetrahedron_indices(points):
    """
    Finds the valid tetrahedron with the smallest volume from the given points.

    Args:
        points (list): List of points where each point is a tuple (x, y, z, n).

    Returns:
        tuple: A tuple of indices of the points forming the smallest valid tetrahedron.
    """
    smallest_volume = sys.maxsize  # Initialize with a very large number
    smallest_indices = None

    # Iterate over all combinations of four points
    for comb in combinations(range(len(points)), 4):
        p1, p2, p3, p4 = points[comb[0]], points[comb[1]], points[comb[2]], points[comb[3]]
        sum_n = p1[3] + p2[3] + p3[3] + p4[3]
        # Check if the sum of n values is 100
        if sum_n == 100:
            # Calculate the volume of the tetrahedron
            vol = volume_of_tetrahedron(p1, p2, p3, p4)
            # Update the smallest volume and indices if this tetrahedron is smaller
            if vol < smallest_volume:
                smallest_volume = vol
                smallest_indices = comb

    return smallest_indices

# Main execution
if __name__ == "__main__":
    # File paths
    small_file = 'points_small.txt'  
    large_file = 'points_large.txt'
    file_test = 'test.txt'  # For testing, answer is 0, 3, 4, 6

    # Read points from the file
    points = read_points_from_file(large_file)

    # Find the smallest tetrahedron indices
    smallest_indices = find_smallest_tetrahedron_indices(points)
    print(smallest_indices)
