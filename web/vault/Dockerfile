FROM python:3-alpine

WORKDIR /usr/src/app/
RUN pip install --no-cache-dir flask

RUN mkdir -p files
COPY app.py flags.db ./
COPY files ./files

CMD ["python", "./app.py"]
