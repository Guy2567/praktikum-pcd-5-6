"""
2.a Mirroring vertikal dan horizontal dilakukan secara bersamaan
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
both = np.zeros_like(image)

# Satu kali perulangan: baris dibalik (vertikal) DAN kolom dibalik (horizontal)
for y in range(height):
    for x in range(width):
        both[y, x] = image[height - 1 - y, width - 1 - x]

plt.figure(figsize=(10, 7))

plt.subplot(1, 2, 1)
plt.title("Asli")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Vertikal + Horizontal bersamaan")
plt.imshow(both)

plt.savefig(os.path.join(BASE, "hasil_2a_mirroring_bersamaan.png"), dpi=100)
plt.show()
