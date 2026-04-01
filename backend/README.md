# ⚠️ Project Moved / Dipindahkan ⚠️

Proyek ini telah bermigrasi dari arsitektur monolit (single backend) menjadi **Microservices**. 

Seluruh kode utama, model, dan API yang sebelumnya berada di folder ini sekarang telah dipindahkan dan dikembangkan secara independen di dalam folder **`services/`**.

### Struktur Baru (Docker Compose):
- **Identity & Auth**: [services/auth-service/](../services/auth-service/)
- **Items Management**: [services/item-service/](../services/item-service/)

Meskipun folder `backend/` ini masih dipertahankan untuk referensi migrasi sementara, **jangan melakukan pengembangan di folder ini lagi.** Gunakan folder `services/` untuk penambahan fitur baru.

---
*Silakan baca [README.md utama](../../README.md) untuk panduan integrasi sistem.*
