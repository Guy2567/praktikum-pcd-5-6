"""
1.b Mirroring
Nama  : M. Jafar Sodik
NIM   : 20240040062
Kelas : H Cyber Security
Mata Kuliah: Pengolahan Citra Digital - Praktikum Sesi 5, 6
"""
import os
import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(BASE, "..", "gambar", "source.jpg")
image = img.imread(path)

height, width = image.shape[:2]
horizontal = np.zeros_like(image)
vertical = np.zeros_like(image)

# Mirroring horizontal (cermin kiri-kanan)
for y in range(height):
    for x in range(width):
        horizontal[y, x] = image[y, width - 1 - x]

# Mirroring vertikal (cermin atas-bawah)
for y in range(height):
    for x in range(width):
        vertical[y, x] = image[height - 1 - y, x]

plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.title("Asli")
plt.imshow(image)

plt.subplot(1, 3, 2)
plt.title("Horizontal")
plt.imshow(horizontal)

plt.subplot(1, 3, 3)
plt.title("Vertikal")
plt.imshow(vertical)

plt.savefig(os.path.join(BASE, "hasil_1b_mirroring.png"), dpi=100)
plt.show()
