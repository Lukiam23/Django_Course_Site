from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    meetups = [
        {
        'title': 'A First Meetup',
         'location': "Paris", 
         'slug': 'a-first-meetup' 
        },
        {
        'title': 'A Second Meetup', 
        'location': "Brazil", 
        'slug': 'a-second-meetup'
        },
        {
        'title': 'A Third Meetup', 
        'location': "Italia", 
        'slug': 'a-third-meetup' 
        },
        {
        'title': 'A Fourth Meetup', 
        'location': "Unganda", 
        'slug': 'a-fourth-meetup' 
        }
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):
    print(meetup_slug),
    selected_meetup = {
    'title': 'A First Meetup', 
    'description':'this is the first meetup'
    }

    return render(request,'meetups/meetup-details.html',{
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
        })