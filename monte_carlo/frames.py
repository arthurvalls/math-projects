import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Function to generate a random point
def get_random_point(lower, upper):
    x = random.uniform(lower, upper)
    y = random.uniform(lower, upper)
    return x, y

# Function to update the plot
def update(frame):
    x, y = get_random_point(0, 1)
    plt.scatter(x, y, color='blue')
    plt.title(f'Point {frame + 1}')

# Set up the initial plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1.1)
ax.set_ylim(0, 1.1)
# Create the animation
num_frames = 50
animation = FuncAnimation(fig, update, frames=range(num_frames), interval=500)  # 50 frames, 500 milliseconds interval

# Show the plot
plt.show()
