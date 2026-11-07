# continuous-integration-project-PGC
Proyecto de universidad - SEGUNDO BLOQUE-PROYECTO - VIRTUAL/INTEGRACIÓN CONTINUA-[GRUPO B02]

# Entrega Proyecto 1 (Escenario 3)

Proyecto que demuestra la integración continua y orquestación de contenedores usando Docker, FastAPI y MongoDB.

## Instrucciones para levantar el proyecto localmente

1. Clonar el repositorio.
2. Crear un archivo `.env` en la raíz copiando el contenido de `.env.example`:
   `cp .env.example .env`
3. Ejecutar Docker Compose:
   `docker compose up -d --build`
4. Acceder a la documentación interactiva (Swagger) de FastAPI en:
   `http://localhost:8000/docs`

## Servicios
* **api**: Aplicación backend en FastAPI (Puerto 8000).
* **mongodb**: Base de datos NoSQL con volumen persistente (Puerto 27017).