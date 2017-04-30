from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q

from .forms import DictForm
from .models import Definition

import wikipedia
import json

## API FUNCTIONS ##

def wiki_definition(search_word):
	try:
		return wikipedia.summary( search_word, sentences=2 )
	except:
		return "Please be more specific with your term"

def generate_NASA_pics_link(user_query):
    search_term = ''
    for character in user_query:
        if character == ' ':
            search_term += '+'
        else:
            search_term += character

    return "https://images.nasa.gov/#/search-results?q=" +search_term+ "&page=1&media=image&yearStart=1920&yearEnd=2017"

def generate_youtube_link(user_query):
    search_term = ''
    for character in user_query:
        if character == ' ':
            search_term += '+'
        else:
            search_term += character
    return 'https://www.youtube.com/results?search_query=' + search_term

##

## Django 
def home(request):
	word_list = Definition.objects.all()

	query = request.GET.get("q")

	if query:
		word_list = word_list.filter(
								Q(word__icontains=query)|
								Q(definition__icontains=query)
								).distinct()

		wiki = wiki_definition(query)
		imagesNASA = generate_NASA_pics_link(query)
		video = generate_youtube_link(query)

		relatedDict = "alpha"

		return render(request, 'dictionary/detail.html', context={'query':query, 'word_list': word_list, "wiki": wiki, "images": imagesNASA, "video": video, "related": relatedDict})

	else:
		return render(request, "dictionary/home.html")

def add_term(request):
	form = DictForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {"form": form}

	return render(request, "dictionary/definition_form.html", context)

