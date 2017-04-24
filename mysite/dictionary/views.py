from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from .models import words_NASA

def index(request):
	word_list = words_NASA.objects.all()

	query = request.GET.get("q")

	if query:
		word_list = word_list.filter(
									Q(meaning=query)|
									Q(acronym=query)
									)
		return render(request, 'dictionary/home.html', context={'word_list': word_list})

	else:
		return render(request, 'dictionary/home.html', context={'word_list': word_list})

