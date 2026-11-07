# Continuous Integration Project PGC

*Proyecto de universidad - SEGUNDO BLOQUE-PROYECTO - VIRTUAL/INTEGRACIÓN CONTINUA-[GRUPO B02]*

## Entrega Proyecto 1 (Escenario 3)

Proyecto que demuestra la integración continua y orquestación de contenedores usando Docker, FastAPI y MongoDB.

## Instrucciones para levantar el proyecto localmente

1. **Clonar el repositorio:**
   ```bash
   git clone <url-de-tu-repositorio>
   cd continuous-integration-project-PGC
   ```

2. **Configurar variables de entorno:**
   Crea un archivo llamado `.env` en la raíz del proyecto con el siguiente contenido:
   ```env
   MONGO_USER=admin
   MONGO_PASS=secretpassword
   PORT=5000
   ```

3. **Ejecutar Docker Compose:**
   Construye y levanta los servicios en segundo plano ejecutando:
   ```bash
   docker compose up -d --build
   ```

4. **Acceder a la API:**
   Una vez que los contenedores estén corriendo, accede a la documentación interactiva (Swagger) de FastAPI en:
   [http://localhost:5000/docs](http://localhost:5000/docs)

## Servicios

- **api**: Aplicación backend en FastAPI (Puerto `5000`).
- **mongodb**: Base de datos NoSQL con volumen persistente (Puerto `27017`).

## Detener el proyecto

Para detener los servicios y eliminar los contenedores, ejecuta:
```bash
docker compose down
```