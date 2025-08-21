# Base image עם Python 3.12
FROM python:3.12-slim

# התקנת ספריות מערכת חיוניות ל-pyodbc + ODBC Driver 18
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    apt-transport-https \
    g++ \
    unixodbc-dev \
    build-essential \
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

# הגדרת משתני סביבה חיוניים (אפשר להגדיר גם ב-Render UI)
ENV PORT=10000
ENV DB_DRIVER="ODBC Driver 18 for SQL Server"
ENV DB_SERVER="tcp:minyan-sql-server.database.windows.net,1433"
ENV DB_DATABASE="my-sql-server"
ENV DB_USERNAME="sqladminuser"
ENV DB_PASSWORD="MyStrongPassword!123"
ENV SECRET_KEY="moti_secret_key123"
ENV TOKEN_KEY="token"
ENV MAIL_SERVER="smtp.gmail.com"
ENV MAIL_PORT=587
ENV MAIL_USE_TLS=True
ENV MAIL_USERNAME="motigabay18@gmail.com"
ENV MAIL_PASSWORD="zgxt jxxd ixhy nzmu"
ENV MAIL_DEFAULT_SENDER="motigabay18@gmail.com"
ENV SITE_OWNER_EMAIL="motigabay18@gmail.com"

# פתיחת הפורט
EXPOSE 10000

# פקודת הרצה של השרת Flask עם gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
