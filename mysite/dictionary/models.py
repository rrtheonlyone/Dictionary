from django.db import models

class words_NASA(models.Model):
	acronym = models.CharField(max_length=10)
	meaning = models.CharField(max_length=30)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.acronym + " " + self.meaning