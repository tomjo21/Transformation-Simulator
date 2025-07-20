import numpy as np

def apply(matrix, points):
    return [np.dot(matrix, [x, y, 1])[:2] for x, y in points]

def main():
    shape = [(1, 1), (3, 1), (2, 3)]

    print("Original:", shape)

    # 1. Scale
    scale = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]])
    shape = apply(scale, shape)
    print("After Scaling:", shape)

    # 2. Rotate
    angle = np.radians(30)
    rotate = np.array([[np.cos(angle), -np.sin(angle), 0],
                       [np.sin(angle),  np.cos(angle), 0],
                       [0, 0, 1]])
    shape = apply(rotate, shape)
    print("After Rotation:", shape)

    # 3. Translate
    translate = np.array([[1, 0, 5], [0, 1, 3], [0, 0, 1]])
    shape = apply(translate, shape)
    print("After Translation:", shape)

if __name__ == "__main__":
    main()
