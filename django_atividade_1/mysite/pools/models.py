from django.db import models

class Question(models.Model):
	question_text = models.TextField()
	closed = models.BooleanField(default=False)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		mod = ('------------------------------'
				str(self.question_text)
				'data de criação: '+str(self.pub_date)
				'status: '+str(self.closed)
			)
		return mod

class Choice(models.Model):
	question = models.ManyToManyField(Question, null=True)
	choice_text = models.TextField()
	votes = models.IntegerField(default=0)

	def __str__(self):
		mod = (
			self.question
			'resposta: '+str(self.choice_text)
			'likes: '+str(self.votes)
		)
		return mod
