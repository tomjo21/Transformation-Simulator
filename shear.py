import numpy as np

def apply_shear(points, shear_x=0, shear_y=0):
    shear_matrix = np.array([
        [1, shear_x, 0],
        [shear_y, 1, 0],
        [0, 0, 1]
    ])
    transformed = []
    for x, y in points:
        result = np.dot(shear_matrix, [x, y, 1])
        transformed.append(result[:2])
    return transformed

def main():
    print("Shearing Transformation")
    shape = input("Choose shape (point/triangle): ").strip().lower()

    coords = []
    if shape == 'triangle':
        for i in range(3):
            x = float(input(f"Enter x{i+1}: "))
            y = float(input(f"Enter y{i+1}: "))
            coords.append((x, y))
    elif shape == 'point':
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        coords.append((x, y))
    else:
        print("Invalid shape.")
        return

    shx = float(input("Enter shear factor in X: "))
    shy = float(input("Enter shear factor in Y: "))

    result = apply_shear(coords, shx, shy)

    print("\nOriginal:", coords)
    print("Sheared:", result)

if __name__ == "__main__":
    main()
