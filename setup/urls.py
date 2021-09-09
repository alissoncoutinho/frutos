"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from frutos.views import PessoasViewSet, ReunioesViewSet, FrequenciasViewSet, ListaFrequenciasPorPessoa, ListaFrequenciasPorReuniao
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pessoas', PessoasViewSet, basename='Pessoas')
router.register('reunioes', ReunioesViewSet, basename='Reunioes')
router.register('frequencias', FrequenciasViewSet, basename='Frequencias')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('pessoas/<int:pk>/frequencia/',ListaFrequenciasPorPessoa.as_view()),
    path('reunioes/<int:pk>/frequencia/',ListaFrequenciasPorReuniao.as_view())
]
