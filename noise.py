import cv2
import numpy as np

# Fungsi menambahkan salt & pepper noise
def add_salt_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    noisy = image.copy()
    
    # Salt (putih)
    num_salt = np.ceil(salt_prob * image.size)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = 255

    # Pepper (hitam)
    num_pepper = np.ceil(pepper_prob * image.size)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape[:2]]
    noisy[coords[0], coords[1]] = 0

    return noisy


# # Baca gambar
# image = cv2.imread('image.png')  # ganti dengan path gambar Anda

# # Tambahkan noise
# noisy_image = add_salt_pepper_noise(image)

# # Reduksi noise dengan median filter
# denoised_image = cv2.medianBlur(noisy_image, 5)

# # Tampilkan hasil
# cv2.imshow('Original', image)
# cv2.imshow('Salt & Pepper Noise', noisy_image)
# cv2.imshow('After Median Filter', denoised_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()