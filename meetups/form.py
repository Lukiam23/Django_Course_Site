from django import forms

from .models import Participant

class RegistationForm(forms.ModelForm):
		
	class Meta:
		model = Participant
		fields = ['email'] #especifica os campos que serão mostrados no formulário