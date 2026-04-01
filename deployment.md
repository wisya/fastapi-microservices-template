# Panduan Deployment: Microservices 🚀

Dokumen ini merinci berbagai cara untuk mendeploy sistem microservices Anda ke lingkungan produksi.

## 🏁 Opsi Deployment

Kami mendukung dua metode utama deployment:
1.  **Docker Compose (Standard)**: Cocok untuk VPS tunggal atau server kecil.
2.  **Kubernetes via Helm (Advanced)**: Cocok untuk cluster besar yang butuh *auto-scaling* dan *high-availability*.

---

## 🐋 1. Deployment via Docker Compose (VPS)

Metode ini menggunakan **Traefik** sebagai Reverse Proxy tunggal untuk seluruh microservices.

### Persiapan Server
- Sistem Operasi: Linux (Ubuntu 20.04+ direkomendasikan).
- **Docker** & **Docker Compose** terinstal.
- Buat network publik: `docker network create traefik-public`.

### Langkah-langkah:
1.  **Konfigurasi `.env`**: Atur `DOMAIN`, `SECRET_KEY`, dan `POSTGRES_PASSWORD`.
2.  **Jalankan Traefik**:
    ```bash
    docker compose -f compose.traefik.yml up -d
    ```
3.  **Jalankan Microservices**:
    ```bash
    docker compose -f compose.yml up -d --build
    ```

---

## ☸️ 2. Deployment via Kubernetes (Helm)

Metode ini menggunakan **Helm Chart** generik yang terletak di `./charts/fastapi-app`.

### Persiapan
- Cluster Kubernetes aktif (Minikube, K3s, GKE, EKS).
- **Helm** terinstal di mesin lokal.

### Perintah Deployment:

**Deploy Auth Service**:
```bash
helm upgrade --install auth-service ./charts/fastapi-app \
  -f ./charts/fastapi-app/values.yaml \
  -f ./charts/fastapi-app/values-auth.yaml \
  --set secrets.SECRET_KEY="rahasia-anda"
```

**Deploy Item Service**:
```bash
helm upgrade --install item-service ./charts/fastapi-app \
  -f ./charts/fastapi-app/values.yaml \
  -f ./charts/fastapi-app/values-items.yaml \
  --set secrets.SECRET_KEY="rahasia-anda"
```

---

## 🛠️ Manajemen Environment (Secrets)

> [!CAUTION]
> Jangan pernah membagikan file `.env` atau `values-*.yaml` yang berisi kredensial asli ke repositori publik.
> Gunakan **GitHub Secrets** untuk menyimpan variabel sensitif pada pipeline CI/CD.

| Variabel | Deskripsi | Default (Local) |
| :--- | :--- | :--- |
| `SECRET_KEY` | Kunci tanda tangan JWT | `changethis` |
| `POSTGRES_PASSWORD` | Password root Database | `changethis` |
| `DOMAIN` | Domain publik (Ingress Host) | `localhost` |

---

## 📈 Monitoring & Health Checks

Setiap service memiliki endpoint kesehatan di:
- `http://<domain>/api/v1/utils/health-check/`

Traefik Dashboard (Local): `http://localhost:8091`
