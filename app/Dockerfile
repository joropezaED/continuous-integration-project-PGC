# Dockerfile para la aplicación FastAPI
# Construye la imagen de la aplicación FastAPI con sus dependencias
# Utiliza la imagen base de Python 3.11 slim
# Establece el directorio de trabajo en /app
# Copia las dependencias e instálalas
# Copia el código fuente
# Expone el puerto 5000
# Comando de inicio

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]