# Base image עם Python 3.12
FROM python:3.12-slim

# התקנת ספריות מערכת חיוניות ל-pyodbc
RUN apt-get update && apt-get install -y \
    g++ \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# הגדרת ספריית עבודה
WORKDIR /app

# העתקת קבצי הדרישות
COPY requirements.txt .

# התקנת תלויות Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# העתקת קוד הפרויקט
COPY . .

# הגדרת הפורט ש-Render ישתמש בו
ENV PORT=10000

# פקודת הרצה של השרת Flask
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
