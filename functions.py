import numpy as np

def distance_2_points(point_a, point_b):

    return np.sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)