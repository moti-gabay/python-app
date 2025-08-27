# בוחרים תמונת בסיס של Python
FROM python:3.13-slim

# יוצרים תיקיה לאפליקציה
WORKDIR /app

# מעתיקים קבצי דרישות ומתקינים אותם
COPY requirements.txt .
RUN pip install -r requirements.txt

# מעתיקים את כל קבצי הפרויקט
COPY . .

# מגדירים משתני סביבה
ENV FLASK_ENV=production
ENV PORT=10000

# מצביעים על הפורט שהקונטיינר יחשוף
EXPOSE 10000

# הפקודה שמריצה את האפליקציה באמצעות Gunicorn
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:10000", "--workers", "2", "--threads", "4"]
