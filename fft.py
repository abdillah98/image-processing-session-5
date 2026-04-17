import cv2
import numpy as np
import matplotlib.pyplot as plt

def proses_fft(img):
    f = np.fft.fft2(img)
    return np.fft.fftshift(f)

def balikkan_ke_gambar(fshift_filtered):
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    return np.abs(img_back)

img = cv2.imread('image.png', 0)
fshift = proses_fft(img)
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2

# --- EKSPERIMEN MAHASISWA ---
radius = 30

# 1. Membuat Mask LPF (Lingkaran Putih di tengah)
mask_lpf = np.zeros((rows, cols), np.uint8)
cv2.circle(mask_lpf, (ccol, crow), radius, 1, -1)

# 2. Membuat Mask HPF (Kebalikan LPF: Lingkaran Hitam di tengah)
mask_hpf = 1 - mask_lpf 

# Proses Filter
hasil_lpf = balikkan_ke_gambar(fshift * mask_lpf)
hasil_hpf = balikkan_ke_gambar(fshift * mask_hpf)

# Tampilkan Hasil
plt.figure(figsize=(15, 5))
plt.subplot(151), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(152), plt.imshow(hasil_lpf, cmap='gray'), plt.title(f'Low-Pass (Radius {radius})')
plt.subplot(153), plt.imshow(hasil_hpf, cmap='gray'), plt.title(f'High-Pass (Radius {radius})')
plt.subplot(154), plt.imshow(mask_lpf, cmap='gray'), plt.title(f'Low-Pass Mask')
plt.subplot(155), plt.imshow(mask_hpf, cmap='gray'), plt.title(f'High-Pass Mask')
plt.show()