"""
1.d Zooming (Zoom Plus / memperbesar)
Nama  : M. Jafar Sodik
NIM   : 20240040062
Kelas : H Cyber Security
Mata Kuliah: Pengolahan Citra Digital - Praktikum Sesi 5, 6

Catatan: ukuran citra hasil = ukuran asli x faktor, dan tiap piksel hasil
mengambil piksel asli pada koordinat (y / faktor, x / faktor) (nearest neighbor).
"""
import os
import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))


def zoomPlus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):

            ori_y = int(y / factor)
            ori_x = int(x / factor)

            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)

            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom


image = img.imread(os.path.join(BASE, "..", "gambar", "source.jpg"))
skala = 2.0

imgZoom = zoomPlus(image, skala)
img.imwrite(os.path.join(BASE, "z.jpg"), imgZoom)

plt.figure(figsize=(10, 7))
plt.subplot(1, 2, 1)
plt.title("Citra asli %dx%d" % image.shape[:2][::-1])
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Zoom plus %.1fx -> %dx%d" % ((skala,) + imgZoom.shape[:2][::-1]))
plt.imshow(imgZoom)

plt.savefig(os.path.join(BASE, "hasil_1d_zooming.png"), dpi=100)
plt.show()
