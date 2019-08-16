# Importamos a função index() definida no arquivo views.py
from website import views
from django.urls import path

app_name = 'website'

# urlpatterns a lista de roteamentos de URLs para funções/Views
urlpatterns = [
    # GET /
    path('/lista', views.lista_funcionarios, name='lista_funcionarios'),
]
