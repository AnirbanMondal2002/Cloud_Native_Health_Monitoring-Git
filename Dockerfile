FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001
EXPOSE 8000
CMD ["python", "health_monitoring.py"]
