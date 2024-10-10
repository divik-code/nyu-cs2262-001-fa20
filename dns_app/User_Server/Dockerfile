FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install Flask requests

EXPOSE 8080

CMD ["python", "./US.py"]