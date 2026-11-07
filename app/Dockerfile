# Imagen base oficial y versión fija
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]