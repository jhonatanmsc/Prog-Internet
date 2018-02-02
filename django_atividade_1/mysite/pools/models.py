import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.TextField()
    closed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        mod = ('------------------------------\n' +
               str(self.question_text) + '\n' +
               'data de criação: ' + str(self.pub_date) + '\n' +
               'status: ' + str(self.closed) + '\n'
               )
        return mod

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_qtd_choice(self):
        return len(self.alternativas_associadas.all())

    def get_qtd_votes(self):
        total_votes = 0
        for choice in self.alternativas_associadas.all():
            total_votes += choice.votes
        return total_votes


    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publicado recentemente?'

    class Meta:
        ordering = ['-pub_date']


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='alternativas_associadas', on_delete=models.CASCADE)
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def get_percen(self):
        if self.votes == 0:
            return 0
        total = 0
        for i in self.question.alternativas_associadas.all():
            total += i.votes
        return str("%.2f" % ((self.votes/total) * 100))
