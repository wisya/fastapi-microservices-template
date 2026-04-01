# FastAPI Microservices Template 🚀

Selamat datang di template **FastAPI Microservices** yang fleksibel dan siap untuk di-deploy ke produksi. Proyek ini telah berevolusi dari monolit menjadi arsitektur microservices modern yang ter-orkestrasi dengan baik.

## 🏗️ Arsitektur Sistem

Sistem ini terdiri dari dua service inti yang berjalan secara independen:
- **`auth-service`**: Pintu gerbang identitas (Registrasi, JWT Auth, User Management).
- **`item-service`**: Pengelolaan data barang dengan skema basis data yang ter-decouple.
- **`Traefik`**: Berperan sebagai API Gateway dan Ingress Controller.

## 🚀 Quick Start (Docker Compose)

Cara termudah untuk mencoba proyek ini secara lokal adalah menggunakan Docker Compose:

```bash
docker compose up -d --build
```
Aplikasi akan tersedia di `http://api.localhost:8081`.

## 📂 Panduan Dokumentasi

Pilih panduan yang Anda butuhkan:

| Dokumen | Isi Utama |
| :--- | :--- |
| 🛠️ [**Development**](./development.md) | Konfigurasi lokal, cara menambah fitur, dan unit testing. |
| 🚢 [**Deployment**](./deployment.md) | Panduan deploy ke VPS (Docker Compose) dan Kubernetes (Helm). |
| 🛡️ [**Security**](./SECURITY.md) | Kebijakan keamanan dan pelaporan kerentanannya. |
| 🤝 [**Contributing**](./CONTRIBUTING.md) | Aturan berkontribusi dan standar penulisan kode microservices. |

---

## 🧪 Pengujian Cepat (curl)

Gunakan perintah ini untuk memverifikasi sistem:

```bash
# 1. Health Check (Identity Service)
curl -H "Host: api.localhost" http://localhost:8081/api/v1/utils/health-check/

# 2. Login (Dapatkan Token)
export TOKEN=$(curl -s -X POST -H "Host: api.localhost" -d "username=admin@example.com&password=changethis" http://localhost:8081/api/v1/login/access-token | jq -r .access_token)

# 3. Create Item (Item Service)
curl -X POST -H "Host: api.localhost" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"title": "Item Baru"}' http://localhost:8081/api/v1/items/
```

## 🛠️ Struktur Proyek

```text
.
├── charts/             # Kubernetes Helm Charts
├── services/           # Folder Microservices
│   ├── auth-service/   # Identity & Access Management
│   └── item-service/   # Item Management
├── scripts/            # Utility & Automation Scripts
├── compose.yml         # Konfigurasi Production (Standard)
└── compose.override.yml # Konfigurasi Development Lokal
```

---
*Dibuat oleh Antigravity untuk skalabilitas super cepat.*
