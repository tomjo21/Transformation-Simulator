import numpy as np

def main():
    print("Enter a 3x3 transformation matrix:")
    matrix = []
    for i in range(3):
        row = list(map(float, input(f"Row {i+1} (3 values): ").split()))
        matrix.append(row)

    matrix = np.array(matrix)
    print("You entered:\n", matrix)

    x = float(input("Enter x-coordinate: "))
    y = float(input("Enter y-coordinate: "))

    result = np.dot(matrix, [x, y, 1])
    print(f"Transformed Point: {result[:2]}")

if __name__ == "__main__":
    main()
