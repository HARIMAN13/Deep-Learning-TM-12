# Deep-Learning-TM-12

Repository ini berisi pengerjaan tugas Praktikum Pembelajaran Mesin (Minggu 12) mengenai **Deep Learning (Artificial Neural Network)** menggunakan **TensorFlow** dan **Keras**.

## Identitas Mahasiswa
- **Nama** : Rafi Hariman Priambodo
- **NIM** : 434241115
- **Kelas** : C7
- **Program Studi** : D4 Teknik Informatika
- **Fakultas** : Fakultas Vokasi, Universitas Airlangga

---

## Deskripsi Tugas & Alur Kerja
Tugas ini menerapkan klasifikasi biner menggunakan model *Multilayer Perceptron (Sequential)* dengan 12 tahapan:
1. **Import Library**: TensorFlow, Keras, Scikit-Learn, Pandas, NumPy, Seaborn, Matplotlib.
2. **Load Dataset**: Membaca data pengamatan dari `BlaBla.xlsx`.
3. **Pemisahan Fitur & Label**: Input variabel `Umur`, `B` s/d `M` (13 fitur), Output variabel target `N` (biner).
4. **Encoding Variabel Umur**:
   - `1`: Umur $\le 20$
   - `2`: $21 \le \text{Umur} \le 30$
   - `3`: $31 \le \text{Umur} \le 40$
   - `4`: $41 \le \text{Umur} \le 50$
   - `5`: $\text{Umur} > 50$
5. **Data Preprocessing**: Deteksi dan penanganan nilai anomali/missing value pada kolom `UMUR_TAHUN`, serta deteksi outlier dengan metode IQR.
6. **Data Splitting & Standarisasi**: Pembagian data 80% Train dan 20% Test, dilanjutkan dengan standarisasi fitur menggunakan `StandardScaler`.
7. **Arsitektur Model**:
   - Layer 1: Dense 16 unit, aktivasi ReLU (`input_shape=(13,)`)
   - Layer 2: Dense 8 unit, aktivasi ReLU
   - Layer Output: Dense 1 unit, aktivasi Sigmoid
8. **Compile & Train**: Optimizer Adam, loss `binary_crossentropy`, metrik `accuracy`, dilatih selama 100 epoch dengan validasi 20%.
9. **Evaluasi**: Evaluasi performa model pada data uji.
10. **Confusion Matrix**: Perhitungan matriks konfusi data uji.
11. **Visualisasi Heatmap**: Heatmap confusion matrix menggunakan Seaborn (*Blues*).
12. **Classification Report**: Laporan evaluasi Precision, Recall, dan F1-Score.

---

## Hasil Kinerja Model

- **Akurasi Data Uji**: **95.24%**
- **Loss Data Uji**: **0.134**

| Kelas Target | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **0 (Negatif)** | 0.97 | 0.97 | 0.97 | 326 |
| **1 (Positif)** | 0.92 | 0.92 | 0.92 | 136 |
| **Accuracy** | | | **0.95** | 462 |
| **Macro Avg** | 0.94 | 0.94 | 0.94 | 462 |
| **Weighted Avg** | 0.95 | 0.95 | 0.95 | 462 |

---

## Struktur File Repository
- `deep_learning.py` : Script program Python utama (bersih tanpa inline comments).
* `BlaBla.xlsx` : Dataset input tugas.
* `Pertemuan 11- Deep Learning.pdf` : Panduan modul dan instruksi tugas dosen.
* `confusion_matrix.png` : Visualisasi output heatmap Confusion Matrix.
* `Laporan_Deep_Learning_434241115.pdf` : Laporan resmi praktikum dalam format PDF.
* `Laporan_Deep_Learning_434241115.docx` : Laporan resmi praktikum dalam format Word.
* `Deep Learning_434241115.zip` : Berkas arsip pengumpulan e-learning (HEBAT).
