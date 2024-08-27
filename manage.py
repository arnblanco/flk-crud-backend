#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Obtiene la configuración de Django desde una variable de entorno
DJANGO_CONFIGURATION = os.getenv('DJANGO_CONFIGURATION', '')

def main():
    """Run administrative tasks."""
    # Establece el módulo de configuración de Django por defecto
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
    # Establece la configuración de Django desde una variable de entorno
    os.environ.setdefault("DJANGO_CONFIGURATION", DJANGO_CONFIGURATION)
    
    try:
        # Importa y ejecuta el comando desde django-configurations
        from configurations.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Ejecuta el comando en la línea de comandos
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
