FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir python-multipart==0.0.21
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8081

CMD ["python", "-m", "uvicorn", "ai_service.api.main:app", "--host", "0.0.0.0", "--port", "8081"]
