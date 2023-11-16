# Use an official Python runtime as a parent image
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT 5000
ENV SECRET_KEY 'my-secret'
# 10 minutes
ENV ACCESS_TOKEN_EXPIRE_SEC 600

EXPOSE 5000

CMD ["python", "main.py", "--host", "0.0.0.0"]