from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Location(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=300)

	def __str__(self):
		return  f'{self.name} {self.address}'

class Participant(models.Model):
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.email

class Meetup(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	organizer_email = models.EmailField()
	date = models.DateField()
	description = models.TextField()
	image =  models.ImageField(upload_to='images', null=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	participants = models.ManyToManyField(Participant, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Meetup, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.title} = {self.slug}'