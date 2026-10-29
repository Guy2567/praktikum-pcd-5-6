"""
2.b Rotasi Citra dengan pivot di titik (0,0) pojok kiri atas
Nama  : M. Jafar Sodik
NIM   : 20240040062
Kelas : H Cyber Security
Mata Kuliah: Pengolahan Citra Digital - Praktikum Sesi 5, 6

Rumus (sama dengan rotasi pivot tengah, tetapi x dan y dihitung dari pojok
kiri atas citra, tanpa pergeseran ke tengah kanvas):
    newX = cos(a) * x - sin(a) * y
    newY = sin(a) * x + cos(a) * y
Koordinat hasil bisa bernilai negatif, jadi ukuran kanvas dihitung dari
keempat sudut citra setelah dirotasi, dan sumbu gambar menampilkan koordinat
aslinya supaya pivot (0,0) terlihat.
"""
import os
import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))


def rotateImagePivot00(image, degree):
    radian_deg = np.radians(degree)
    cos_deg, sin_deg = np.cos(radian_deg), np.sin(radian_deg)

    height, width = image.shape[:2]

    # Hitung batas kanvas dari 4 sudut citra setelah dirotasi
    corners = [(0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1)]
    xs = [int(cos_deg * x - sin_deg * y) for x, y in corners]
    ys = [int(sin_deg * x + cos_deg * y) for x, y in corners]
    minX, maxX = min(xs), max(xs)
    minY, maxY = min(ys), max(ys)

    outputImage = np.zeros((maxY - minY + 1, maxX - minX + 1, 3), dtype=image.dtype)

    for y in range(height):
        for x in range(width):
            newX = int(cos_deg * x - sin_deg * y)  # pivot (0,0)
            newY = int(sin_deg * x + cos_deg * y)
            outputImage[newY - minY, newX - minX] = image[y, x]

    return outputImage, (minX, maxX, minY, maxY)


image = img.imread(os.path.join(BASE, "..", "gambar", "source.jpg"))
height, width = image.shape[:2]

rotated_image, (minX, maxX, minY, maxY) = rotateImagePivot00(image, 45)

plt.figure(figsize=(11, 7))

plt.subplot(1, 2, 1)
plt.title("Citra asli (pivot di (0,0))")
plt.imshow(image, extent=(-0.5, width - 0.5, height - 0.5, -0.5))
plt.plot(0, 0, "ro")
plt.xlim(minX - 10, max(maxX, width) + 10)
plt.ylim(max(maxY, height) + 10, minY - 10)

plt.subplot(1, 2, 2)
plt.title("Rotasi 45 derajat, pivot (0,0)")
plt.imshow(rotated_image, extent=(minX - 0.5, maxX + 0.5, maxY + 0.5, minY - 0.5))
plt.plot(0, 0, "ro")
plt.xlim(minX - 10, max(maxX, width) + 10)
plt.ylim(max(maxY, height) + 10, minY - 10)

plt.savefig(os.path.join(BASE, "hasil_2b_rotasi_pivot_0_0.png"), dpi=100)
plt.show()
