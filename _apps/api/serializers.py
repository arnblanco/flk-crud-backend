import os
import requests
from rest_framework import serializers
from .models import Company

class CompanyReadSerializer(serializers.ModelSerializer):
    """
    Serializador para la lectura de datos básicos de la entidad Company.

    Este serializador incluye los campos esenciales que se exponen al cliente 
    cuando se solicita información básica de una empresa.
    """
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'symbol']


class CompanyReadFullSerializer(serializers.ModelSerializer):
    """
    Serializador para la lectura detallada de la entidad Company, 
    incluyendo datos externos de Alpha Vantage.

    Este serializador extiende el CompanyReadSerializer añadiendo el campo 
    'alpha_vantage' que contiene información adicional y un campo 'time_serie' 
    que se obtiene a través de la API de Alpha Vantage.
    """
    time_serie = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'symbol', 'alpha_vantage', 'time_serie']

    def get_time_serie(self, obj):
        """
        Obtiene la serie temporal diaria de la empresa desde la API de Alpha Vantage.

        Args:
            obj (Company): La instancia de Company para la que se solicita la serie temporal.

        Returns:
            dict: Los datos de la serie temporal en formato JSON obtenidos de la API.
        """
        # Obtén el símbolo y la clave de API del entorno
        symbol = obj.symbol
        api_key = os.getenv('ALPHAVANTAGE_KEY', '')

        # Crea la URL para la consulta de la API
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

        # Envía una solicitud GET a la API
        response = requests.get(url)

        # Analiza la respuesta JSON
        data = response.json()

        # Retorna los datos de la API
        return data


class CompanyWriteSerializer(serializers.ModelSerializer):
    """
    Serializador para la creación y actualización de la entidad Company.

    Este serializador maneja la validación del símbolo de la empresa y obtiene 
    información adicional desde la API de Alpha Vantage para almacenarla en la 
    base de datos.
    """
    class Meta:
        model = Company
        fields = ['name', 'description', 'symbol']

    def validate_symbol(self, value):
        """
        Valida el símbolo de la empresa y obtiene información adicional desde la API.

        Args:
            value (str): El símbolo de la empresa a validar.

        Returns:
            str: El símbolo en mayúsculas si es válido.

        Raises:
            serializers.ValidationError: Si el símbolo no es válido o no se encuentra información.
        """
        symbol_upper = value.upper()

        data = self.get_company_data(symbol_upper)
        if not data:
            raise serializers.ValidationError("El símbolo no es válido o no se encontró información.")
        
        # Guarda el response en el campo `alpha_vantage`
        self.company_data = data
        return symbol_upper

    def get_company_data(self, symbol):
        """
        Obtiene los datos de la empresa desde la API de Alpha Vantage.

        Args:
            symbol (str): El símbolo de la empresa.

        Returns:
            dict: Los datos de la empresa en formato JSON si existen.

        Raises:
            serializers.ValidationError: Si ocurre un error al contactar la API o si la clave de API no está configurada.
        """
        alphavantage_key = os.getenv('ALPHAVANTAGE_KEY', '')
        if not alphavantage_key:
            raise serializers.ValidationError("API key for Alpha Vantage is not set.")
        
        url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={alphavantage_key}'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            raise serializers.ValidationError(f"Error while contacting Alpha Vantage API: {str(e)}")
        
        # Retorna el JSON si existe y si es igual al símbolo ingresado.
        return data if 'Symbol' in data and data['Symbol'] == symbol else None

    def create(self, validated_data):
        """
        Crea una nueva instancia de Company, almacenando los datos de Alpha Vantage.

        Args:
            validated_data (dict): Los datos validados para crear la instancia.

        Returns:
            Company: La instancia de Company creada.
        """
        # Actualiza los datos validados con el response de la API
        validated_data['alpha_vantage'] = self.company_data
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia existente de Company, almacenando los datos de Alpha Vantage.

        Args:
            instance (Company): La instancia de Company a actualizar.
            validated_data (dict): Los datos validados para actualizar la instancia.

        Returns:
            Company: La instancia de Company actualizada.
        """
        # Actualiza los datos validados con el response de la API
        validated_data['alpha_vantage'] = self.company_data
        return super().update(instance, validated_data)
