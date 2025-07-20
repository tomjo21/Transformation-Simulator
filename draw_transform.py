import numpy as np
import matplotlib.pyplot as plt

def transform_triangle(triangle, matrix):
    transformed = []
    for point in triangle:
        result = np.dot(matrix, [point[0], point[1], 1])
        transformed.append(result[:2])
    return transformed

def main():
    triangle = [(0, 0), (1, 0), (0.5, 1)]
    angle = np.radians(45)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle),  np.cos(angle), 0],
        [0, 0, 1]
    ])
    rotated = transform_triangle(triangle, rotation_matrix)

    orig_x, orig_y = zip(*triangle + [triangle[0]])
    trans_x, trans_y = zip(*rotated + [rotated[0]])

    plt.plot(orig_x, orig_y, 'bo-', label='Original')
    plt.plot(trans_x, trans_y, 'ro--', label='Rotated')
    plt.axis('equal')
    plt.legend()
    plt.title('Triangle Rotation Visualization')
    plt.show()

if __name__ == "__main__":
    main()
