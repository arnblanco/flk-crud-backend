from rest_framework import viewsets
from rest_framework.response import Response

from .models import Company
from .serializers import CompanyReadSerializer, CompanyWriteSerializer, CompanyReadFullSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las operaciones CRUD de la entidad Company.

    Este ViewSet maneja la creación, lectura, actualización y eliminación (CRUD) 
    de las instancias del modelo Company. Dependiendo del tipo de operación 
    (HTTP method) y la acción, se selecciona automáticamente el serializador adecuado.

    Atributos:
        queryset (QuerySet): El conjunto de consultas que devuelve todas las instancias del modelo Company.
    """
    queryset = Company.objects.all()

    def get_serializer_class(self):
        """
        Retorna la clase de serializador adecuada según la operación HTTP y la acción.

        - Para métodos POST, PUT, PATCH: utiliza CompanyWriteSerializer.
        - Para la acción 'retrieve': utiliza CompanyReadFullSerializer.
        - Para los demás casos: utiliza CompanyReadSerializer.

        Returns:
            Serializer class: La clase de serializador correspondiente.
        """
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return CompanyWriteSerializer

        if self.action == 'retrieve':
            return CompanyReadFullSerializer
        
        return CompanyReadSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Maneja la operación de lectura detallada (retrieve) para una instancia de Company.

        Este método sobrescribe el método retrieve predeterminado de ModelViewSet 
        para obtener una instancia específica del modelo Company y devolverla 
        serializada en la respuesta.

        Args:
            request (HttpRequest): El objeto de solicitud HTTP recibido.
            *args: Argumentos adicionales.
            **kwargs: Argumentos clave adicionales.

        Returns:
            Response: La respuesta HTTP con los datos serializados de la instancia.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
