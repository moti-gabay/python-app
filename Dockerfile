# Base image
FROM python:3.12-slim

# התקנת ספריות מערכת חיוניות ל-pyodbc + ODBC Driver 18
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    apt-transport-https \
    build-essential \
    unixodbc \
    unixodbc-dev \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# התקנת Microsoft ODBC Driver 18 ל-SQL Server
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/ubuntu/22.04/prod jammy main" > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*

# הגדרת משתני סביבה ל־ODBC
ENV LD_LIBRARY_PATH=/opt/microsoft/msodbcsql18/lib64:$LD_LIBRARY_PATH

# ספריית עבודה
WORKDIR /app

# העתקת קובץ requirements ותקנת ספריות Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל הקוד
COPY . .

# משתני סביבה ל-Render
ENV PORT=10000
EXPOSE 10000

# Start command מותאם ל-Render
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "main:app", "--workers", "2", "--log-level", "info", "--access-logfile", "-", "--error-logfile", "-"]
