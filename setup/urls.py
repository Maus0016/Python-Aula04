"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home,listarChamados, novoChamado, fechar
from core.views import listar_categorias, nova_categoria, excluir_categoria


urlpatterns = [
    path('admin/', admin.site.urls),


    path('', home),
    path('listar_chamados/', listarChamados),
    path('novoChamado', novoChamado),
    path('fechar/<int>:id>', fechar , name='fechar_chamado'),
    path('listar_categorias', listar_categorias),
    path('nova_categoria', nova_categoria),
    path('excluir_categoria/<int>:id', nova_categoria, name='excluir_categoria'),
]