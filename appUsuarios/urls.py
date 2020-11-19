from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_registros, name='registro_clientes'),
    path('persona/nueva', views.persona_nueva, name='persona_nueva'),
    path('clubLectores', views.lista_tarjetas, name='lista_tarjetas'),
    path('tarjetas_saldo', views.tarjetas_saldo, name='tarjetas_saldo'),
       
]
    