# pull the official base image
FROM python:3.9.5-alpine

# set work directory
WORKDIR /app

# copy project
COPY . /app
COPY ./.env /app

# install dependencies
COPY ./requirements.txt /app

RUN apk update && apk add --virtual .build-deps \
    postgresql-dev gcc python3-dev musl-dev

RUN set -ex \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt

# set environment variables
ENV VIRTUAL_ENV /env
ENV DEBUG False
ENV PATH /env/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "moviedb.wsgi:application"]