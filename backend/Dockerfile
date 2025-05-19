# استخدم صورة Python خفيفة الوزن
FROM python:3.10-slim

# تثبيت بعض الأدوات الأساسية
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المتطلبات أولاً لتثبيت الباكجات
COPY requirements.txt .

# تثبيت الحزم المطلوبة
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# تعيين البورت (مهم لـ fly.io و railway)
EXPOSE 8080

# الأمر الافتراضي لتشغيل التطبيق
CMD ["python", "run.py"]
