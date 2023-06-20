FROM python:3.10.8-slim-buster as builder

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip

ADD requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 3001

FROM python:3.10.8-slim-buster
COPY . /app
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin



ENTRYPOINT ["python"]
CMD ["main.py"]