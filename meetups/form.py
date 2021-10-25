from django import forms

from .models import Participant, Meetup

class RegistrationForm(forms.Form):
	email = forms.EmailField(label='Email')

class MeetupForm(forms.ModelForm):
	class Meta:
		model = Meetup
		fields = ['title','organizer_email','date','description','image','location','participants']
		widgets ={
			'title' : forms.TextInput(attrs={'class':'form-control'}),
			'slug' : forms.TextInput(attrs={'class':'form-control'}),
			'organizer_email' : forms.EmailInput(attrs={'class':'form-control'}),
			'date' : forms.DateInput(attrs={'class':'form-control'}),
			'description' : forms.Textarea(attrs={'class':'form-control'}),
			'image' : forms.FileInput(attrs={'class':'form-control'}),
			'location' : forms.Select(attrs={'class':'form-control'}),
			'participants' : forms.SelectMultiple(attrs={'class':'form-control'}),
		} 