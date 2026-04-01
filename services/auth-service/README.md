# Auth Service (Identity & Access Management) 🛡️

Service ini bertanggung jawab untuk menangani seluruh proses autentikasi, otorisasi, dan manajemen profil pengguna di dalam ekosistem microservices Docker Compose ini.

## 🛠️ Tanggung Jawab (Responsibility)

- **Registrasi & Login**: Manajemen token JWT (Login, Password Recovery, dll).
- **User Management**: Operasi CRUD untuk data pengguna (halaman admin).
- **Utilities**: Health-check sistem dan pembersihan data temporer.

---

## 🚀 Cara Menjalankan Secara Lokal

Pastikan Anda memiliki [**uv**](https://docs.astral.sh/uv/) terinstal di mesin lokal Anda.

```bash
# 1. Masuk ke folder service
cd services/auth-service

# 2. Sinkronkan dependensi
uv sync

# 3. Jalankan server pengembangan
uv run fastapi dev app/main.py
```

---

## 📐 Skema Tabel (Database)

Service ini mengelola tabel berikut di database PostgreSQL bersama:
- `users`: Data identitas pengguna dan kredensial terenkripsi.

---

## 🧪 Pengujian (Testing)

```bash
uv run bash scripts/tests-start.sh
```
Laporan cakupan kode (coverage) akan dihasilkan secara otomatis di folder `htmlcov/`.
