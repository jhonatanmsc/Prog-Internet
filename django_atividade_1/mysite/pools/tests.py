import datetime

from django.urls import reverse
from django.utils import timezone
from django.test import TestCase

from .models import *


def criar_questao(question_text, days):
    """
    Crie uma pergunta com o `question_text` fornecido e publique o número dado
    de "dias" compensados até agora (negativo para questões publicadas no passado,
    positivo para questões que ainda não foram publicadas).
    """
    data = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=data)


class QuestionIndexViewTests(TestCase):
    def test_sem_questoes(self):
        """
        Caso não haja questões, manda uma mensagem de aviso.
        """
        resposta = self.client.get(reverse('pools:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Não existem questões publicadas.")
        self.assertQuerysetEqual(resposta.context['ultimas_questoes'], [])

    def test_questao_passada(self):
        """
        Questões no passado que são mostradas na index.
        """
        criar_questao(question_text="Questão passada", days= -30)
        resposta = self.client.get(reverse('pools:index'))
        self.assertQuerysetEqual(resposta.context['ultimas_questoes'], ['<Question: Questão passada.>'])

    def test_questao_futura(self):
        """
        Questions no futuro não devem ser mostradas na index.
        """
        criar_questao(question_text="Questão futura.", days=30)
        resposta = self.client.get(reverse('pools:index'))
        self.assertContains(resposta, "Não existem questões publicadas.")
        self.assertQuerysetEqual(resposta.context['ultimas_questoes'], [])

    def test_questoes_futuras_e_passadas(self):
        """
        Se existirem tanto questões no futuro tanto no passado, somente
        as no passado deverão ser mostradas.
        """
        criar_questao(question_text="Questão passada.", days=-30)
        criar_questao(question_text="Questão futura.", days=30)
        resposta = self.client.get(reverse('pools:index'))
        self.assertQuerysetEqual(resposta.context['ultimas_questoes'], ['<Question: Questão passada.'])

    def test_multiplas_questoes_no_passado(self):
        """
        A index deverá, se possível, mostrar múltiplas questões.
        """
        criar_questao(question_text='Questão passada 1.', days= -30)
        criar_questao(question_text='Questão passada 2.', days= -5)
        resposta = self.client.get(reverse('pools:index'))
        self.assertQuerysetEqual(resposta.context['ultimas_questoes'],
                                 ['<Question: Questão passada 2.>', '<Question: Questão passada 1.>'])

class QuestionModelsTest(TestCase):

    def test_foi_publicado_recentemente_no_futuro(self):
        data_futura = timezone.now() + datetime.timedelta(days=30)
        questao_futura = Question(pub_date=data_futura)
        self.assertIs(questao_futura.was_published_recently(), False)

    def test_foi_publicado_recentemente_como_questao_antiga(self):
        data = timezone.now() - datetime.timedelta(days=1, seconds=1)
        questao_antiga = Question(pub_date=data)
        self.assertIs(questao_antiga.was_published_recently(), False)

    def test_foi_publicada_recentemente_como_questao_recente(self):
        data = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        questao_recente = Question(pub_date=data)
        self.assertIs(questao_recente.was_published_recently(), True)


class ShowQuestionViewTests(TestCase):

    def test_questao_futura(self):
        """
        Ao procurar detalhes de uma questão publicada no futuro
        um erro 404 deverá acontecer.
        """
        questao_futura = criar_questao(question_text='Questão futura.', days=5)
        url = reverse('pools:exibir_questao', args=(questao_futura.pk,))
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 404)

    def test_questao_no_passado(self):
        """
        Questões no passado deverão ter seus textos exibidos.
        """
        questao_passada = criar_questao(question_text='Questão no passado.', days= -5)
        url = reverse('pools:exibir_questao', args=(questao_passada.pk,))
        resposta = self.client.get(url)
        self.assertContains(resposta, questao_passada.question_text)