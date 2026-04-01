# Item Service (Resource Management) 📦

Service ini khusus menangani operasional barang atau aset dalam sistem microservices. Service ini telah di-decouple (lepas) dari dependensi langsung ke model `User` untuk fleksibilitas di masa depan.

## 🛠️ Tanggung Jawab (Responsibility)

- **Manajemen Barang**: CRUD (Create, Read, Update, Delete) data barang.
- **Validasi Kepemilikan**: Memastikan hanya pemilik yang bisa mengubah/menghapus barang miliknya sendiri.

---

## 🚀 Cara Menjalankan Secara Lokal

Pastikan Anda memiliki [**uv**](https://docs.astral.sh/uv/) terinstal di mesin lokal Anda.

```bash
# 1. Masuk ke folder service
cd services/item-service

# 2. Sinkronkan dependensi
uv sync

# 3. Jalankan server pengembangan
uv run fastapi dev app/main.py
```

---

## 📐 Skema Tabel (Database)

Service ini mengelola tabel berikut:
- `items`: Berisi data judul, deskripsi, dan `owner_id` (UUID). 
  - **Catatan**: Hubungan ke tabel User sekarang dilakukan menggunakan `owner_id` (UUID) tanpa hubungan kunci asing SQL langsung untuk mendukung de-coupling pada level kode.

---

## 🧪 Pengujian (Testing)

```bash
uv run bash scripts/tests-start.sh
```
Laporan cakupan kode (coverage) akan dihasilkan secara otomatis di folder `htmlcov/`.
