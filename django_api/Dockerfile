FROM python:3-slim

ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=1
ENV DJANGODIR=/django_api
ENV REQDIR=requirements

RUN mkdir $DJANGODIR
WORKDIR $DJANGODIR
COPY $REQDIR $REQDIR

RUN apt-get -y update && apt-get install -y gettext
RUN pip3 install -r requirements/development.txt

COPY . $DJANGODIR

RUN apt install nano