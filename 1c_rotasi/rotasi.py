"""
1.c Rotasi Citra (pivot di tengah citra)
Nama  : M. Jafar Sodik
NIM   : 20240040062
Kelas : H Cyber Security
Mata Kuliah: Pengolahan Citra Digital - Praktikum Sesi 5, 6
"""
import os
import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))


def rotateImage(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)

    height, width = image.shape[:2]
    max_dim = int(np.sqrt(height**2 + width**2))
    outputImage = np.zeros((max_dim, max_dim, 3), dtype=image.dtype)

    centerY, centerX = max_dim // 2, max_dim // 2

    for y in range(-height // 2, height // 2):
        for x in range(-width // 2, width // 2):
            newX = int(cos_deg * x - sin_deg * y) + centerX
            newY = int(sin_deg * x + cos_deg * y) + centerY

            if 0 <= newX < max_dim and 0 <= newY < max_dim:
                outputImage[newY, newX] = image[y + height // 2, x + width // 2]
    return outputImage


image = img.imread(os.path.join(BASE, "..", "gambar", "source.jpg"))

rotated_image = rotateImage(image, 45)

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.title("Citra asli")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Rotasi 45 derajat (pivot tengah)")
plt.imshow(rotated_image)

plt.savefig(os.path.join(BASE, "hasil_1c_rotasi.png"), dpi=100)
plt.show()
