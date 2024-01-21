import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.animation import FuncAnimation
import random

point = 0
blues = 0
reds = 0
def get_distance(x, y):
    return np.sqrt(np.power(x - 0, 2) + np.power(y - 0, 2))


def get_random_point(lower, upper):
    x = random.uniform(lower, upper)
    y = random.uniform(lower, upper)
    return x, y

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
animation = FuncAnimation(fig, update, frames=range(num_frames), interval=5) 
plt.show()
