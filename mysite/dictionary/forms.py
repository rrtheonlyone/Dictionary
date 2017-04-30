from django import forms

from .models import Definition

class DictForm(forms.ModelForm):
	class Meta:
		model=Definition
		fields = [
			"user",
			"credentials" ,
			"word",
			"pictures",
			"acronym" ,
			"definition",
			"links" 
		]