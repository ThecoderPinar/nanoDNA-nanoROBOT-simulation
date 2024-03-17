import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Nanorobot:
    def __init__(self, position):
        self.position = np.array(position, dtype=float)
        self.history = [position]

    def move(self, displacement):
        new_position = self.position + np.array(displacement, dtype=float)
        self.position = new_position
        self.history.append(new_position)


def detect_target_molecules(genomic_sequence, target_sequence):
    # Genomik dizilimde hedef dizilimi arama
    target_start_index = genomic_sequence.find(target_sequence)

    if target_start_index != -1:
        print("Hedef dizilim bulundu. Başlangıç indeksi:", target_start_index)
        return target_start_index
    else:
        print("Hedef dizilim bulunamadı.")
        return None


# Genomik dizilim dosyasını okuma
genomic_sequence_file = "../data/GCA_000001405.29/GCA_000001405.29_GRCh38.p14_genomic.fna"

with open(genomic_sequence_file, "r") as f:
    genomic_sequence = f.read()

# Örnek bir hedef dizilimi belirleyin
target_sequence = "ATCG"

# Hedef dizilimi algıla ve başlangıç indeksini al
target_start_index = detect_target_molecules(genomic_sequence, target_sequence)

# Nanorobotun başlangıç konumu
initial_position = [0, 0]

# Nanorobot örneğini oluştur
nanorobot = Nanorobot(initial_position)

# Animasyonu hazırla
fig, ax = plt.subplots()
line, = ax.plot([], [], 'ro-', linewidth=2, markersize=5)  # Nanorobotun izini çizmek için çizgi ekleyin
target_line, = ax.plot([], [], 'g-', linewidth=1)  # Hedef dizilim için daha belirgin bir çizgi ekleyin

# Hedef dizilimi vurgula
if target_start_index is not None:
    target_position = [target_start_index, 0]
    target_line.set_data([target_position[0], target_position[0]], [-10, 10])


def init():
    ax.set_title("Nanorobotun Konumu")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    return line, target_line


def update(frame):
    nanorobot.move([np.random.uniform(-1, 1), np.random.uniform(-1, 1)])
    line.set_data([pos[0] for pos in nanorobot.history], [pos[1] for pos in nanorobot.history])
    return line, target_line


# Animasyonu başlat
ani = FuncAnimation(fig, update, frames=iter(range(100)), init_func=init, blit=True, save_count=100,
                    cache_frame_data=False)
plt.show()

# Nanorobotun hareketlerini simüle et ve mesafeyi hesapla
total_distance = 0
for i in range(100):
    displacement = [np.random.uniform(-1, 1), np.random.uniform(-1, 1)]
    nanorobot.move(displacement)
    total_distance += np.linalg.norm(displacement)

# Nanorobotun hareketlerini görselleştir
plt.figure(figsize=(8, 6))
plt.plot([pos[0] for pos in nanorobot.history], [pos[1] for pos in nanorobot.history], 'b-')
plt.xlabel('X Pozisyonu')
plt.ylabel('Y Pozisyonu')
plt.title('Nanorobotun Hareketi')
plt.grid(True)
plt.show()

# Toplam mesafeyi ve ortalama hızı hesapla
average_speed = total_distance / 100
print("Toplam Mesafe:", total_distance)
print("Ortalama Hız:", average_speed)

# Analiz sonuçlarını dosyaya yaz
with open("analiz_sonuclari.txt", "w") as f:
    f.write("Toplam Mesafe: {:.2f}\n".format(total_distance))
    f.write("Ortalama Hız: {}\n".format(average_speed))

# Nanorobotun hareket mesafesinin dağılımını görselleştir
displacements = [np.linalg.norm(nanorobot.history[i + 1] - nanorobot.history[i]) for i in
                 range(len(nanorobot.history) - 1)]
plt.hist(displacements, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Hareket Mesafesi')
plt.ylabel('Frekans')
plt.title('Nanorobotun Hareket Mesafesi Dağılımı')
plt.grid(True)
plt.show()

# Hedef diziliminin genomik dizilimdeki konumunun istatistiklerini hesapla
if target_start_index is not None:
    genomic_length = len(genomic_sequence)
    target_position = target_start_index / genomic_length
    print("Hedef diziliminin genomik dizilimdeki konumu: {:.2f}".format(target_position))

# Nanorobotun ortalama hızının zaman içindeki değişimini görselleştir
time = np.linspace(0, 1, len(nanorobot.history) - 1)  # 0'dan 1'e normalleştirilmiş zaman dizisi
speeds = [np.linalg.norm(nanorobot.history[i + 1] - nanorobot.history[i]) for i in range(len(nanorobot.history) - 1)]
plt.plot(time, speeds, 'r-')
plt.xlabel('Zaman')
plt.ylabel('Hız')
plt.title('Nanorobotun Ortalama Hızı')
plt.grid(True)
plt.show()

# Hedef Dizilimi İle Mesafe Analizi
target_distance = np.linalg.norm(target_position - nanorobot.position)
print("Hedef Dizilimine Mesafe:", target_distance)

# Baz Kompozisyonu Analizi
base_counts = {base: genomic_sequence.count(base) for base in 'ATCG'}
print("Baz Sayıları:", base_counts)


# Hedef Dizilimine Yakınlık Analizi
def distance_to_target(genomic_sequence, target_sequence, current_position):
    target_start_index = genomic_sequence.find(target_sequence)
    if target_start_index != -1:
        target_position = [target_start_index, 0]
        distance = np.linalg.norm(np.array(target_position) - np.array(current_position))
        return distance
    else:
        return None


# Nanorobotun Yolu ve Rotası
def plot_robot_path(history):
    x = [pos[0] for pos in history]
    y = [pos[1] for pos in history]
    plt.plot(x, y, 'b-', linewidth=1)
    plt.scatter(x[0], y[0], color='g', marker='o', label='Start')
    plt.scatter(x[-1], y[-1], color='r', marker='o', label='End')
    plt.title('Nanorobot Yolu ve Rotası')
    plt.xlabel('X Koordinatı')
    plt.ylabel('Y Koordinatı')
    plt.legend()
    plt.grid(True)
    plt.show()


# Hız Dağılımı Analizi
def plot_speed_distribution(speeds):
    plt.hist(speeds, bins=10, color='skyblue', edgecolor='black')
    plt.title('Hız Dağılımı')
    plt.xlabel('Hız')
    plt.ylabel('Frekans')
    plt.grid(True)
    plt.show()


# Analiz sonuçlarını dosyaya yaz
with open("analiz_sonuclari.txt", "a") as f:
    f.write("Hedef Dizilimine Mesafe: {} mevcut sonuçlar\n".format(
        distance_to_target(genomic_sequence, target_sequence, nanorobot.position)))
    f.write("Nanorobotun Yolu ve Rotası: analiz_sonuclari.txt dosyasına bakınız\n")
    f.write("Hız Dağılımı Analizi: analiz_sonuclari.txt dosyasına bakınız\n")

# Analiz sonuçlarını görselleştirme
plot_robot_path(nanorobot.history)
plot_speed_distribution(speeds)