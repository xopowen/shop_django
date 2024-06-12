FROM python:3.9.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN mkdir /shop_django/

COPY . /shop_django/

WORKDIR /shop_django

RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt
EXPOSE 8000

#FROM python:3.9.0
#
#RUN mkdir /app/
#RUN mkdir /app/shop_django/
#COPY . /app/shop_django/
#
#WORKDIR /app
#
#RUN pip install --upgrade pip
#RUN pip install gunicorn
#RUN pip install -r shop_django/requirements.txt
#EXPOSE 8000