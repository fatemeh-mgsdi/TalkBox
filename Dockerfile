# define the global arguments
ARG PYTHON_VERSION=3.8

# base image
FROM python:${PYTHON_VERSION} as base

LABEL MAINTAINER "Fatemeh maghsoudi <fatemeh.mnaghsoudi76>"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# set work directory
COPY . /src/

WORKDIR /src

RUN pip install --upgrade pip && pip install --no-cache-dir -r /src/requirements.txt


ENTRYPOINT [ "./docker-entrypoint.sh" ]
