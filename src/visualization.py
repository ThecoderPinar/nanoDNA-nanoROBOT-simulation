import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def visualize_movement_2d(history):
    fig, ax = plt.subplots()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Nanorobot Movement')

    def update(frame):
        ax.clear()
        ax.plot(history[:frame, 0], history[:frame, 1], color='b')
        ax.scatter(history[frame, 0], history[frame, 1], color='r', marker='o')

    anim = FuncAnimation(fig, update, frames=len(history), interval=100)
    plt.show()
