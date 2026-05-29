import cv2
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 1. LOAD GAMBAR
# =========================
img = cv2.imread('assets/image-coin.png')
# img = cv2.imread('assets/image-coin-2.jpg')
# img = cv2.imread('assets/image.png')
# img = cv2.imread('assets/image-coin.png')

# Convert BGR ke RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# =========================
# 2. PREPROCESSING
# =========================

# Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gaussian Blur untuk reduksi noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# =========================
# 3. SEGMENTASI
# =========================

# Thresholding
_, thresh = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# =========================
# 4. DETEKSI CONTOUR
# =========================

contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# =========================
# 5. EKSTRAKSI FITUR
# =========================

jumlah_objek = 0

for cnt in contours:

    # Hitung luas area contour
    area = cv2.contourArea(cnt)

    # Filter noise kecil
    if area > 2000:

        jumlah_objek += 1

        # Bounding Box
        x, y, w, h = cv2.boundingRect(cnt)

        # Gambar kotak
        cv2.rectangle(
            img_rgb,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            2
        )

        # Tampilkan luas area
        cv2.putText(
            img_rgb,
            f'Area: {int(area)}',
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2
        )

# =========================
# 6. TAMPILKAN HASIL
# =========================

plt.figure(figsize=(12,6))

# Threshold
plt.subplot(1,2,1)
plt.imshow(thresh, cmap='gray')
plt.title('Hasil Segmentasi')

# Hasil akhir
plt.subplot(1,2,2)
plt.imshow(img_rgb)
plt.title(f'Jumlah Objek: {jumlah_objek}')

plt.show()