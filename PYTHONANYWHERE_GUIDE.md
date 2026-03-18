# PythonAnywhere da Botni Sozlash (Webhook)

Botni PythonAnywhere bepul hostingiga **Webhook** orqali joylash bo'yicha qo'llanma.

### 1-qadam: Fayllarni yuklash
Loyihangizdagi barcha fayllarni PythonAnywhere ga yuklang (masalan, ZIP qilib yuklab, unzip qilishingiz mumkin).

### 2-qadam: Kutubxonalarni o'rnatish
PythonAnywhere **Bash** konsolini oching va quyidagi buyruqni bering:

```bash
pip install -r requirements.txt --user
```

### 3-qadam: Web App yaratish
1. **Web** bo'limiga o'ting.
2. **Add a new web app** tugmasini bosing.
3. **Next** -> **Flask** -> **Python 3.10** (yoki o'zingizga mos versiya) ni tanlang.
4. Path so'raganda, shunchaki Next bosing (keyinroq o'zgartiramiz).

### 4-qadam: WSGI faylini sozlash
Web app yaratilgach, **Code** bo'limida **WSGI configuration file** degan joy bor (masalan: `/var/www/username_pythonanywhere_com_wsgi.py`). O'sha faylga kiring va ichidagi hamma narsani o'chirib, quyidagini yozing:

```python
import sys
import os

# Loyiha papkasiga yo'l (Username o'rniga o'z loginligingizni yozing)
project_home = '/home/username/jonlitaxi'

if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Environment o'zgaruvchilarni yuklash (agar .env ishlatayotgan bo'lsangiz)
# from dotenv import load_dotenv
# load_dotenv(os.path.join(project_home, '.env'))

# flask_app.py dagi 'app' o'zgaruvchisini import qilamiz
from flask_app import app as application
```
*Eslatma: `username` va `jonlitaxi` (papkangiz nomi) to'g'ri ekanligiga ishonch hosil qiling.*

### 5-qadam: Webhookni ulash
Web appni ishga tushirganingizdan so'ng (Reload tugmasini bosing), bot Telegramga javob berishi uchun webhookni sozlash kerak.
Bash konsoliga qaytib, quyidagi buyruqni bering (o'z domeningiz bilan):

```bash
python set_webhook.py https://SizningLogin.pythonanywhere.com
```

Agar hammasi to'g'ri bo'lsa, "Yangi webhook muvaffaqiyatli o'rnatildi" degan yozuv chiqadi.

### Tayyor!
Endi botingiz 24/7 ishlaydi (agar PythonAnywhere bepul versiyasida bo'lsangiz, har 3 oyda kirib "Run until 3 months" tugmasini bosib turishingiz kerak).

⚠️ **Eslatma:** Webhook rejimida `scheduler` (fon vazifalari - masalan, haydovchi obunasini tekshirish) avtomatik ishlamasligi mumkin, chunki bepul hostingda saytga hech kim kirmasa, u uxlab qoladi. Buning uchun `UptimeRobot` kabi xizmatlardan saytingizga har 5 daqiqada so'rov yuborib turishni sozlashingiz mumkin.
