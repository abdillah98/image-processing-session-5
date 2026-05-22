import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load Gambar
img = cv2.imread('scan.jpeg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Konversi ke grayscale untuk Matplotlib

# Mengubah teks hitam menjadi putih, dan kertas putih menjadi hitam
# Angka 127 adalah nilai ambang (bisa disesuaikan dengan kontras gambar)
_, img_biner = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

# 2. MEMBUAT STRUCTURING ELEMENT (STREL)
# Membuat kernel berukuran 3x3 piksel berbentuk kotak penuh (Rectangular)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))


# 3. PROSES OPERASI MORFOLOGI DASAR
# A. Erosi (Erosion) -> Mengikis objek
erosion = cv2.erode(img_biner, kernel, iterations=1)

# B. Dilasi (Dilation) -> Menebalkan objek
dilation = cv2.dilate(img_biner, kernel, iterations=1)


# 4. PROSES OPERASI MORFOLOGI KOMBINASI
# C. Opening -> Erosi dulu baru Dilasi (Menghilangkan bintik putih di luar)
opening = cv2.morphologyEx(img_biner, cv2.MORPH_OPEN, kernel)

# D. Closing -> Dilasi dulu baru Erosi (Menutup lubang hitam di dalam)
closing = cv2.morphologyEx(img_biner, cv2.MORPH_CLOSE, kernel)


# 2. Tampilkan Perbandingan
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(img_biner, cmap='gray'), plt.title('Gambar Asli')
plt.subplot(1, 3, 2), plt.imshow(erosion, cmap='gray'), plt.title('Erosi')
plt.subplot(1, 3, 3), plt.imshow(dilation, cmap='gray'), plt.title('Dilasi')
# plt.subplot(1, 5, 4), plt.imshow(opening, cmap='gray'), plt.title('Opening')
# plt.subplot(1, 5, 5), plt.imshow(closing, cmap='gray'), plt.title('Closing')
plt.show()