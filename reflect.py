import numpy as np

def reflect(points, axis='x'):
    if axis == 'x':
        matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
    elif axis == 'y':
        matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    elif axis == 'origin':
        matrix = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
    else:
        raise ValueError("Invalid axis")

    return [np.dot(matrix, [x, y, 1])[:2] for x, y in points]

def main():
    x = float(input("X-coordinate: "))
    y = float(input("Y-coordinate: "))
    axis = input("Reflect over (x/y/origin): ").strip().lower()

    result = reflect([(x, y)], axis)
    print(f"Reflected Point: {result[0]}")

if __name__ == "__main__":
    main()
