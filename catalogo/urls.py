from django.urls import path

from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('bolos/', views.lista_bolos, name='lista_bolos'),
    path('bolos/novo', views.novo_bolo, name='novo_bolo')
]