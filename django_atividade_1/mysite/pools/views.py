from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Question


def home(request):
    questoes = Question.objects.all()
    objetos = {
        'questoes': questoes
    }
    return render(request, 'pools/index.html', objetos)

def exibir_questao(request, pk):
    questao = get_object_or_404(Question, pk=pk)
    objetos = {
        'questao': questao,
        'alternativas': questao.alternativas_associadas.all()
    }
    return render(request, 'pools/question.html', objetos)
