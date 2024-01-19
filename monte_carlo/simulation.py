import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import random
import numpy as np

def get_random_point(lower, upper):
    x = random.uniform(lower, upper)
    y = random.uniform(lower, upper)
    return x, y


def generate_random_points(amount):
    points = []
    for i in range(amount):
        points.append(get_random_point(0, 1))
    return points

def get_distance(x, y):
    return np.sqrt(np.power(x - 0, 2) + np.power(y - 0, 2) )

def main():
    center = (0, 0)
    radius = 1
    circle = Circle(center, radius, fill=False, color='black')
    square = Rectangle((-1, -1), 2, 2, fill=False)

    fig, ax = plt.subplots()

    points = generate_random_points(10)

    for point in points:
        plt.plot(point[0], point[1], 'bo')

    ax.set_xlim(0, 1.1)
    ax.set_ylim(0, 1.1)
    ax.grid(alpha=0.1)
    ax.add_patch(circle)
    ax.add_patch(square)
    ax.set_aspect('equal')

    plt.show()


if __name__ == '__main__':
    main()
