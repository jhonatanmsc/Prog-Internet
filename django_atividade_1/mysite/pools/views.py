from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice


class HomeView(generic.ListView):
    template_name = 'pools/index.html'
    context_object_name = 'ultimas_questoes'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5] #menor ou igual

class ShowQuestionView(generic.DetailView):
    model = Question
    template_name = 'pools/question.html'
    context_object_name = 'questao'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'pools/results.html'
    context_object_name = 'questao'


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

    return HttpResponseRedirect(reverse('pools:results', args=(questao.id,)))
