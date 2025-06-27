# Dockerfile
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto (opcional, útil para documentación)
EXPOSE 8080

# Comando por defecto
CMD ["gunicorn", "djcrm.wsgi:application", "--bind", "0.0.0.0:8080"]
