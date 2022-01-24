FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN apt-get update 

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install


COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app