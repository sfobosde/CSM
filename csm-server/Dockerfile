FROM python:3.10.7-alpine

EXPOSE 8000

RUN apk update
RUN apk add gcc musl-dev
RUN apk add --no-cache mariadb-dev

ENV PYTHONUNBUFFERED 1
RUN mkdir /web_django
WORKDIR /web_django
COPY requirements.txt /web_django/

RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /web_django/
COPY . .

# Задаем создание миграции для приложения.
#CMD [ "python", "csm-server/csm_django/manage.py", "makemigrations", "db"]

# Миграция данных.
#CMD [ "python", "csm-server/csm_django/manage.py", "migrate"]

#CMD [ "python", "csm-server/csm_django/manage.py", "runserver", "0.0.0.0:8000" ]