from Parejas.herramientas import agregarViewURL
from .views import crear_persona

urlpatterns = [
    agregarViewURL('', crear_persona, 'crear_persona'),
]