<div align="center">

# 🖩 Kalkulator GUI + Text-to-Voice

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Repo Size](https://img.shields.io/github/repo-size/useripx/08-Kalkulator-GUI?style=for-the-badge&color=blue)
![License](https://img.shields.io/badge/License-Free-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Selesai-brightgreen?style=for-the-badge)
![Semester](https://img.shields.io/badge/Semester-1-blueviolet?style=for-the-badge)

**Kalkulator dengan antarmuka grafis (GUI) menggunakan Tkinter, dilengkapi fitur Text-to-Voice.**

*Dibuat oleh Yogi Ario — Proyek Semester 1*

---

</div>

## 📖 Deskripsi

Proyek ini berisi dua aplikasi utama:

1. **Kalkulator GUI** (`calgui.py`) — Kalkulator dengan tampilan grafis menggunakan **Tkinter**, mendukung operasi aritmatika dasar dengan layout tombol mirip kalkulator fisik. Mendukung input melalui klik tombol maupun keyboard.

2. **Text-to-Voice** (`ttv.py`) — Aplikasi konversi teks ke suara menggunakan **pyttsx3** (offline TTS engine), mendukung suara Bahasa Indonesia.

## ✨ Fitur

### Kalkulator GUI (`calgui.py`)
- ➕ ➖ ✖️ ➗ Operasi dasar (tambah, kurang, kali, bagi)
- 🔢 Mendukung angka desimal
- ⌨️ **Keyboard binding** — input angka & operator langsung dari keyboard
- ⌫ **Backspace** — hapus karakter terakhir
- 🔄 Tombol **Clear (C)** — reset input
- ⚠️ **Error handling** — menampilkan popup error untuk input tidak valid
- 🖥️ Layout grid responsif mirip kalkulator fisik

### Text-to-Voice (`ttv.py`)
- 🔊 Konversi teks ke suara secara **offline**
- 🗣️ Mendukung suara **wanita Bahasa Indonesia**
- ⚡ Pengaturan kecepatan bicara (rate: 150)
- 🔁 Loop untuk input berulang

## 📁 Struktur Proyek

```
08 Kalkulatr GUI/
├── calgui.py              # Kalkulator GUI (Tkinter)
├── ttv.py                 # Text-to-Voice (pyttsx3)
├── main.py                # Entry point (import TTV)
├── mains.py               # Entry point eksperimen
├── coba.py                # File percobaan
├── img.ico                # Icon aplikasi
└── __pycache__/           # Cache Python
```

## 🚀 Cara Menjalankan

### Kalkulator GUI

```bash
python calgui.py
```

Akan terbuka jendela kalkulator dengan tampilan grafis. Bisa diklik tombol atau ketik langsung dari keyboard.

### Text-to-Voice

```bash
pip install pyttsx3
python ttv.py
```

## 📸 Tampilan Kalkulator

```
┌─────────────────────────┐
│                     0   │  ◄ Display
├───────┬───────┬───────┬─┤
│   C   │       │       │ ÷ │
├───────┼───────┼───────┼───┤
│   7   │   8   │   9   │ × │
├───────┼───────┼───────┼───┤
│   4   │   5   │   6   │ - │
├───────┼───────┼───────┼───┤
│   1   │   2   │   3   │ + │
├───────┼───────┼───────┴───┤
│   .   │   0   │     =     │
└───────┴───────┴───────────┘
```

### Keyboard Shortcut

| Key | Fungsi |
|-----|--------|
| `0-9` | Input angka |
| `+ - * /` | Operator |
| `.` | Desimal |
| `Enter` | Hitung (=) |
| `Backspace` | Hapus karakter terakhir |

## 📸 Contoh Text-to-Voice

```
Konversi Teks ke Suara

Masukkan teks yang ingin dikonversi menjadi suara (tekan Enter untuk keluar): Halo, selamat datang
🔊 (Suara: "Halo, selamat datang")

Masukkan teks yang ingin dikonversi menjadi suara (tekan Enter untuk keluar):
```

## 🛠️ Teknologi

| Komponen | Detail |
|----------|--------|
| Bahasa | Python 3.x |
| GUI Framework | Tkinter (built-in) |
| TTS Engine | pyttsx3 (offline) |
| Platform | Windows |

## 👤 Author & Kontak

**Yogi Ario Pratama**

Jika Anda memiliki pertanyaan seputar kode ini atau ingin berdiskusi, silakan hubungi saya melalui WhatsApp:
📱 **[Chat via WhatsApp (wa.me/6281358113087)](https://wa.me/6281358113087)**

---

### 💖 Donasi
Dukungan Anda sangat berarti agar saya dapat terus semangat belajar dan mengembangkan proyek-proyek open-source lainnya. Jika berkenan memberikan donasi/apresiasi, Anda dapat menyalurkannya melalui:

💳 **Bank Seabank**
- No Rekening: **901497113744**
- Atas Nama: **Yogi Ario Pratama**

<div align="center">
  <br>
  <em>Terima kasih atas kunjungannya. Proyek Mata Kuliah — Semester 1 — Teknik Informatika UNP</em>
</div>
