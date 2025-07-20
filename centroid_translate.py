import numpy as np

def translate_to_origin(points):
    centroid = np.mean(points, axis=0)
    print(f"Centroid: {centroid}")
    translation = np.array([[1, 0, -centroid[0]], [0, 1, -centroid[1]], [0, 0, 1]])

    return [np.dot(translation, [x, y, 1])[:2] for x, y in points]

def main():
    triangle = [(1, 1), (4, 1), (2.5, 5)]
    result = translate_to_origin(triangle)

    print("Original:", triangle)
    print("Translated to Origin:", result)

if __name__ == "__main__":
    main()
