from django.urls import path

from .views import *

app_name = 'pools'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('questao/<int:pk>', ShowQuestionView.as_view(), name='exibir_questao'),
    path('questao/<int:pk>/resultados/', ResultsView.as_view(), name='results'),
    path('questao/<int:pk>/vote', vote, name='vote'),
]