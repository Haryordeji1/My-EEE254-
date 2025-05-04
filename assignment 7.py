import math

# Function to calculate the nth root of a number
def nth_root(value, n):
    """
    Returns the nth root of a given value.
    Example: nth_root(27, 3) → 3.0
    """
    return value ** (1 / n)

# Function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    """
    Returns the Euclidean distance between two points.
    Each point should be a tuple: (x, y)
    Example: euclidean_distance((1, 2), (4, 6)) → 5.0
    """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Example usage
if __name__ == "__main__":
    # Nth root test
    print("Cube root of 27 is:", nth_root(27, 3))

    # Euclidean distance test
    print("Distance between (1, 2) and (4, 6) is:", euclidean_distance((1, 2), (4, 6)))