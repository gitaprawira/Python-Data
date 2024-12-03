# Import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style untuk visualisasi
sns.set(style="whitegrid")

# Load dataset
file_path = 'data/gym_membership.csv'
df = pd.read_csv(file_path)

# Langkah Pembersihan Data
# 1. Memeriksa Nilai Hilang
print("Jumlah nilai hilang di setiap kolom:")
print(df.isnull().sum())

# Mengisi nilai hilang di kolom yang bersifat kategorikal dengan 'Unknown'
df['fav_group_lesson'].fillna('Unknown', inplace=True)
df['fav_drink'].fillna('Unknown', inplace=True)
df['name_personal_trainer'].fillna('Unknown', inplace=True)

# Mengisi nilai hilang di kolom numerik dengan rata-rata (jika diperlukan)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['visit_per_week'].fillna(df['visit_per_week'].mean(), inplace=True)
df['avg_time_in_gym'].fillna(df['avg_time_in_gym'].mean(), inplace=True)

# 2. Menghapus Duplikasi
df.drop_duplicates(inplace=True)

# 3. Memastikan Tipe Data yang Benar
# Konversi kolom 'visit_per_week' dan 'avg_time_in_gym' ke tipe integer jika diperlukan
df['visit_per_week'] = df['visit_per_week'].astype(int)
df['avg_time_in_gym'] = df['avg_time_in_gym'].astype(int)

# 4. Menangani Data yang Tidak Valid
# Memfilter data untuk memastikan usia berada dalam rentang yang wajar (misalnya 10 hingga 100 tahun)
df = df[(df['Age'] >= 10) & (df['Age'] <= 100)]

# Menjaga frekuensi kunjungan mingguan antara 0 hingga 7
df = df[(df['visit_per_week'] >= 0) & (df['visit_per_week'] <= 7)]

# Menjaga durasi di gym per kunjungan dalam rentang yang wajar (misalnya, 0 hingga 300 menit)
df = df[(df['avg_time_in_gym'] >= 0) & (df['avg_time_in_gym'] <= 300)]

# Tampilkan data yang telah dibersihkan
print("\nData setelah pembersihan:")
print(df.info())
print(df.describe())

# Visualisasi Data setelah Pembersihan

# Visualisasi 1: Distribusi Usia Anggota Gym
plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribusi Usia Anggota Gym")
plt.xlabel("Usia")
plt.ylabel("Jumlah Anggota")
plt.show()

# Visualisasi 2: Frekuensi Kunjungan Gym Per Minggu
plt.figure(figsize=(8, 5))
sns.countplot(x='visit_per_week', data=df, palette="viridis")
plt.title("Frekuensi Kunjungan Gym Per Minggu")
plt.xlabel("Kunjungan per Minggu")
plt.ylabel("Jumlah Anggota")
plt.show()

# Visualisasi 3: Durasi Waktu di Gym per Kunjungan
plt.figure(figsize=(8, 5))
plt.hist(df['avg_time_in_gym'], bins=10, color='salmon', edgecolor='black')
plt.title("Durasi Waktu di Gym per Kunjungan")
plt.xlabel("Waktu di Gym (menit)")
plt.ylabel("Jumlah Anggota")
plt.show()

# Visualisasi 4: Preferensi terhadap Kelas Kelompok
group_class_count = df['attend_group_lesson'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(group_class_count, labels=['Mengikuti', 'Tidak Mengikuti'], autopct='%1.1f%%', startangle=140, colors=['#66c2a5', '#fc8d62'])
plt.title("Preferensi Mengikuti Kelas Kelompok")
plt.show()

# Visualisasi 5: Penggunaan Pelatihan Pribadi
personal_training_count = df['personal_training'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(personal_training_count, labels=['Menggunakan', 'Tidak Menggunakan'], autopct='%1.1f%%', startangle=140, colors=['#8da0cb', '#e78ac3'])
plt.title("Preferensi Menggunakan Pelatihan Pribadi")
plt.show()
