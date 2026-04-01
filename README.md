# FastAPI Microservices Split (Docker Compose) 🚀

Template ini mendemonstrasikan cara memecah **FastAPI Monolith** menjadi **Microservices** yang independen dan ter-orkestrasi melalui Docker Compose.

## 🏗️ Arsitektur Sistem

Proyek ini telah dipecah menjadi dua service inti:
- **`auth-service`**: Menangani Identitas, Login, dan User Management.
- **`item-service`**: Menangani operasional CRUD untuk Barang (Items).
- **`Traefik`**: Berfungsi sebagai API Gateway tunggal yang melakukan routing cerdas berdasarkan path URL.

## 🚀 Cara Menjalankan Secara Lokal

Pastikan Docker dan Docker Compose sudah terinstal di komputer Anda.

```bash
docker compose up -d --build
```
Aplikasi akan tersedia di `http://api.localhost:8081`.

---

## 📂 Panduan Dokumentasi

Pilih panduan pemeliharaan dan pengoperasian:

| Dokumen | Isi Utama |
| :--- | :--- |
| 🚢 [**Deployment**](./deployment.md) | Panduan mendeploy ke VPS menggunakan Docker Compose. |
| 🛠️ [**Development**](./development.md) | Konfigurasi lokal, cara menambah fitur, dan unit testing. |
| 🤝 [**Contributing**](./CONTRIBUTING.md) | Aturan berkontribusi dan standar penulisan kode microservices. |

---

## 🛠️ Struktur Proyek

```text
.
├── services/           # Folder Microservices
│   ├── auth-service/   # Identity & Access Management
│   └── item-service/   # Item Management
├── scripts/            # Utility & Automation Scripts
├── compose.yml         # Konfigurasi Production (Standard)
└── compose.override.yml # Konfigurasi Development Lokal
```

## 🧪 Verifikasi Cepat

```bash
# 1. Health Check (Identity Service)
curl -H "Host: api.localhost" http://localhost:8081/api/v1/utils/health-check/

# 2. Login (Dapatkan Token)
export TOKEN=$(curl -s -X POST -H "Host: api.localhost" -d "username=admin@example.com&password=changethis" http://localhost:8081/api/v1/login/access-token | jq -r .access_token)

# 3. Create Item (Item Service)
curl -X POST -H "Host: api.localhost" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"title": "Item Baru"}' http://localhost:8081/api/v1/items/
```

---
*Catatan: Jika Anda memerlukan orkestrasi Kubernetes, silakan cek branch `feat/kubernetes-helm`.*
