# pull the official base image
FROM python:3.9.5-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV VIRTUAL_ENV /env
ENV DEBUG False
ENV PATH /env/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV SECRET_KEY=$SECRET_KEY
ENV OMDB_API_KEY=$OMDB_API_KEY
ENV DB_NAME=$DB_NAME
ENV DB_HOST=$DB_HOST
ENV DB_PASSWORD=$DB_PASSWORD
ENV DB_USER=$DB_USER
ENV DB_PORT=$DB_PORT

# copy project
COPY . /app

# install dependencies
COPY ./requirements.txt /app

RUN apk update && apk add --virtual .build-deps \
    postgresql-dev gcc python3-dev musl-dev

RUN set -ex \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "moviedb.wsgi:application"]