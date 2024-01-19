import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import random
from matplotlib.lines import Line2D
import numpy as np

AMOUNT_POINTS = 1000


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
    return np.sqrt(np.power(x - 0, 2) + np.power(y - 0, 2))


def main():
    center = (0, 0)
    radius = 1
    circle = Circle(center, radius, fill=False, color='black')
    square = Rectangle((-1, -1), 2, 2, fill=False)

    fig, ax = plt.subplots()

    points = generate_random_points(AMOUNT_POINTS)
    reds = 0
    blues = 0
    total = 0

    for point in points:
        color = 'bo' if get_distance(point[0], point[1]) < 1 else 'ro'
        if color == 'ro':
            reds += 1
            total += 1
        else:
            blues += 1
            total += 1

        plt.plot(point[0], point[1], color)

    approx = 4 * blues / total

    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 1.5)
    ax.grid(alpha=0.1)
    ax.add_patch(circle)
    ax.add_patch(square)
    ax.set_aspect('equal')

    # Add legend
    legend_lines = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=5, label=f'{blues} Blues'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=5, label=f'{reds} Reds'),
        Line2D([0], [0], marker='o', color='black', label=f'Total: {total}'),
        Line2D([0], [0], marker='$\pi$', color='black', linewidth=0, label=f'Approx: {approx:.4f}')
    ]
    ax.legend(handles=legend_lines, loc='upper right', bbox_to_anchor=(1, 1), prop={'size': 8})

    plt.show()


if __name__ == '__main__':
    main()
