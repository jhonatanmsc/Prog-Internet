from django.urls import path
from django.conf.urls import url

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('^questao/<int:pk>', exibir_questao, name='exibir_questao'),
]