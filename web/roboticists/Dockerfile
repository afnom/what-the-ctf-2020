FROM python:3-alpine

WORKDIR /usr/src/app/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY robots.txt .
COPY templates ./templates
COPY static ./static

CMD ["python", "./server.py"]

