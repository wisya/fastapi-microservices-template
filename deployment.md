# Panduan Deployment: Microservices (Docker Compose) 🐋

Dokumen ini merinci cara mendeploy sistem microservices Anda ke lingkungan produksi menggunakan Docker Compose.

## 🏁 Persiapan Server

1.  **Server VPS**: Siapkan server Linux (Ubuntu 20.04+ direkomendasikan).
2.  **Docker & Compose**: Pastikan Docker dan Docker Compose sudah terinstal.
3.  **DNS**: Arahkan domain Anda (misal: `api.contoh.com`) ke IP server.
4.  **Docker Network**: Buat network untuk Traefik:
    ```bash
    docker network create traefik-public
    ```

---

## 🛠️ Langkah Deployment

### 1. Konfigurasi Environment
Salin file `.env` dan sesuaikan variabel produksi:
- `DOMAIN`: Domain asli Anda.
- `SECRET_KEY`: Gunakan string acak yang aman.
- `POSTGRES_PASSWORD`: Ganti dari nilai default.

### 2. Jalankan API Gateway (Traefik)
Traefik akan menangani pembuatan sertifikat SSL (HTTPS) secara otomatis.
```bash
docker compose -f compose.traefik.yml up -d
```

### 3. Jalankan Microservices
```bash
docker compose -f compose.yml up -d --build
```

---

## 🛰️ Struktur Service & Routing

Sistem ini menggunakan routing berbasis path melalui Traefik:

| Path Prefix | Target Service | Deskripsi |
| :--- | :--- | :--- |
| `/api/v1/login` | `auth-service` | Autentikasi |
| `/api/v1/users` | `auth-service` | Manajemen User |
| `/api/v1/items` | `item-service` | Manajemen Barang |
| `/api/v1/utils` | `auth-service` | Utilitas & Health Check |

---

## 📈 Monitoring

Setiap service memiliki endpoint kesehatan yang bisa dipantau:
- `http://<domain>/api/v1/utils/health-check/`

Dashboard Traefik (Internal): `http://localhost:8091`

---
> [!NOTE]
> Untuk deployment skala besar menggunakan Kubernetes, silakan merujuk ke branch `feat/kubernetes-helm`.
