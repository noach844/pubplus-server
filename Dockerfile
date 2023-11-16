# Use an official Python runtime as a parent image
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# ENV NAME World

CMD ["python", "main.py", "--host", "0.0.0.0"]

