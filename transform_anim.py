import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

triangle = [(0, 0), (1, 0), (0.5, 1)]
angle_step = np.radians(5)

def transform(points, angle):
    matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle),  np.cos(angle), 0],
        [0, 0, 1]
    ])
    return [np.dot(matrix, [x, y, 1])[:2] for x, y in points]

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], 'bo-')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    global triangle
    triangle[:] = transform(triangle, angle_step)
    x, y = zip(*(triangle + [triangle[0]]))
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, update, frames=60, init_func=init, blit=True, interval=100)
plt.title("Rotating Triangle Animation")
plt.show()
