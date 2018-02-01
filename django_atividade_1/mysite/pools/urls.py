from django.urls import path

from .views import *

app_name = 'pools'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('questao/<int:pk>', ShowQuestionView.as_view(), name='exibir_questao'),
    path('questao/<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('questao/<int:pk>/manage/', ManageView.as_view(), name='manage'),
    path('questao/<int:pk>/vote', vote, name='vote'),
    path('questao/<int:pk>', deletar_questao, name='deletar_questao'),
    path('questao/<int:pk>', deletar_alternativa, name='deletar_alternativa'),
]