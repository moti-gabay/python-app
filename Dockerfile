# Base image עם Python 3.12
FROM python:3.12-slim

# התקנת ספריות מערכת חיוניות ל-pyodbc + ODBC Driver 18
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    apt-transport-https \
    g++ \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# התקנת Microsoft ODBC Driver 18 ל-SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18

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
