# בוחרים תמונת בסיס של Python
FROM python:3.13-slim

# יוצרים תיקיה לאפליקציה
WORKDIR /app

# מעתיקים קבצי פרויקט
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# מגדירים משתני סביבה (אם רוצים)
ENV FLASK_ENV=development
ENV PORT=5000

# מצביעים על הפורט שהקונטיינר יחשוף
EXPOSE 5000

# הפקודה שמריצה את האפליקציה
CMD ["python", "main.py"]
