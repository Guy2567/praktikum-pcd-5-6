"""
1.a Translasi Citra
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


def Translasi(image, shiftX, shiftY):

    imgTranslasi = np.roll(image, shift=shiftY, axis=0)  # Geser vertikal
    imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1)  # Geser horizontal

    # Mengisi bagian yang kosong dengan warna hitam (0)
    if shiftY > 0:
        imgTranslasi[:shiftY, :] = 0  # Bagian atas jika geser ke bawah
    elif shiftY < 0:
        imgTranslasi[shiftY:, :] = 0  # Bagian bawah jika geser ke atas
    if shiftX > 0:
        imgTranslasi[:, :shiftX] = 0  # Bagian kiri jika geser ke kanan
    elif shiftX < 0:
        imgTranslasi[:, shiftX:] = 0  # Bagian kanan jika geser ke kiri

    return imgTranslasi


image = img.imread(os.path.join(BASE, "..", "gambar", "source.jpg"))

imgResult = Translasi(image, shiftX=50, shiftY=-150)

plt.figure(figsize=(10, 8))
plt.subplot(1, 2, 1)
plt.title("Citra asli")
plt.imshow(image)
plt.subplot(1, 2, 2)
plt.title("Translasi (shiftX=50, shiftY=-150)")
plt.imshow(imgResult)
plt.savefig(os.path.join(BASE, "hasil_1a_translasi.png"), dpi=100)
plt.show()
