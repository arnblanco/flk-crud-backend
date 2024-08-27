from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración del esquema de la API
schema_view = get_schema_view(
   openapi.Info(
      title="NYSE API",  # Título de la documentación de la API
      default_version='v1',  # Versión de la API
      description="Django NYSE Crud API Documentation",  # Descripción de la API
      terms_of_service="https://www.google.com/policies/terms/",  # Términos de servicio
      contact=openapi.Contact(email="oblancomorales@gmail.com"),  # Información de contacto
      license=openapi.License(name="BSD License"),  # Licencia de la API
   ),
   public=True,  # Especifica si la documentación debe ser pública
   permission_classes=(permissions.AllowAny,),  # Permite el acceso a cualquier usuario
)

# Definición de las rutas
urlpatterns = [
    # Ruta para la interfaz Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # Ruta para la interfaz Redoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Ruta para obtener el esquema de la API en formato JSON
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    # Incluye las rutas de la aplicación API
    path('api/', include('_apps.api.urls')),
]
