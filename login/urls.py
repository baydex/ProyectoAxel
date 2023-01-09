from .views import registro
from Parejas.herramientas import agregarViewURL

app_name = 'login'

urlpatterns = [
    agregarViewURL('', registro, 'sign_up'),
]