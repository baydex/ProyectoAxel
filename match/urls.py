from Parejas.herramientas import agregarViewURL
from .views import cargar_match

urlpatterns = [
    agregarViewURL("", cargar_match, "cargar_match")
]