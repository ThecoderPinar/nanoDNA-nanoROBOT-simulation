import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


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
        total_moves = len(self.history) - 1
        return total_moves

    def calculate_distance_to_target(self, target_position):
        return np.linalg.norm(target_position - self.position)


def visualize_movement(nanorobot):
    history_array = np.array(nanorobot.history)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Y', fontsize=14)
    ax.set_zlabel('Z', fontsize=14)
    ax.set_title('Nanorobot Hareketi', fontsize=16)
    ax.plot(history_array[:, 0], history_array[:, 1], history_array[:, 2], color='b', alpha=0.5, label='Nanorobot Yolu')
    ax.scatter(history_array[0, 0], history_array[0, 1], history_array[0, 2], color='g', marker='o', s=100,
               label='Başlangıç Noktası')
    ax.scatter(history_array[-1, 0], history_array[-1, 1], history_array[-1, 2], color='r', marker='o', s=100,
               label='Bitiş Noktası')
    ax.legend()
    plt.show()


def main():
    dna_sequence = "ATCGATCGATCGATCG"
    target_position = np.array([10, 10, 10])
    nanorobot = Nanorobot(dna_sequence=dna_sequence)

    # Nanorobotun hareketi
    for _ in range(50):
        displacement = np.random.uniform(-1, 1, size=3)
        nanorobot.move(displacement)

    total_moves = nanorobot.analyze_movement()
    print("Toplam Hareket Sayısı:", total_moves)
    visualize_movement(nanorobot)

    # Hedefe olan uzaklık ve sınıflandırma
    distances = nanorobot.calculate_distance_to_target(target_position)
    print("Hedefe olan uzaklık:", distances)

    # Sınıflandırma modeli eğitimi ve performans değerlendirmesi
    X = np.array([distances]).reshape(-1, 1)
    y = np.array([1])  # Örnek etiket, gerektiğinde güncellenmeli
    model = RandomForestClassifier()
    model.fit(X, y)
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    report = classification_report(y, y_pred)
    print("Sınıflandırma Modeli Doğruluğu:", accuracy)
    print("Sınıflandırma Raporu:\n", report)


if __name__ == "__main__":
    main()

