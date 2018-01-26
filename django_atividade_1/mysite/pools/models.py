from django.db import models


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

    class Meta:
        ordering = ['-pub_date']


class Choice(models.Model):
    question = models.ForeignKey('Question', null=True, related_name='alternativas_associadas', on_delete=models.CASCADE)
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        mod = (
            self.question + '\n' +
            'resposta: ' + str(self.choice_text) + '\n' +
            'likes: ' + str(self.votes) + '\n'
        )
        return mod
