from django.urls import path
from .views import gerar_numero

urlpatterns = [
    path('', gerar_numero, name='index'),
]
