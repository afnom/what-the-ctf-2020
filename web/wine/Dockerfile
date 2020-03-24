FROM python:3

WORKDIR /usr/src/app/
RUN pip install --no-cache-dir flask

RUN mkdir -p static templates complaints
COPY app.py ./
COPY static ./static
COPY templates ./templates
COPY app.py ./app.py
COPY secret.flag ./secret.flag

CMD ["python", "./app.py"]
