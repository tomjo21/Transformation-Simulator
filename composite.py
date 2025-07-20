import numpy as np

def get_transformation():
    transformation_matrix = np.eye(3)

    while True:
        print("\nChoose transformations to apply:")
        print("1. Scale")
        print("2. Rotate")
        print("3. Translate")
        print("4. Done")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            sx = float(input("Scaling factor for X-axis: "))
            sy = float(input("Scaling factor for Y-axis: "))
            scale_matrix = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
            transformation_matrix = np.dot(scale_matrix, transformation_matrix)

        elif choice == '2':
            angle = float(input("Rotation angle in degrees: "))
            radians = np.radians(angle)
            cos_a, sin_a = np.cos(radians), np.sin(radians)
            rotation_matrix = np.array([
                [cos_a, -sin_a, 0],
                [sin_a,  cos_a, 0],
                [0,      0,     1]
            ])
            transformation_matrix = np.dot(rotation_matrix, transformation_matrix)

        elif choice == '3':
            tx = float(input("Translation along X-axis: "))
            ty = float(input("Translation along Y-axis: "))
            translation_matrix = np.array([
                [1, 0, tx],
                [0, 1, ty],
                [0, 0, 1]
            ])
            transformation_matrix = np.dot(translation_matrix, transformation_matrix)

        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    return transformation_matrix

def apply_transformation(matrix, points):
    transformed_points = []
    for point in points:
        vector = np.array([point[0], point[1], 1])
        result = np.dot(matrix, vector)
        transformed_points.append(result[:2])
    return transformed_points

def display_transformation_result(original, transformed):
    print("\nOriginal Coordinates:")
    for i, point in enumerate(original):
        print(f"Point {i+1}: {point}")

    print("\nTransformed Coordinates:")
    for i, point in enumerate(transformed):
        print(f"Point {i+1}: {point}")

def main():
    shape = input("Would you like to transform a point or a triangle? (point/triangle): ").strip().lower()

    if shape == 'triangle':
        coordinates = []
        for i in range(3):
            x = float(input(f"X-coordinate of vertex {i+1}: "))
            y = float(input(f"Y-coordinate of vertex {i+1}: "))
            coordinates.append((x, y))

        transformation_matrix = get_transformation()
        new_coordinates = apply_transformation(transformation_matrix, coordinates)
        display_transformation_result(coordinates, new_coordinates)

    elif shape == 'point':
        x = float(input("Enter X-coordinate: "))
        y = float(input("Enter Y-coordinate: "))
        point = [(x, y)]

        transformation_matrix = get_transformation()
        transformed_point = apply_transformation(transformation_matrix, point)
        display_transformation_result(point, transformed_point)

    else:
        print("Invalid choice. Please enter 'point' or 'triangle'.")

if __name__ == "__main__":
    main()
