FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["sh", "-c", "while true; do python app.py; sleep 180; done"]