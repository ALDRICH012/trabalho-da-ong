from django.urls import path
from . import views

app_name = 'doacoes'

urlpatterns = [
    path('', views.home, name='home'),
    path('nova-doacao/alimento/', views.nova_doacao_alimento, name='nova_doacao_alimento'),
    path('nova-doacao/roupa/', views.nova_doacao_roupa, name='nova_doacao_roupa'),
    path('nova-doacao/higiene/', views.nova_doacao_higiene, name='nova_doacao_higiene'),
    path('lista-doacoes/', views.lista_doacoes, name='lista_doacoes'),
] 