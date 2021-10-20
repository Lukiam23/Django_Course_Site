from django import forms

from .models import Participant, Meetup

class RegistrationForm(forms.Form):
	email = forms.EmailField(label='Email')

class MeetupForm(forms.ModelForm):
	class Meta:
		model = Meetup
		fields = '__all__'