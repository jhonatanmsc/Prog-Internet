from django.urls import path
from django.conf.urls import url

from .views import *

urlpatterns = [
    path('', home, name='home'),
    url(r'^questao/(?P<pk>[0-9]+)/$', exibir_questao, name='exibir_questao'),
]