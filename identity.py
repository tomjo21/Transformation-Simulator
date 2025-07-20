import numpy as np

def main():
    point = np.array([4, 7, 1])
    identity_matrix = np.eye(3)

    result = np.dot(identity_matrix, point)

    print(f"Original Point: {point[:2]}")
    print(f"After Identity Transformation: {result[:2]} (should be same)")

if __name__ == "__main__":
    main()
