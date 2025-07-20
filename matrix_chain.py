import numpy as np

def main():
    print("Matrix Order Test (Scale → Rotate vs Rotate → Scale)")

    point = np.array([2, 1, 1])

    scale = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]])
    angle = np.radians(45)
    rotate = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle),  np.cos(angle), 0],
        [0, 0, 1]
    ])

    first = np.dot(rotate, np.dot(scale, point))
    second = np.dot(scale, np.dot(rotate, point))

    print("Scale then Rotate:", first[:2])
    print("Rotate then Scale:", second[:2])

if __name__ == "__main__":
    main()
