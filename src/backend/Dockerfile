# Imagen
FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["/bin/bash", "-c", "cd /app && uvicorn api:app --host 0.0.0.0 --port 8000"]