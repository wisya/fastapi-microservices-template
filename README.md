# FastAPI Microservices Template

Pembaruan arsitektur dari monolit menjadi **Microservices**. Proyek ini telah dipecah menjadi dua service independen yang dikelola melalui **Traefik** sebagai API Gateway.

## Arsitektur Microservices

Proyek ini terbagi menjadi dua service utama:
- **`auth-service`**: Menangani registrasi, login, manajemen user, dan utilitas kesehatan sistem.
- **`item-service`**: Menangani operasional CRUD untuk *Items* (barang/sumber daya).

### Teknologi yang Digunakan:
- **Backend**: FastAPI & SQLModel (Pydantic v2).
- **Gateway**: Traefik (Reverse Proxy & Load Balancer).
- **Database**: PostgreSQL (Shared Database Pattern).
- **Package Management**: [uv](https://docs.astral.sh/uv/) (Sangat cepat).

---

## Cara Menjalankan Service

### 1. Persiapan Environment
Pastikan Docker dan Docker Compose sudah terinstal. Salin file `.env` dan sesuaikan nilainya jika diperlukan (default sudah cukup untuk lokal).

### 2. Jalankan dengan Docker Compose
Gunakan perintah berikut untuk membangun dan menjalankan seluruh service:

```bash
docker compose up -d --build
```

Service akan tersedia di:
- **API Gateway**: [http://localhost:8081](http://localhost:8081)
- **Auth Service Docs**: [http://api.localhost:8081/docs](http://api.localhost:8081/docs) (Host: `api.localhost`)
- **Item Service Docs**: [http://api.localhost:8081/docs](http://api.localhost:8081/docs) (Terintegrasi via Traefik routing)
- **Traefik Dashboard**: [http://localhost:8091](http://localhost:8091)

---

## Contoh Eksekusi & Pengujian Endpoint

Berikut adalah urutan pengujian lengkap menggunakan `curl`. Gunakan header `Host: api.localhost` karena Traefik melakukan routing berdasarkan domain tersebut.

### A. Service Autentikasi (`auth-service`)

**1. Registrasi User Baru**
```bash
curl -X POST -H "Host: api.localhost" -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "securepassword123", "full_name": "User Test"}' \
  http://localhost:8081/api/v1/users/signup
```

**2. Login untuk Mendapatkan Token**
```bash
# Simpan token ke variabel agar mudah digunakan
export TOKEN=$(curl -s -X POST -H "Host: api.localhost" \
  -d "username=user@example.com&password=securepassword123" \
  http://localhost:8081/api/v1/login/access-token | jq -r .access_token)

echo "Token Anda: $TOKEN"
```

**3. Health Check Sistem**
```bash
curl -H "Host: api.localhost" http://localhost:8081/api/v1/utils/health-check/
```

### B. Service Barang (`item-service`)

**1. Membuat Item Baru (Butuh Token)**
```bash
curl -X POST -H "Host: api.localhost" -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"title": "Laptop Gaming", "description": "High performance laptop"}' \
  http://localhost:8081/api/v1/items/
```

**2. List Semua Item**
```bash
curl -H "Host: api.localhost" -H "Authorization: Bearer $TOKEN" \
  http://localhost:8081/api/v1/items/
```

---

## Struktur Proyek

- `services/auth-service/`: Kode sumber service identitas dan auth.
- `services/item-service/`: Kode sumber service manajemen barang.
- `compose.yml`: Konfigurasi service untuk produksi.
- `compose.override.yml`: Konfigurasi untuk pengembangan lokal (Hot Reloading).

## Pengembangan Lokal
Untuk fitur **Hot Reloading**, kami melakukan *volume mounting* pada folder `app/`. Setiap perubahan kode di direktori `services/*/app/` akan langsung memicu restart otomatis di dalam container tanpa perlu build ulang.
