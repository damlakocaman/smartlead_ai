# SmartLead AI
# SmartLead AI
INTEROCEANIC GLOBE markasına ait bir websitesi. Yapay zeka desteği ile uçtan uca lojistik süreçlerinin takibinde aktif katılımcılara yardım edecek. Bu websitesi firmalar için yeni kullanıcı kaydı yapabilen ve yapay zeka ile mesaj döndürebilen bir sistemdir.


# Detaylı özellikleri

- Müşteri ekleme
- Kayıtlı müşteri adaylarını listeleme
- İsim ve telefon bilgilerini görüntüleme
- Yapay zekâ destekli sohbet
- Groq API entegrasyonu
- PostgreSQL veritabanı kullanımı
- Flask REST API
- Wix arayüzü ile backend bağlantısı

# Kullanılan Teknolojiler

- **Frontend:** Wix
- **Backend:** Python / Flask
- **AI:** Groq API
- **Database:** PostgreSQL
- **Deployment:** Render

# API

Backend kısmı aşağıdaki işlemler ile ilgilidir.

- `GET /health` — Sunucunun çalışıp çalışmadığını kontrol eder.
- `GET /api/leads` — Müşteri adaylarını listeler.
- `POST /api/leads` — Yeni müşteri adayı ekler.
- `POST /api/sohbet` — Yapay zekâ ile sohbet isteği gönderir.

# Kurulum

Projeyi çalıştıran Python paketi:

```bash
pip install -r requirements.txt
