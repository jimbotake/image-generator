
# 🎨 Image Generator (Stable Diffusion + Streamlit, CPU Ready)

Aplikasi web sederhana untuk menghasilkan gambar dari teks (text-to-image generation) menggunakan [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5) dan Streamlit. Dirancang agar ringan dan dapat dijalankan di laptop/PC tanpa GPU (CPU only).

---

## 🚀 Demo

Masukkan prompt → Klik tombol → Gambar akan dihasilkan oleh model Stable Diffusion.

> Contoh prompt: `a mystical forest with glowing mushrooms, digital art`

---

## ✨ Fitur

- ✅ Input teks bebas untuk membuat gambar
- 🧠 Menggunakan model: `runwayml/stable-diffusion-v1-5` (kompatibel CPU)
- ⚙️ Bisa dijalankan secara lokal tanpa GPU
- 🧱 Dibuat dengan Streamlit, Diffusers, dan PyTorch

---

## 📦 Cara Instalasi

### 1. Clone repo

```bash
git clone https://github.com/jimbotake/image-generator.git
cd image-generator
```

### 2. Buat environment Conda

```bash
conda env create -f environment.yml
conda activate image-generator
```

### 3. Jalankan aplikasi

```bash
streamlit run app.py
```

---

## 📁 Struktur Folder

```
image-generator/
│
├── app.py
├── README.md
├── environment.yml
├── requirements.txt         # (optional)
├── .gitignore
```

---

## 📌 Catatan

- Proses generate pertama kali mungkin lambat (download model ±4 GB)
- Pipeline menggunakan `torch.float32` untuk CPU
- Setelah model di-cache, proses jauh lebih cepat

---

## 📝 Lisensi

MIT License © 2025 [Dimas Sony Dewantara]
