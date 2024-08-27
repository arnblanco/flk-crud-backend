import uuid
from django.db import models

class Company(models.Model):
    """
    Modelo que representa una empresa en el sistema.

    Atributos:
        id (UUID): Identificador único de la empresa, generado automáticamente.
        name (str): Nombre de la empresa.
        description (str): Descripción corta de la empresa.
        symbol (str): Símbolo de la empresa (abreviatura, ticker).
        alpha_vantage (JSONField): Información adicional de la empresa proveniente de Alpha Vantage, 
                                   almacenada en formato JSON (opcional).
    """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5)
    alpha_vantage = models.JSONField(blank=True, null=True)

    def __str__(self):
        """
        Retorna una representación en cadena del objeto Company.

        Returns:
            str: El nombre de la empresa.
        """
        return self.name
