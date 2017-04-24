from django.shortcuts import render
from django.http import HttpResponse

from .models import words_NASA

def index(request):
	word_list = words_NASA.objects.all()
	return render(request, 'dictionary/home.html', context={'word_list': word_list})

