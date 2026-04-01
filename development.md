# Panduan Pengembangan Microservices 🛠️

Dokumen ini menjelaskan cara mengembangkan, menguji, dan menjalankan microservices secara lokal.

## 🐋 1. Menjalankan Stack Lokal

Kami menggunakan Docker Compose untuk orkestrasi lokal. Seluruh service dikonfigurasi untuk **Hot Reloading** (perubahan kode langsung terasa tanpa restart container).

### Cara Menjalankan:
```bash
docker compose up -d
```

### URL Lokal Penting:
- **API Gateway (Traefik)**: `http://localhost:8081`
- **Dashboard Traefik**: `http://localhost:8091`
- **MailCatcher (Email Test)**: `http://localhost:1080`
- **Postgres Database**: `localhost:5432`

---

## 💻 2. Pengembangan Per Service

Setiap service berada di dalam folder `services/`. Kami menggunakan [**uv**](https://docs.astral.sh/uv/) untuk manajemen paket Python yang sangat cepat.

### Contoh: Masuk ke Auth Service
```bash
cd services/auth-service
# Install dependensi lokal
uv sync
# Jalankan test
uv run bash scripts/tests-start.sh
```

### Tips Pengembangan:
1.  **Shared Secret**: Pastikan `SECRET_KEY` di `.env` sama untuk semua service agar JWT bisa divalidasi silang secara lokal.
2.  **Shared Database**: Untuk saat ini, kedua service berbagi satu database PostgreSQL. Pastikan skema tabel tetap terpisah secara logis.

---

## 🧪 3. Pengujian (Testing)

Kami menyediakan skrip otomatis untuk mengetes seluruh ekosistem sekaligus:

```bash
# Jalankan semua unit test di semua service
./scripts/test-services.sh
```

---

## 🧹 4. Linting & Formatting

Kami menggunakan `prek` (alternatif modern pre-commit) untuk menjaga kualitas kode.

```bash
# Jalankan linting pada semua file
uv run prek run --all-files
```

---

## 📜 5. Dokumentasi API (Swagger)

Setiap service memiliki dokumentasi Swagger-nya sendiri, namun semuanya dapat diakses melalui Gateway:
- **Auth Service Docs**: `http://api.localhost:8081/docs` (Routed from `/api/v1/login`, `/api/v1/users`, etc.)
- **Item Service Docs**: `http://api.localhost:8081/docs` (Routed from `/api/v1/items`)

> [!NOTE]
> Karena Traefik melakukan routing berdasarkan PathPrefix, jika Anda membuka `/docs`, Anda mungkin melihat dokumentasi dari salah satu service tergantung pada aturan prioritas. Untuk melihat dokumentasi spesifik, Anda bisa mengakses port service secara langsung (misal: `:8001/docs` untuk auth, `:8002/docs` untuk items) jika port tersebut diekspos di `compose.override.yml`.
