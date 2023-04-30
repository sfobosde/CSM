FROM python:3.10.7-alpine

EXPOSE 8000

ENV PYTHONUNBUFFERED 1
RUN mkdir /web_django
WORKDIR /web_django
COPY requirements.txt /web_django/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /web_django/
COPY . .

CMD [ "python", "csm-server/csm_django/manage.py", "runserver", "0.0.0.0:8000" ]