FROM python:3.9-slim

WORKDIR /app
COPY app/app.py /app/app.py

CMD ["sh", "-c", "while true; do python app.py; sleep 100; done"]
