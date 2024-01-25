import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

def recaman(n):
    seq = []
    for i in range(n + 1):
        if i == 0:
            seq.append(0)
        else:
            next_value = seq[i - 1] - i
            if next_value < 0 or next_value in seq:
                next_value = seq[i - 1] + i
            seq.append(next_value)
    return seq


def generate_arcs(my_list, ax):
    for i in range(len(my_list) - 1):
        x1, y1 = i, my_list[i]
        x2, y2 = i + 1, my_list[i + 1]

        # Calculate the radius and angle of the arc
        radius = abs(y2 - y1) / 2
        angle = np.sign(y2 - y1) * 180

        # Determine the center of the arc
        center = ((x1 + x2) / 2, (y1 + y2) / 2)

        dir = 0 if ((my_list[i + 1]) - my_list[i]) > 0 else 180

        # Plot the arc
        arc = Arc(center, 2 * radius, 2 * radius, angle=dir, theta1=0, theta2=angle)
        ax.add_patch(arc)
        plt.scatter(my_list[i],my_list[i], color='r')


def main():
    limit = 10
    recaman_sequence = recaman(limit)
    

    fig, ax = plt.subplots()
    generate_arcs(recaman_sequence, ax)
    ax.set_xlim(0, len(recaman_sequence) - 1)
    ax.set_ylim(min(recaman_sequence) - 1, max(recaman_sequence) + 1)
    plt.title('recaman_sequence')
    plt.show()

if __name__ == "__main__":
	main()