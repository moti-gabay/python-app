# בסיס: Python 3.11 slim
FROM python:3.11-slim

# הגדרות סביבת עבודה
WORKDIR /app

# התקנת כלי מערכת נחוצים
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# הוספת מקור Microsoft והתקנת ODBC Driver 18
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*

# העתקת קובץ הדרישות והתקנת החבילות
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל הקוד
COPY . .

# חשיפה של פורט 5000 (Flask default)
EXPOSE 5000

# פקודת הרצה
CMD ["python", "app.py"]
