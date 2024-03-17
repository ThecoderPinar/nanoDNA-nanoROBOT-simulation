import re
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Dosya yolunu doğrulayın
file_path = "../data/GCF_000001405.40/protein.faa"

try:
    # Dosyayı açın ve verileri yükleyin
    with open(file_path, "r") as f:
        data = f.read()

    # Protein dizilimlerini bulun
    protein_seqs = re.findall(r"\n(\w+)", data)

    # Protein dizilimlerinin uzunluklarını hesaplayın
    protein_lengths = [len(seq) for seq in protein_seqs]

    # En uzun ve en kısa protein uzunluklarını bulun
    max_protein_length = max(protein_lengths)
    min_protein_length = min(protein_lengths)

    # Ortalama protein uzunluğunu hesaplayın
    average_protein_length = sum(protein_lengths) / len(protein_lengths)

    # Proteinlerdeki amino asit dağılımını hesaplayın
    amino_acids = "".join(protein_seqs)
    amino_acid_counts = Counter(amino_acids)

    # En sık kullanılan 10 amino asiti bulun
    top_amino_acids = amino_acid_counts.most_common(10)

    # Verileri görselleştirin
    # Protein uzunluklarının histogramını çizin
    plt.figure(figsize=(10, 6))
    plt.hist(protein_lengths, bins=20, color='skyblue', edgecolor='black')
    plt.title('Protein Uzunluk Dağılımı')
    plt.xlabel('Protein Uzunluğu')
    plt.ylabel('Frekans')
    plt.grid(True)
    plt.show()

    # En sık kullanılan 10 amino asidi çubuk grafikle çizin
    plt.figure(figsize=(10, 6))
    plt.bar(*zip(*top_amino_acids), color='salmon')
    plt.title('En Sık Kullanılan Amino Asitler')
    plt.xlabel('Amino Asit')
    plt.ylabel('Frekans')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

    # Sonuçları raporlayın
    print("Toplam Protein Sayısı:", len(protein_seqs))
    print("En Uzun Protein Uzunluğu:", max_protein_length)
    print("En Kısa Protein Uzunluğu:", min_protein_length)
    print("Ortalama Protein Uzunluğu:", average_protein_length)
    print("En Sık Kullanılan Amino Asitler:")
    for amino_acid, count in top_amino_acids:
        print(f"{amino_acid}: {count}")

except FileNotFoundError:
    print("Belirtilen dosya bulunamadı.")
# Özellikler ve hedef değişkenleri ayırın
X = pd.DataFrame(protein_lengths, columns=["protein_length"])
y = pd.Series(["Human"] * len(protein_lengths))  # Etiketleri buraya yazın

# Eğitim ve test veri setlerini oluşturun
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest sınıflandırıcı modelini oluşturun
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Modeli eğitin
rf_classifier.fit(X_train, y_train)

# Modeli test edin
y_pred = rf_classifier.predict(X_test)

# Modelin doğruluğunu değerlendirin
accuracy = accuracy_score(y_test, y_pred)
print("Model Doğruluğu:", accuracy)

# Sınıflandırma raporunu görselleştirin
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
report_df.drop(columns=['support'], inplace=True)
report_df.plot(kind='bar', figsize=(10, 6))
plt.title('Sınıflandırma Raporu')
plt.xlabel('Sınıf')
plt.ylabel('Değer')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()
plt.show()

# 1. Sınıf Dengesizliği Analizi
class_distribution = y.value_counts()
print("Sınıf Dağılımı:")
print(class_distribution)

# 2. Model Performansı
print("\nSınıflandırma Raporu:")
print(classification_report(y_test, y_pred))

# 3. Model Hiperparametre Ayarlaması
# Örnek: RandomForestClassifier için ağaç sayısı hiperparametresini optimize edelim
n_estimators_values = [50, 100, 150, 200]
for n_estimators in n_estimators_values:
    rf_classifier = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    rf_classifier.fit(X_train, y_train)
    y_pred = rf_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAğaç Sayısı: {n_estimators}, Doğruluk: {accuracy}")

# 4. Çapraz Doğrulama
from sklearn.model_selection import cross_val_score
cross_val_scores = cross_val_score(rf_classifier, X, y, cv=5)
print("\nÇapraz Doğrulama Skorları:")
print(cross_val_scores)

# 5. Aşırı Uydurma Analizi
train_accuracy = accuracy_score(y_train, rf_classifier.predict(X_train))
print("\nEğitim Verisi Doğruluğu:", train_accuracy)

# 6. Özellik Önem Sıralaması
feature_importances = rf_classifier.feature_importances_
feature_importance_df = pd.DataFrame({"Feature": X.columns, "Importance": feature_importances})
feature_importance_df = feature_importance_df.sort_values(by="Importance", ascending=False)
print("\nÖzellik Önem Sıralaması:")
print(feature_importance_df)

# 7. Model Karşılaştırması
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

models = {
    "RandomForestClassifier": RandomForestClassifier(),
    # "LogisticRegression": LogisticRegression(),  # Logistic Regression modelini kaldırın
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n{name} Doğruluk: {accuracy}")

