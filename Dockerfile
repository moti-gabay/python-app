# Base image עם Python 3.12
FROM python:3.12-slim

# התקנת ספריות מערכת חיוניות ל-pyodbc + ODBC Driver 18
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    apt-transport-https \
    g++ \
    unixodbc \
    unixodbc-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# התקנת Microsoft ODBC Driver 18 ל-SQL Server
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg \
    && curl -sSL https://packages.microsoft.com/config/ubuntu/22.04/prod.list -o /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18

# ספריית עבודה
WORKDIR /app

# העתקת קבצי requirements והתקנה
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל הקוד
COPY . .

# משתני סביבה
ENV PORT=10000
EXPOSE 10000

# הרצת Gunicorn עם workers מרובים ולוגים נקיים
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "main:app", "--workers", "2", "--log-level", "info", "--access-logfile", "-", "--error-logfile", "-"]
