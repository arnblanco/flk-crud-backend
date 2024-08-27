from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet

# Se crea una instancia del enrutador por defecto de Django REST Framework
router = DefaultRouter()
# Se registra el ViewSet de Company en el enrutador bajo el prefijo 'companies'
router.register(r'companies', CompanyViewSet)

# Se incluyen las rutas generadas por el enrutador en las URLs del proyecto
urlpatterns = [
    path('', include(router.urls)),
]
