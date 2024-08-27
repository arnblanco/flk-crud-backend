# Usamos la imagen oficial de Python 3.10 en Alpine
FROM python:3.10-alpine

# Establecemos las variables de entorno para PostgreSQL
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalamos dependencias del sistema
RUN apk update && apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    build-base \
    bash \
    git \
    curl

# Instalamos Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Añadimos el directorio de instalación de Poetry al PATH
ENV PATH="/root/.local/bin:$PATH"

# Creamos el directorio de la app
WORKDIR /app

# Copiamos los archivos pyproject.toml y poetry.lock si existen
COPY pyproject.toml poetry.lock* /app/

# Instalamos las dependencias del proyecto
RUN poetry install --no-root

# Copiamos el resto del código de la aplicación
COPY . /app/

# Exponemos el puerto 8000 para Django
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
