# 🛡️ DevOps Shield — Uptime & Server Monitoring Service

<p align="center">
  <img src="https://github.com/ibrohim0811/Devshield/blob/master/favicon/logo.png" alt="I>_Develop Logo" width="400">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django_DRF-4.2+-red?style=for-the-badge&logo=django&logoColor=white" alt="Django DRF">
  <img src="https://img.shields.io/badge/PostgreSQL-15-blue?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Celery-5.3-green?style=for-the-badge&logo=celery&logoColor=white" alt="Celery">
  <img src="https://img.shields.io/badge/Redis-⚡-red?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
</p>

---

## 📝 Loyiha Haqida

**DevOps Shield** — bu serverlar, veb-saytlar va API endpointlarining uzluksiz ishlashini (Uptime) real vaqt rejimida kuzatib borish uchun yaratilgan asinxron monitoring tizimi. Foydalanuvchilar o'z saytlarini tizimga qo'shishadi, dastur esa fonda har daqiqa ularni tekshirib, muammo bo'lganda zudlik bilan ogohlantiradi.

> ✨ *Ushbu loyiha barcha xavfsizlik va yuqori yuklama (High-Load) talablariga javob beradigan professional arxitekturada qurilgan.*

---

## 🚀 Asosiy Imkoniyatlari (Features)

* **Real-time Monitoring:** Saytlarning holatini (`200 OK`, `404`, `500`) va javob berish tezligini sekundma-sekund kuzatish.
* **Asinxron Background Tasks:** Saytlarni asinxron fonda tekshirish uchun `Celery` va `Redis` integratsiyasi.
* **Xavfsizlik (Password Limiting):** Brute-force hujumlaridan himoya qiluvchi IP-ga asoslangan `DRF Throttling` tizimi.
* **Vaqt Zonasi:** O'zbekiston vaqti (`Asia/Tashkent`) bilan to'liq moslashtirilgan loglar tizimi.
* **Avtomatik Hujjatlar:** `drf-spectacular` orqali OpenAPI 3.0 va interaktiv `Swagger UI` hujjatlashtirish.

---

## 🛠️ Texnologiyalar Tizimi (Tech Stack)

* **Backend:** Django REST Framework (DRF)
* **Baza:** PostgreSQL (Ma'lumotlar aniqligi uchun `DecimalField` va tezkor qidiruv uchun `index=True` ustunlar)
* **Task Queue:** Celery & Redis Cache
* **API Documentation:** OpenAPI v3 (`drf-spectacular`)

---

## 💻 Loyihani Ishga Tushirish

### 1. Loyihani yuklab olish va virtual muhitni yoqish
```bash
git clone [https://github.com/sizning_github_username/devops_shield.git](https://github.com/sizning_github_username/devops_shield.git)
cd devops_shield
python -m venv venv
source venv/bin/activate  # Windows uchun: venv\Scripts\activate