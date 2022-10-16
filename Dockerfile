FROM python:3.10

WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY src/* /app/*

CMD ["python3", "/app/src/main.py"]