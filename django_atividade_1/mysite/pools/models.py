from django.db import models

class Question(models.Model):
	question_text = models.TextField()
	closed = models.BooleanField(default=False)
	pub_date = models.DateTimeField(auto_now_add=True)