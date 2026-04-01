# Panduan Kontribusi Microservices 🤝

Terima kasih telah tertarik untuk berkontribusi! Untuk menjaga ekosistem microservices tetap bersih dan skalabel, harap ikuti panduan berikut.

## 🛠️ Pengembangan Lokal

Sebelum berkontribusi, pastikan Anda telah membaca [**Panduan Pengembangan**](./development.md). 

### Aturan Emas Microservices:
1.  **Loose Coupling**: Hindari membuat dependensi langsung (seperti relasi `ForeignKey` lintas database) antar service di level kode. Gunakan UUID untuk referensi ID.
2.  **Shared Logic**: Jika Anda menemukan logika yang sama di dua service (misal: `app/core/security.py`), pertimbangkan untuk menduplikasi sementara atau sampaikan di diskusi untuk dibuat menjadi *shared library*.
3.  **Independensi**: Setiap service harus bisa dijalankan dan di-test secara mandiri.

---

## 🧪 Aturan Pengujian

1.  **Setiap Fitur = Satu Test**: Pastikan setiap rute baru memiliki unit test di folder `tests/` milik service tersebut.
2.  **Coverage**: Kami menjaga cakupan kode di atas **80%**. Jalankan `./scripts/test-services.sh` sebelum melakukan Pull Request.

---

## 🛰️ Pull Request (PR)

Saat mengirimkan PR:
1.  Sebutkan service mana yang terdampak (misal: `[auth-service] fix login bug`).
2.  Pastikan `uv run prek run --all-files` lulus untuk menjaga format kode.
3.  Jika ada perubahan skema database, sertakan file migrasi **Alembic** di dalam folder service yang bersangkutan.

---

## 💡 Diskusi Terlebih Dahulu

Untuk **perubahan besar** (menambah service baru, mengubah arsitektur gateway), harap buka [GitHub Discussion](../../discussions) terlebih dahulu.

Terima kasih telah membangun masa depan microservices bersama kami! 🙇
