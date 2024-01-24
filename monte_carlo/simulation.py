import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
import random
import argparse

point = 0
blues = 0
reds = 0

def get_distance(x, y):
    return np.sqrt(np.power(x - 0, 2) + np.power(y - 0, 2))

def get_random_point(lower, upper):
    x = random.uniform(lower, upper)
    y = random.uniform(lower, upper)
    return x, y

def generate_random_points(amount):
    points = []
    for i in range(amount):
        points.append(get_random_point(0, 1))
    return points

def update(frame):
    global point  
    global reds
    global blues
    x, y = get_random_point(0, 1)
    color = 'blue' if get_distance(x, y) < 1 else 'red'
    if color == 'blue':
        blues += 1
    else:
        reds += 1
    plt.scatter(x, y, color=color)
    plt.title(f'Random points PI approximation')
    point += 1
    plt.legend([f"n of points: {point}", f"blues = {blues}", f"reds = {reds}", f"pi approximation = {blues*4/(blues+reds):.2f}"], bbox_to_anchor=(1, 1), markerscale=0)

def main():
    parser = argparse.ArgumentParser(description='Approximate pi using random points.')
    parser.add_argument('--animation', type=bool, default=False, help='Number of points to plot')
    args = parser.parse_args()   

    circle = Circle((0, 0), 1, fill=False, color='black')
    square = Rectangle((-1, -1), 2, 2, fill=False)

    fig, ax = plt.subplots()
    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 1.5)
    ax.grid(alpha=0.1)
    ax.add_patch(circle)
    ax.add_patch(square)
    ax.set_aspect('equal')
    num_frames = 10000
    
    if args.animation:
        animation = FuncAnimation(fig, update, frames=range(num_frames), interval=5) 
        plt.show()
    else:
        AMOUNT_POINTS = 1000  # Define the number of points
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
        legend_lines = [
            Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=5, label=f'{blues} Blues'),
            Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=5, label=f'{reds} Reds'),
            Line2D([0], [0], marker='o', color='black', label=f'Total: {total}'),
            Line2D([0], [0], marker='$\pi$', color='black', linewidth=0, label=f'Approx: {approx:.4f}')
        ]
        ax.legend(handles=legend_lines, loc='upper right', bbox_to_anchor=(1, 1), prop={'size': 8})
        plt.show()

if __name__ == "__main__":
    main()
