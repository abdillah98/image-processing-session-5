import cv2
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 1. LOAD GAMBAR
# =========================
img = cv2.imread('assets/image-coin.png')

# Convert BGR ke RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# =========================
# 2. GRAYSCALE
# =========================
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# =========================
# 3. REDUKSI NOISE
# =========================
blur = cv2.GaussianBlur(gray, (9, 9), 0)

# =========================
# 4. THRESHOLDING
# =========================
_, thresh = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# =========================
# 5. MORFOLOGI
# =========================
kernel = np.ones((3,3), np.uint8)

morph = cv2.morphologyEx(
    thresh,
    cv2.MORPH_OPEN,
    kernel,
    iterations=2
)

# =========================
# 6. DETEKSI CONTOUR
# =========================
contours, _ = cv2.findContours(
    morph,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# =========================
# 7. FILTER & HITUNG OBJEK
# =========================
count = 0

for cnt in contours:

    area = cv2.contourArea(cnt)

    # Filter noise kecil
    if area > 500:

        count += 1

        # Gambar bounding box
        x, y, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(
            img_rgb,
            (x, y),
            (x+w, y+h),
            (255, 0, 0),
            2
        )

# =========================
# 8. TAMPILKAN HASIL
# =========================
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.imshow(morph, cmap='gray')
plt.title('Hasil Segmentasi')

plt.subplot(1,2,2)
plt.imshow(img_rgb)
plt.title(f'Jumlah Koin: {count}')

plt.show()