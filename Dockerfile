FROM python:3.6-alpine3.8
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code

RUN python -m pip --no-cache install -r requirements.txt
