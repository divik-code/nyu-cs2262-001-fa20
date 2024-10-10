FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install Flask

EXPOSE 9090

CMD ["python", "./FS.py"]