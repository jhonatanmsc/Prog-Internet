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

    class Meta:
        ordering = ['-pub_date']


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='alternativas_associadas', on_delete=models.CASCADE)
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
