# Usa una imagen base de Python 3.10 slim
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#ENV MYSQLCLIENT_CFLAGS =
#ENV MYSQLCLIENT_LDFLAGS =

WORKDIR /app

#COPY requirements.txt /app/
RUN apt-get update
RUN apt-get install gcc default-libmysqlclient-dev -y

# install dependencies
RUN pip install -U pip setuptools wheel
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# copy project
COPY . .

# Convert plain text files from Windows or Mac format to Unix
RUN apt-get install dos2unix

COPY . /app/
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
