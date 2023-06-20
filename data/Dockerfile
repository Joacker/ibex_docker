FROM python:3.7.3-stretch

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip

ADD requirements.txt .
RUN pip install -r requirements.txt

COPY . .


CMD ["tail", "-f", "/dev/null"]