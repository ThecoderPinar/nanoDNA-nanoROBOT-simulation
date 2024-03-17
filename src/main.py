# Ana kütüphaneleri içe aktarın
import nanorobot
import dna_interaction
import motion_simulation
import energy_management
import visualization


def main():
    # Nanorobot oluşturma ve başlangıç konumunu belirleme
    nanobot = nanorobot.Nanorobot()
    nanobot.set_initial_position(x=0, y=0, z=0)

    # DNA etkileşimi simülasyonunu başlatma
    dna_interaction.simulate_interaction(nanobot)

    # Hareket simülasyonunu başlatma
    motion_simulation.simulate_motion(nanobot)

    # Enerji yönetimi algoritmalarını uygulama
    energy_management.apply_energy_management(nanobot)

    # Sonuçları görselleştirme
    visualization.visualize_results(nanobot)


if __name__ == "__main__":
    main()
