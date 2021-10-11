from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    meetups = [
        {'title': 'A First Meetup'},
        {'title': 'A Second Meetup'},
        {'title': 'A Third Meetup'},
        {'title': 'A Fourth Meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': False,
        'meetups': meetups
    })