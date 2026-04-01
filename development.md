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

- **Auth Service Docs**: [http://localhost:8001/docs](http://localhost:8001/docs)
- **Item Service Docs**: [http://localhost:8002/docs](http://localhost:8002/docs)

> [!NOTE]
> Akses dokumentasi secara langsung melalui port service sangat disarankan selama pengembangan lokal untuk menghindari ambiguitas routing di API Gateway.
