FROM python:3.10.8-slim-buster as builder

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip

ADD requirements.txt .
RUN pip install -r requirements.txt

COPY . .


CMD ["tail", "-f", "/dev/null"]