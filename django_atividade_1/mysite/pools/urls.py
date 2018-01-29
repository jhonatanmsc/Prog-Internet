from django.urls import path

from .views import *

app_name = 'pools'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('questao/<int:pk>', exibir_questao, name='exibir_questao'),
    path('questao/<int:pk>/resultados', results, name='results'),
    path('questao/<int:pk>/vote', vote, name='vote'),
    # path('questao/<int:pk>/', DetailView.as_view(), name='exibir_questao'),
    # path('questao/<int:pk>/resultados/', ResultsView.as_view(), name='results'),
]