import cv2
import matplotlib.pyplot as plt

# 1. Load Gambar
img = cv2.imread('image.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Konversi ke RGB untuk Matplotlib

# --- BAGIAN PROSES FILTER (Ubah di sini sesuai tugas kelompok) ---
# Contoh untuk Kelompok 1:
hasil = cv2.blur(img_rgb, (5, 5))
# -----------------------------------------------------------------

# 2. Tampilkan Perbandingan
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(img_rgb), plt.title('Gambar Asli')
plt.subplot(122), plt.imshow(hasil), plt.title('Hasil Filter')
plt.show()