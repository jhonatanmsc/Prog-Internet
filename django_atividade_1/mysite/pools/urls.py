from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('questao/<int:pk>', exibir_questao, name='exibir_questao'),
]