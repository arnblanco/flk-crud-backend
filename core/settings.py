import os
from pathlib import Path
from configurations import Configuration

# Global Settings
class Common(Configuration):
    """
    Configuración base común para todos los entornos.
    """
    
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    ALLOWED_HOSTS = []
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'corsheaders', # Django Cors Headers
        'rest_framework',  # Django REST Framework para construir APIs
        'drf_yasg',  # Herramienta para generar documentación de API con Swagger
        '_apps.api',  # Aplicación personalizada del proyecto
    ]
    
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'core.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'core.wsgi.application'

    # Configuración de Loggin para registrar errores
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': 'errors.log',  # Archivo donde se registran los errores
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }
    
    # Configuración de la Base de Datos usando PostgreSQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('POSTGRES_DB', ''),
            'USER': os.getenv('POSTGRES_USER', ''),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
            'HOST': os.getenv('POSTGRES_HOST', ''),
            'PORT': os.getenv('POSTGRES_PORT', ''),
            'OPTIONS': {
                'options': '-c search_path=public'  # Define el esquema por defecto
            },
        }        
    }

    # Validación de contraseñas
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Internacionalización
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_TZ = True

    # Configuración de archivos estáticos
    STATIC_URL = 'static/'
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración para entornos de desarrollo
class Dev(Common):
    """
    Configuración específica para el entorno de desarrollo.
    """
    CORS_ALLOWED_ORIGINS = ['http://localhost:5173',]
    ALLOWED_HOSTS = ['localhost']
    DEBUG = True  # Habilita el modo de depuración

# Configuración para entornos de producción
class Prod(Common):
    """
    Configuración específica para el entorno de producción.
    """
    ALLOWED_HOSTS = []
    DEBUG = False 
