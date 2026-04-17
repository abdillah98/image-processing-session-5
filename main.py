import cv2
import matplotlib.pyplot as plt
from noise import add_salt_pepper_noise

# 1. Load Gambar
img = cv2.imread('image.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Konversi ke RGB untuk Matplotlib

# --- BAGIAN PROSES FILTER (Ubah di sini sesuai tugas kelompok) ---
# Contoh untuk Kelompok 1:

# blur1 = cv2.blur(img_rgb, (3, 3))
# blur2 = cv2.blur(img_rgb, (11, 11))
# blur3 = cv2.blur(img_rgb, (25, 25))

noisy_img = add_salt_pepper_noise(img_rgb, 0.05, 0.05)
median1 = cv2.medianBlur(noisy_img, 5)
# median2 = cv2.medianBlur(img_rgb, 11)

# sobel_x = cv2.Sobel(img_rgb, cv2.CV_64F, 1, 0, ksize=5)
# sobel_y = cv2.Sobel(img_rgb, cv2.CV_64F, 0, 1, ksize=5)

# bilateral1 = cv2.bilateralFilter(img_rgb, 9, 75, 75)
# bilateral2 = cv2.bilateralFilter(img_rgb, 9, 150, 150)

# gaussian1 = cv2.GaussianBlur(img_rgb, (3, 3), 0)
# gaussian2 = cv2.GaussianBlur(img_rgb, (11, 11), 0)
# gaussian3 = cv2.GaussianBlur(img_rgb, (25, 25), 0)

# canny = cv2.Canny(img_rgb, 50, 150)
# canny2 = cv2.Canny(img_rgb, 200, 250)

# -----------------------------------------------------------------

# 2. Tampilkan Perbandingan
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(img_rgb), plt.title('Gambar Asli')
plt.subplot(1, 3, 2), plt.imshow(noisy_img), plt.title('Salt and Pepper Noise')
plt.subplot(1, 3, 3), plt.imshow(median1), plt.title('Median Filter 5x5')

plt.show()