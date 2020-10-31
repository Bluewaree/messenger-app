FROM python:3.7-alpine3.10
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && apk add libffi-dev py-cffi \
  && apk add curl openssh bash  \
  && apk add postgresql-client \
  && pip install pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --dev
ADD . ./


