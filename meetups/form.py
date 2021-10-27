from django import forms

from .models import Participant, Meetup
from django.template.defaultfilters import slugify

class RegistrationForm(forms.Form):
	email = forms.EmailField(label='Email')

class MeetupForm(forms.ModelForm):
	class Meta:
		model = Meetup
		fields = ['title','organizer_email','date','description','image','location','participants']
		widgets ={
			'title' : forms.TextInput(attrs={'class':'form-control'}),
			'organizer_email' : forms.EmailInput(attrs={'class':'form-control'}),
			'date' : forms.DateInput(attrs={'class':'form-control'}),
			'description' : forms.Textarea(attrs={'class':'form-control'}),
			'image' : forms.FileInput(attrs={'class':'form-control'}),
			'location' : forms.Select(attrs={'class':'form-control'}),
			'participants' : forms.SelectMultiple(attrs={'class':'form-control'}),
		} 
	

class MeetupUpdate(forms.ModelForm):
	class Meta:
		model = Meetup
		fields = ['title','organizer_email','date','description','image','location','participants']
		widgets ={
			'title' : forms.TextInput(attrs={'class':'form-control'}),
			'organizer_email' : forms.EmailInput(attrs={'class':'form-control'}),
			'date' : forms.DateInput(attrs={'class':'form-control'}),
			'description' : forms.Textarea(attrs={'class':'form-control'}),
			'image' : forms.FileInput(attrs={'class':'form-control'}),
			'location' : forms.Select(attrs={'class':'form-control'}),
			'participants' : forms.SelectMultiple(attrs={'class':'form-control'}),
		} 


	def save(self, commit=True):
		meetup = self.instance
		meetup.title = self.cleaned_data['title']
		meetup.slug = slugify(meetup.title)
		meetup.organizer_email = self.cleaned_data['organizer_email']
		meetup.date = self.cleaned_data['date']
		meetup.description = self.cleaned_data['description']
		meetup.image = self.cleaned_data['image']
		meetup.location = self.cleaned_data['location']
		meetup.participants.set(self.cleaned_data['participants'])

		if commit:
			meetup.save()
		return meetup

