from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'pools/index.html'
    context_object_name = 'ultimas_questoes'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'pools/question.html'
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'pools/results.html'


def home(request):
    ultimas_cinco_questoes_registradas = Question.objects.order_by('-pub_date')[:5]
    context = {
        'ultimas_cinco_questoes_registradas': ultimas_cinco_questoes_registradas
    }
    return render(request, 'pools/index.html', context)

def exibir_questao(request, pk):
    questao = get_object_or_404(Question, pk=pk)
    return render(request, 'pools/question.html', {'questao':questao})

def results(request, pk):
    questao = get_object_or_404(Question, pk=pk)
    return render(request, 'pools/results.html', {'questao':questao})

def vote(request, pk):
    questao = get_object_or_404(Question, pk=pk)
    try:
        alternativa = questao.alternativas_associadas.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'questao': questao,
            'error_message': 'Você não selecionou uma opção.',
        }
        return render(request, 'pools/question.html', context)

    else:
        alternativa.votes += 1
        alternativa.save()
    # if(request.method == 'POST'):
    #     pk_ch = request.POST['choice']
    #     ch = Choice.objects.get(pk=pk_ch)
    #     ch.votes += 1
    #     ch.save()
    return HttpResponseRedirect(reverse('pools:results', args=(questao.id,)))
