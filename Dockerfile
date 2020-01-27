FROM python:3.7

WORKDIR /deploy/app

COPY . /deploy/app

RUN set -ex && pip install --no-cache-dir pipenv

RUN set -ex && pipenv install --ignore-pipfile --deploy --system
