FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5002

ENV FLASK_APP=src/app.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5002"]
