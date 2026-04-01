# Panduan Pengembangan Microservices 🛠️

Dokumen ini menjelaskan cara mengembangkan, menguji, dan menjalankan microservices secara lokal pada branch `feat/microservices-split`.

## 🐋 1. Menjalankan Stack Lokal

Kami menggunakan Docker Compose untuk orkestrasi lokal. Hubungan antar service dikelola secara dinamis melalui Traefik.

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

Setiap service berada di dalam folder `services/`. Kami menggunakan [**uv**](https://docs.astral.sh/uv/) untuk manajemen paket Python yang efisien.

### Contoh: Masuk ke Auth Service
```bash
cd services/auth-service
# Install dependensi lokal
uv sync
# Jalankan unit test
uv run bash scripts/tests-start.sh
```

---

## 🧪 3. Pengujian (Testing)

Kami menyediakan skrip otomatis untuk mengetes seluruh ekosistem sekaligus:

```bash
# Jalankan semua unit test di semua service
./scripts/test-services.sh
```

---

## 📐 4. Skema Database Ter-decouple

Penting untuk menjaga pemisahan antar service pada level basis data:

1.  **Shared PostgreSQL**: Untuk saat ini, kedua service berbagi satu database PostgreSQL tetapi terpisah secara tabel.
2.  **Referential Integrity**: Gunakan UUID (misal: `owner_id`) untuk referensi antarentitas tanpa menggunakan kunci asing (`ForeignKey`) langsung di level SQLAlchemy guna menghindari keterikatan antar service.

---

## 📜 5. Dokumentasi API (Swagger)

Akses dokumentasi per-service melalui:
- **Auth Service Docs**: `http://api.localhost:8081/docs` (Routed from `/api/v1/login`, `/api/v1/users`, etc.)
- **Item Service Docs**: `http://api.localhost:8081/docs` (Routed from `/api/v1/items`)
