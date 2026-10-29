# Praktikum PCD Sesi 5, 6 - Transformasi Geometri Citra

**Nama:** M. Jafar Sodik  
**NIM:** 20240040062  
**Kelas:** H Cyber Security  
**Mata Kuliah:** Pengolahan Citra Digital

Semua program memakai Python (`numpy`, `imageio`, `matplotlib`) dan gambar sumber `gambar/source.jpg` (480 x 680 px).

## Struktur folder

| No. | Folder | Isi |
|---|---|---|
| 1.a | `1a_translasi/` | Translasi citra (`np.roll` + isi hitam) |
| 1.b | `1b_mirroring/` | Mirroring horizontal dan vertikal (terpisah) |
| 1.c | `1c_rotasi/` | Rotasi 45 derajat, pivot di tengah citra |
| 1.d | `1d_zooming/` | Zoom plus (memperbesar) 2x |
| 2.a | `2a_mirroring_bersamaan/` | Mirroring vertikal + horizontal sekaligus dalam satu perulangan |
| 2.b | `2b_rotasi_pivot_0_0/` | Rotasi 45 derajat dengan pivot (0,0) pojok kiri atas |
| 2.c | `2c_zoom_minus/` | Zoom minus (memperkecil) 2x |

Tiap folder berisi kode program (`.py`) dan screenshot hasil program (`hasil_*.png`). Gambar sumber ada di folder `gambar/`, dan gambar hasil zoom disimpan sebagai `z.jpg` (1.d) dan `zm.jpg` (2.c).

## Cara menjalankan

```bash
pip install numpy imageio matplotlib
python 1a_translasi/translasi.py
```

## Catatan

- Zoom plus (1.d): ukuran hasil = ukuran asli x faktor, piksel diambil dari koordinat (y / faktor, x / faktor).
- Zoom minus (2.c): ukuran hasil = ukuran asli / faktor, piksel diambil dari koordinat (y x faktor, x x faktor).
- Rotasi (1.c dan 2.b) memakai pemetaan maju (forward mapping), sehingga pada sudut tertentu dapat muncul titik-titik kosong kecil pada hasil.
