import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Nanorobot:
    def __init__(self, position=[0, 0, 0], dna_sequence=""):
        self.position = np.array(position, dtype=float)
        self.history = [position]
        self.dna_sequence = dna_sequence

    def move(self, displacement):
        new_position = self.position + np.array(displacement, dtype=float)
        self.position = new_position
        self.history.append(new_position)

    def recognize_target_sequence(self, target_sequence):
        if target_sequence in self.dna_sequence:
            return True
        else:
            return False

    def bind_to_target_sequence(self, target_sequence):
        if self.recognize_target_sequence(target_sequence):
            # Hedef dizilimine bağlanma işlevselliğinin simülasyonu
            pass

    def analyze_movement(self):
        # Nanorobotun hareketinin analizi
        distances = np.linalg.norm(np.diff(np.array(self.history), axis=0), axis=1)
        total_distance = np.sum(distances)
        average_speed = total_distance / len(self.history)
        return total_distance, average_speed


def visualize_simulation_results(nanorobot):
    history = np.array(nanorobot.history)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(history[:, 0], history[:, 1], history[:, 2], color='b', alpha=0.5, label='Nanorobot Yolu')
    ax.scatter(history[0, 0], history[0, 1], history[0, 2], color='g', marker='o', s=100, label='Başlangıç Noktası')
    ax.scatter(history[-1, 0], history[-1, 1], history[-1, 2], color='r', marker='o', s=100, label='Bitiş Noktası')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.title('Nanorobot Hareketi')
    plt.show()


def main():
    dna_sequence = "ATCGATCGATCGATCG"
    nanorobot = Nanorobot(dna_sequence=dna_sequence)
    for _ in range(100):
        nanorobot.move(np.random.uniform(-1, 1, size=3))
    total_distance, average_speed = nanorobot.analyze_movement()
    print("Toplam Mesafe:", total_distance)
    print("Ortalama Hız:", average_speed)
    visualize_simulation_results(nanorobot)


if __name__ == "__main__":
    main()
