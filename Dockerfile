FROM python:3.12-slim

WORKDIR /main

COPY requirements.txt .

RUN /bin/sh -c pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5010

CMD [ "gunicorn", "--workers", "4", "--bind", "0.0.0.0:5010", "main:main" ]