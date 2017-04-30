from django.db import models
from django.core.urlresolvers import reverse

class Definition(models.Model):
	user = models.CharField(max_length=20)
	credentials = models.CharField(max_length=50, blank=True)
	word = models.CharField(max_length=10)
	acronym = models.CharField(max_length=10, blank=True)
	pictures = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
	definition = models.CharField(max_length=30)
	links = models.CharField(max_length=50, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.word + " " + self.definition

	def get_absolute_url(self):
		return reverse("dictionary:home")

