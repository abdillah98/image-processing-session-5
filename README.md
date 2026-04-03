# Praktikum Pengolahan Citra Digital (DIP) 📸
**Topik:** Implementasi Low-Pass Filter, High-Pass Filter, dan Smoothing.

Repositori ini berisi panduan dasar dan kode sumber untuk melakukan eksperimen manipulasi frekuensi citra digital menggunakan **Python** dan **OpenCV**. Proyek ini disusun untuk mempermudah mahasiswa dalam memahami perbedaan antara teknik penghalusan (*smoothing*) dan deteksi tepi (*edge detection*).

---

## 🚀 Persiapan Lingkungan (Setup)

Ikuti langkah-langkah di bawah ini untuk menyiapkan proyek di VS Code Anda:

### 1. Unduh Project
* Klik tombol **Code** (warna hijau) di halaman GitHub ini.
* Pilih **Download ZIP**.
* Ekstrak file ZIP tersebut ke folder di komputer Anda (misal: di Desktop atau Documents).
* Buka VS Code, pilih menu **File > Open Folder**, dan arahkan ke folder hasil ekstrak tadi.

### 2. Buat & Aktifkan Virtual Environment (venv)
Gunakan *Virtual Environment* agar library proyek tetap terisolasi dan tidak merusak Python utama.

* **Buka Terminal di VS Code** (`Ctrl + ` `).
* **Ketik perintah berikut (Windows):**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
* **Ketik perintah berikut (macOS/Linux):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
* *Tanda Berhasil:* Muncul tulisan `(venv)` di depan baris perintah terminal.

### 3. Instalasi Library
Jalankan perintah berikut di terminal VS Code untuk menginstal pustaka yang diperlukan:
```bash
pip install opencv-python matplotlib
```

### 4. Jalankan Kode
Ketikan perintah berikut untuk menjalankan code
```bash
python main.py
```