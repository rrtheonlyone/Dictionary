import csv, sys, os

project_dir = "C:/Users/rahul/Desktop/Dictionary/mysite/mysite" 

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from dictionary.models import words_NASA

data = csv.reader(open("C:/Users/rahul/Desktop/Dictionary/mysite/csv/data.csv"), delimiter=",")

for row in data:
	if row[0] != 'acronym':
		words = words_NASA()
		words.acronym = row[0]
		words.meaning = row[1]
		words.save()


