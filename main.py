import cv2
import matplotlib.pyplot as plt
from noise import add_salt_pepper_noise

# 1. Load Gambar
img = cv2.imread('image.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Konversi ke RGB untuk Matplotlib

# --- BAGIAN PROSES FILTER (Ubah di sini sesuai tugas kelompok) ---
# Contoh untuk Kelompok 1:


# noisy_img = add_salt_pepper_noise(img_rgb, 0.05, 0.05)
# median = cv2.medianBlur(img_rgb, 5)
# blur = cv2.blur(img_rgb, (3, 3))
# bilateral = cv2.bilateralFilter(img_rgb, 9, 75, 75)
# gaussian = cv2.GaussianBlur(img_rgb, (3, 3), 0)

canny = cv2.Canny(img_rgb, 50, 150)
# sobel = cv2.Sobel(img_rgb, cv2.CV_64F, 1, 0, ksize=5)

# -----------------------------------------------------------------

# 2. Tampilkan Perbandingan
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(img_rgb), plt.title('Gambar Asli')
plt.subplot(1, 2, 2), plt.imshow(canny), plt.title('Hasil Filter')

plt.show()