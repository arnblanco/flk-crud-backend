# NYSE API

Este proyecto es una API CRUD para gestionar información de empresas del NYSE. La API está desarrollada con Django y Django REST Framework, utilizando PostgreSQL como base de datos. También se integra con la API de Alpha Vantage para obtener información financiera en tiempo real.

## Requisitos

- Docker 20.10+
- Docker Compose 1.27+
- Python 3.10+
- PostgreSQL 12+

## Instalación y Ejecución con Docker

1. **Clona el repositorio:**

   `git clone https://github.com/tu-usuario/nyse-api.git`
   `cd nyse-api`

2. **Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:**
```
SECRET_KEY=tu_clave_secreta
DJANGO_CONFIGURATION=Dev  # O Prod si estás en producción
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=crud-db
POSTGRES_PORT=5432
ALPHAVANTAGE_KEY=tu_clave_api_alpha_vantage
```

3. **Construye y ejecuta los contenedores Docker:**

`docker-compose up --build -d`

Esto construirá las imágenes Docker para el proyecto y levantará los contenedores de PostgreSQL y Django.

4. **Accede a la aplicación:**

La API estará disponible en `http://127.0.0.1:8000/api/companies/`.

## Configuración del Proyecto

### Dependencias

El proyecto utiliza Poetry para la gestión de dependencias. Aquí están las principales dependencias definidas en `pyproject.toml`:

- **Django**: Framework web para construir la API.
- **psycopg2-binary**: Adaptador PostgreSQL para Django.
- **django-configurations**: Gestión de configuraciones para Django.
- **djangorestframework**: Para construir la API REST.
- **drf-yasg**: Generación de documentación Swagger para la API.
- **requests**: Para hacer solicitudes HTTP a la API de Alpha Vantage.

### Archivos Clave

- **Dockerfile**: Define cómo construir la imagen Docker para el proyecto.
- **docker-compose.yml**: Define los servicios necesarios, incluyendo la base de datos PostgreSQL y la aplicación Django.
- **pyproject.toml**: Configuración del proyecto y dependencias gestionadas por Poetry.
- **manage.py**: Utilidad de Django para ejecutar comandos administrativos.
- **core/settings.py**: Configuración principal del proyecto Django, incluyendo la base de datos y middleware.

## Uso

### Endpoints principales

- **GET /api/companies/**: Listar todas las empresas.
- **POST /api/companies/**: Crear una nueva empresa.
- **GET /api/companies/{id}/**: Obtener detalles de una empresa específica.
- **PUT /api/companies/{id}/**: Actualizar una empresa existente.
- **DELETE /api/companies/{id}/**: Eliminar una empresa.

### Documentación de la API

La documentación interactiva está disponible en:

- `http://127.0.0.1:8000/swagger/` (Swagger UI)
- `http://127.0.0.1:8000/redoc/` (ReDoc)

## Docker Compose

El archivo `docker-compose.yml` define dos servicios:

- **db**: Contenedor para la base de datos PostgreSQL.
- **web**: Contenedor para la aplicación Django.

El servicio `web` está configurado para ejecutar las migraciones y luego iniciar el servidor de desarrollo de Django.

### Comandos Docker Compose

- **Iniciar los contenedores:**

`docker-compose up`

- **Detener y eliminar los contenedores:**

`docker-compose down`

- **Ver logs de los contenedores:**

`docker-compose logs -f`

## Pruebas

Para ejecutar las pruebas dentro del contenedor de la aplicación, puedes usar el siguiente comando:

`docker-compose run web poetry run python manage.py test`

## Despliegue

Para despliegues en producción, asegúrate de:

1. Establecer `DJANGO_CONFIGURATION=Prod` en las variables de entorno.
2. Configurar adecuadamente las variables `ALLOWED_HOSTS` y `DEBUG` en `core/settings.py`.

## Licencia

Este proyecto está licenciado bajo la licencia BSD. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para cualquier duda o consulta, puedes contactarme a través de [oblancomorales@gmail.com](mailto:oblancomorales@gmail.com).
