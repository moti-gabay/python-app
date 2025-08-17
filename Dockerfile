# בסיס Ubuntu עם Python
FROM python:3.13-slim

# התקנת ODBC Driver
RUN apt-get update && \
    apt-get install -y curl gnupg apt-transport-https unixodbc-dev && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | tee /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18

# קבצי אפליקציה
WORKDIR /app
COPY . /app

# התקנת חבילות Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# חשיפה לפורט של Flask
EXPOSE 5000

# הרצת האפליקציה
CMD ["python", "app.py"]
